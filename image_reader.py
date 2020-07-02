import cv2
import numpy as np
import pandas as pd
import os
from sklearn.cluster import KMeans
import string

def image_names(path):
	all_images = os.listdir(path)
	return all_images

def image_reader(path, images, n_clusters, symbols):
	H = 45
	W = 100
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
		for row in new_image:
			column = []
			for col in row:
				column .append(symbols[col])
			print(''.join(column))
			reformed_data.append(column)
		print()
		reformed_data =  np.array(reformed_data)
		reformed_data = pd.DataFrame(reformed_data)
		reformed_data.to_csv('./reformed/'+name[:name.index('.')+1]+'csv', header=None, index=None)




path = './images/'
symbols = input("Enter Symbols you wish to use:\t")
if len(symbols) == 0:
	symbols = string.punctuation
n_clusters = len(symbols)
images = image_names(path)
image_reader(path, images, n_clusters, symbols)