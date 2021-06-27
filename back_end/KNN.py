# import os
# import cv2
# import numpy as np
# from imutils import paths
# from tensorflow.keras.utils import to_categorical
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from sklearn import preprocessing
# import tensorflow as tf
# import PIL
# import matplotlib.pyplot as plt
# from sklearn.metrics import accuracy_score
# import scipy.spatial
# from sklearn.preprocessing import LabelEncoder
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import classification_report
# from collections import Counter

# class KNN:
#     def __init__(self, k):
#         self.k = k

#     def fit(self, X, y):
#         self.trainX = X
#         self.trainY = y

#     def distance(self, X1, X2):
#         distance = scipy.spatial.distance.euclidean(X1, X2)
#         return distance

#     def predict(self, testData):
#         final_output = []
#         for i in range(len(testData)):
#             d = []
#             votes = []
#             for j in range(len(trainX)):
#                 dist = self.distance(trainX[j] , testX[i])
#                 d.append([dist, j])
#             d.sort()
#             d = d[0:self.k]
#             for d, j in d:
#                 votes.append(trainY[j])
#             ans = Counter(votes).most_common(1)[0][0]
#             final_output.append(ans)

#         return final_output

#     def score(self, testX, testY):
#         predictions = self.predict(testX)
#         return (predictions == testY).sum() / len(testY)

# dataset = r'data'

# def pretrain(img):
#     image = cv2.resize(img, (128,128))
#     image = np.reshape(image, (128,128, 3))
#     return image

# print("[INFO] loading images...")
# X = []
# Y = []
# imagePaths = list(paths.list_images(dataset))
# classes =  0
# lb = LabelEncoder()

# for _, dirnames, _ in os.walk(dataset):
#     classes += len(dirnames)

# total = 0
# dem = 0
# for (i, imagePath) in enumerate(imagePaths):
#     print("[INFO] processing image {}/{}".format(i + 1,len(imagePaths)))
#     image = cv2.imread(imagePath)
#     image = pretrain(image)
#     label = imagePath.split(os.path.sep)[-2]
#     X.append(image)
#     Y.append(label)

# print("\n[INFO] serializing {} encodings...".format(total))
# # x_train = preprocessing.StandardScaler().fit(np.array(x_train, dtype='float') / 255.0)
# X = np.array(X)/255.
# Y = to_categorical(np.array(lb.fit_transform(Y)))

# (trainX, testX, trainY, testY) = train_test_split(X, Y, test_size=0.2, random_state=42)
 
# # now, let's take 10% of the training data and use that for validation
# (trainX, valX, trainY, valY) = train_test_split(trainX, trainY, test_size=0.1, random_state=84)
 
# # show the sizes of each data split
# print("training data points: {}".format(len(trainY)))
# print("validation data points: {}".format(len(valY)))
# print("testing data points: {}".format(len(testY)))

# # initialize the values of k for our k-Nearest Neighbor classifier along with the
# # list of accuracies for each value of k
# kVals = range(1, 30, 2)
# accuracies = []
 
# # loop over various values of `k` for the k-Nearest Neighbor classifier
# for k in range(1, 30, 2):
# 	# train the k-Nearest Neighbor classifier with the current value of `k`
# 	# model = KNeighborsClassifier(n_neighbors=k)
#     model = KNN(k)
#     model.fit(trainX, trainY)
 
#     # evaluate the model and update the accuracies list
#     score = model.score(valX, valY)
#     print("k=%d, accuracy=%.2f%%" % (k, score * 100))
#     accuracies.append(score)
    
# # find the value of k that has the largest accuracy
# i = int(np.argmax(accuracies))
# print("k=%d achieved highest accuracy of %.2f%% on validation data" % (kVals[i],
#     accuracies[i] * 100))

# # re-train our classifier using the best k value and predict the labels of the
# # test data
# # model = KNeighborsClassifier(n_neighbors=kVals[i])
# model = KNN(kVals[i])
# model.fit(trainX, trainY)
# predictions = model.predict(testX)

# # show a final classification report demonstrating the accuracy of the classifier
# # for each of the digits
# print("EVALUATION ON TESTING DATA")
# print(classification_report(lb.inverse_transform(testY), predictions))


from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
import os

def image_to_feature_vector(image, size=(32, 32)):
	# resize the image to a fixed size, then flatten the image into
	# a list of raw pixel intensities
	return cv2.resize(image, size).flatten()

def extract_color_histogram(image, bins=(8, 8, 8)):
	# extract a 3D color histogram from the HSV color space using
	# the supplied number of `bins` per channel
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	hist = cv2.calcHist([hsv], [0, 1, 2], None, bins,
		[0, 180, 0, 256, 0, 256])
	# handle normalizing the histogram if we are using OpenCV 2.4.X
	if imutils.is_cv2():
		hist = cv2.normalize(hist)
	# otherwise, perform "in place" normalization in OpenCV 3 (I
	# personally hate the way this is done
	else:
		cv2.normalize(hist, hist)
	# return the flattened histogram as the feature vector
	return hist.flatten()

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
	help="path to input dataset")
ap.add_argument("-k", "--neighbors", type=int, default=1,
	help="# of nearest neighbors for classification")
ap.add_argument("-j", "--jobs", type=int, default=-1,
	help="# of jobs for k-NN distance (-1 uses all available cores)")
args = vars(ap.parse_args())

# grab the list of images that we'll be describing
print("[INFO] describing images...")
imagePaths = list(paths.list_images(args["dataset"]))
# initialize the raw pixel intensities matrix, the features matrix,
# and labels list
rawImages = []
features = []
labels = []

# loop over the input images
for (i, imagePath) in enumerate(imagePaths):
	# load the image and extract the class label (assuming that our
	# path as the format: /path/to/dataset/{class}.{image_num}.jpg
	image = cv2.imread(imagePath)
	label = imagePath.split(os.path.sep)[-1].split(".")[0]
	# extract raw pixel intensity "features", followed by a color
	# histogram to characterize the color distribution of the pixels
	# in the image
	pixels = image_to_feature_vector(image)
	hist = extract_color_histogram(image)
	# update the raw images, features, and labels matricies,
	# respectively
	rawImages.append(pixels)
	features.append(hist)
	labels.append(label)
	# show an update every 1,000 images
	if i > 0 and i % 1000 == 0:
		print("[INFO] processed {}/{}".format(i, len(imagePaths)))

# show some information on the memory consumed by the raw images
# matrix and features matrix
rawImages = np.array(rawImages)
features = np.array(features)
labels = np.array(labels)
print("[INFO] pixels matrix: {:.2f}MB".format(
	rawImages.nbytes / (1024 * 1000.0)))
print("[INFO] features matrix: {:.2f}MB".format(
	features.nbytes / (1024 * 1000.0)))

# partition the data into training and testing splits, using 75%
# of the data for training and the remaining 25% for testing
(trainRI, testRI, trainRL, testRL) = train_test_split(
	rawImages, labels, test_size=0.25, random_state=42)
(trainFeat, testFeat, trainLabels, testLabels) = train_test_split(
	features, labels, test_size=0.25, random_state=42)

# train and evaluate a k-NN classifer on the raw pixel intensities
print("[INFO] evaluating raw pixel accuracy...")
model = KNeighborsClassifier(n_neighbors=args["neighbors"],
	n_jobs=args["jobs"])
model.fit(trainRI, trainRL)
acc = model.score(testRI, testRL)
print("[INFO] raw pixel accuracy: {:.2f}%".format(acc * 100))

# train and evaluate a k-NN classifer on the histogram
# representations
print("[INFO] evaluating histogram accuracy...")
model = KNeighborsClassifier(n_neighbors=args["neighbors"],
	n_jobs=args["jobs"])
model.fit(trainFeat, trainLabels)
acc = model.score(testFeat, testLabels)
print("[INFO] histogram accuracy: {:.2f}%".format(acc * 100))

