import cv2
import numpy as np
import os
from sklearn.cluster import KMeans
import string

def image_names(path):
	all_images = os.listdir(path)
	return all_images

def image_reader(path, images, n_clusters=len('.*"/#$%'), symbols='.*"/#$%', H=45, W=100):
	H, W = W, H
	document = []
	for img in images:
		name = img
		image = cv2.imread(path+img)
		image = cv2.resize(image, (H, W))
		image = image/255
		image_new = []
		for row in image:
			for col in row:
				image_new.append(col)
		image_new = np.array(image_new)
		kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(image_new)
		labels = kmeans.labels_
		new_image = []
		for row in range(W):
			img = []
			for col in range(H):
				img.append(labels[H*row+col])
			new_image.append(img)
		new_image = np.array(new_image)
		reformed_data = []
		file = open('./reformed/txt/'+name[:name.index('.')+1]+'txt', 'a')
		for row in new_image:
			column = []
			for col in row:
				column .append(symbols[col])
			print(''.join(column))
			file.write(''.join(column)+'\n')
			reformed_data.append(column)
		print()
		file.close()
		
path = './images/'
symbols = input("Enter Symbols you wish to use:\t")
H = int(input('Enter Height:\t'))
W = int(input('Enter Width:\t'))
if len(symbols) == 0:
	symbols = string.punctuation
n_clusters = len(symbols)
images = image_names(path)
image_reader(path, images, n_clusters, symbols, H, W)
#image_reader(path, images)