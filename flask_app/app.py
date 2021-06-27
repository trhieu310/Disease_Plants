from flask import Flask
from flask import request
from flask import jsonify
import os
import cv2
from flask.helpers import url_for
import numpy as np
from PIL import Image
import io
import imutils
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from werkzeug.utils import redirect, secure_filename
from firebase_admin import credentials, firestore, initialize_app

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


app = Flask(__name__)

cred = credentials.Certificate(
    'plant-e7169-firebase-adminsdk-vv9mb-6fba92240c.json')
default_app = initialize_app(cred)
db = firestore.client()
todo_ref = db.collection('Disease')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def model():
    global model
    model = load_model('model_tool_train.h5')

def pretrain(img):
  image = cv2.cvtColor(np.float32(img), cv2.COLOR_BGR2RGB)
  image = cv2.resize(image, (256,256))
  image = np.reshape(image, (256,256, 3))
  image = image /255.
  return image

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "name": "He thong bao ve cay trong",
        "api": "[POST] /predict"
    }), 200

@app.route('/list', methods=['GET'])
def read():
    """
        read() : Fetches documents from Firestore collection as JSON.
        todo : Return document that matches query ID.
        all_todos : Return all documents.
    """
    try:
        # Check if ID was passed to URL query
        todo_id = request.args.get('id')
        if todo_id:
            todo = todo_ref.document(todo_id).get()
            return jsonify(todo.to_dict()), 200
        else:
            all_todos = [doc.to_dict() for doc in todo_ref.stream()]
            return jsonify(all_todos), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        print(request)
        if 'img' not in request.files:
            return jsonify({
                "error": True,
                'message': 'Missing file'
            }), 100
        file = request.files['img']
        print(file)
        if file.filename == '':
            return jsonify({
                "error": True,
                'message': 'No file selected'
            }), 200
        try:
            if file and allowed_file(file.filename):
                filename = Image.open(file)   
            img = pretrain(filename)
            img = image.img_to_array(img)
            cv2.imshow("ded", img)
            cv2.waitKey(0)
            img = np.expand_dims(img, 0)
            pred = model.predict(img)
            pred = np.argmax(np.round(pred), axis=0)
            return jsonify({
                'filename': str(file.filename),
                'message': 'Success',
                'name': str(pred[0]),
            })
        except Exception as e:
            print (e)
            return jsonify({
                'message': 'Server error'
            }), 300
            # return jsonify({"success": True,  "name": request.form['disease']}), 200

    except Exception as e:
        print(e)
        return f"An Error Occured: {e}"

port = int(os.environ.get('PORT', 8080))
if __name__ == "__main__":

    # port = int(os.environ.get('PORT', 8080))

    print(("* Loading Keras model and Flask starting server..."
           "please wait until server has fully started"))
    model()
    # app.run(threaded=True, host='0.0.0.0', port=8080)
    app.run(threaded=True, host='0.0.0.0', port=port)
