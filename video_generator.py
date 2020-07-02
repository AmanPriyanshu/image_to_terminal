import os
import numpy as np
import time

os.system('clear')
print('Loading Everything...')
time.sleep(2)
path = './reformed/txt/'
images = os.listdir(path)
for image in images:
	image_new = image[len('image'):-4]
	image_new = ''.join(['0' for k in range(len(str(len(images)))-len(str(image_new)))])+str(image_new)
	#print(image_new)
	os.system('mv '+path+image+' '+path+'image'+image_new+'.txt')

images = os.listdir(path)
images.sort()
frameRate = 0.09
os.system('clear')
os.system('setsid play ./video/audio.mp3 &>/dev/null')
for txt in images:
	os.system('clear')
	file = open(path+txt, 'r')
	data = file.readlines()
	data = [i[:-1] for i in data]
	for i in data:
		print(i)
	time.sleep(frameRate)