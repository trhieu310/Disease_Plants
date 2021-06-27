import os
import cv2
import pickle
import numpy as np
from imutils import paths
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing
import tensorflow as tf
import PIL
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import models
import MobileNetV2


dataset = r'data'

def pretrain(img):
    image = cv2.resize(img, (180, 180))
    image = np.reshape(image, (180, 180, 3))
    return image

print("[INFO] loading images...")
X = []
Y = []
imagePaths = list(paths.list_images(dataset))
classes =  0
lb = LabelEncoder()

for _, dirnames, _ in os.walk(dataset):
    classes += len(dirnames)

total = 0
dem = 0
for (i, imagePath) in enumerate(imagePaths):
    print("[INFO] processing image {}/{}".format(i + 1,len(imagePaths)))
    for (i, imagePath) in enumerate(imagePaths):
        # print("[INFO] processing image {}/{}".format(i + 1,len(imagePaths)))
        image = cv2.imread(imagePath)
        image = pretrain(image)
        label = imagePath.split(os.path.sep)[-2]
        X.append(image)
        Y.append(label)
    total += 1
print("\n[INFO] serializing {} encodings...".format(total))

trainX, testX, trainY, testY = train_test_split(X, Y, test_size=0.2)
trainX = np.array(trainX)/255.
testX = np.array(testX)/255.
trainY = to_categorical(np.array(lb.fit_transform(trainY)))
testY = to_categorical(np.array(lb.fit_transform(testY)))
print(testX.shape)
print(testY.shape)
print(trainX.shape)
print(trainY.shape)
# x_train = preprocessing.StandardScaler().fit(np.array(x_train, dtype='float') / 255.0)
# a = lb.inverse_transform(datase(labels[2]))
print(lb.classes_)
print("\n[INFO] done...")


epochs = 30

model = MobileNetV2((256,256,3), classes)
model.summary()

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

aug = ImageDataGenerator(
    rotation_range=30, width_shift_range=0.15,
    height_shift_range=0.15, shear_range=0.15, 
    zoom_range=0.2,horizontal_flip=True, 
    fill_mode="nearest")

history = model.fit_generator(aug.flow(trainX, trainY, batch_size = 32), epochs = epochs, validation_data = (testX, testY))

test_loss, test_acc = model.evaluate(x = testX, y= testY, batch_size=32, verbose=1)
# print(test_acc)

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

model.save("modelss.h5")

epochs_range = range(epochs)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()