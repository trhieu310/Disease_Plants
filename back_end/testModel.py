import cv2
import numpy as np
from imutils import paths
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import load_model
import os
import random
import matplotlib.pylab as plt

data = r'validation'
imagePaths = list(paths.list_images(data))
# classes =  0
# lb = LabelEncoder()

labels = ['BrownSpot', 'Healthy', 'Hispa', 'LeafBlast', 'LeafBlight', 'SheathBlight', 'Tungro']

model = load_model('model.h5')

def pretrain(img):
  image = cv2.resize(img, (256,256))
  image = np.reshape(image, (256,256, 3))
  image = image /255.
  return image
  

def predict(image):
    probabilities = model.predict(np.asarray([image]))[0]
    class_idx = np.argmax(probabilities)
    
    return {labels[class_idx]: probabilities[class_idx]*(99/101)}

# for idx, imagePath in enumerate(random.sample(imagePaths, 10)):
for idx, imagePath in enumerate(imagePaths):
    print("SOURCE: name: %s, path: %s" % (os.path.split(imagePath)[-1], imagePath))
    
    img = cv2.imread(imagePath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    image = pretrain(img)
    # image = np.expand_dims(image, 0)
    prediction = predict(image)
    print("PREDICTED: class: %s, confidence: %f" % (list(prediction.keys())[0], list(prediction.values())[0]))
    plt.title("name: %s,\n class: %s,\n confidence: %f" % (os.path.split(imagePath)[-1], list(prediction.keys())[0], list(prediction.values())[0]))
    plt.imshow(img)
    # plt.figure(idx)    
    plt.show()