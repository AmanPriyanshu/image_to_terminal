import cv2
import numpy as np
import pandas as pd
import os

def image_names(path):
	all_images = os.listdir(path)
	return all_images

def image_reader(path, images):
	for img in images:
		image = cv2.imread(path+img)
		image = np.reshape(image, (image.shape[]))


path = './images/'
images = image_names(path)