
# Required imports
import os
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app
import cv2
import numpy as np

ASSETS_DIR = os.path.dirname(os.path.abspath(__file__))
# Initialize Flask app
app = Flask(__name__)

# Initialize Firestore DB
cred = credentials.Certificate(
    'plant-e7169-firebase-adminsdk-vv9mb-c8a6f499fe.json')
default_app = initialize_app(cred)
db = firestore.client()
todo_ref = db.collection('Disease')


@app.route('/add', methods=['POST'])
def create():
    """
        create() : Add document to Firestore collection with request body.
        Ensure you pass a custom ID as part of json body in post request,
        e.g. json={'id': '1', 'title': 'Write a blog post'}
    """
    try:
        id = request.json['id']
        todo_ref.document(id).set(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"


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


@app.route('/query', methods=['GET'])
def read1():
    """
        read() : Fetches documents from Firestore collection as JSON.
        todo : Return document that matches query ID.
        all_todos : Return all documents.
    """
    try:
        # Check if ID was passed to URL query
        todo_id = request.args.get(1)
        if todo_id:
            todo = todo_ref.document(todo_id).get()
            return jsonify(todo.to_dict()), 200
        else:
            all_todos = [doc.to_dict() for doc in todo_ref.stream()]
            return jsonify(all_todos), 200
    except Exception as e:
        return f"An Error Occured: {e}"


@app.route('/update', methods=['POST', 'PUT'])
def update():
    """
        update() : Update document in Firestore collection with request body.
        Ensure you pass a custom ID as part of json body in post request,
        e.g. json={'id': '1', 'title': 'Write a blog post today'}
    """
    try:
        id = request.json['id']
        todo_ref.document(id).update(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"


@app.route('/delete', methods=['GET', 'DELETE'])
def delete():
    """
        delete() : Delete a document from Firestore collection.
    """
    try:
        # Check for ID in URL query
        todo_id = request.args.get('id')
        todo_ref.document(todo_id).delete()
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def allowed_file(filename):
    extension = filename.rsplit('.', 1)[1].lower()
    return '.' in filename and extension in ALLOWED_EXTENSIONS


@app.route('/predict', methods=['POST', 'PUT'])
def predict():
    try:

        print(request)

        if 'img' not in request.files:
            return jsonify({
                "error": True,
                'message': 'Missing file'
            }), 100
        file = request.files['img']
        if file.filename == '':
            return jsonify({
                "error": True,
                'message': 'No file selected'
            }), 200

        if file and allowed_file(file.filename):

            filestr = file.read()
            img = np.frombuffer(filestr, np.uint8)
            img = cv2.imdecode(img, cv2.IMREAD_COLOR)
            img = cv2.resize(img, (128, 128))
            img = np.reshape(img, (128, 128, 3))
            # img = cv2.reshape(img, (128, 128, 3))
            cv2.imshow("window_name", img)
            cv2.waitKey(0)
            # closing all open windows
            cv2.destroyWindow("window_name")

            return jsonify({"success": True,  "name": request.form['disease']}), 200

    except Exception as e:
        print(e)
        return f"An Error Occured: {e}"


port = int(os.environ.get('PORT', 8080))

if __name__ == '__main__':
    # context = ('./localhost.csr', './localhost.key')
    # app.run(threaded=True, host='0.0.0.0', port=port, ssl_context='adhoc')
    app.run(threaded=True, host='0.0.0.0', port=port)