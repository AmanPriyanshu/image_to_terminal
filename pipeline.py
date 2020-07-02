import os
#Deleting
os.system('rm -R ./images')
os.system('rm -R ./reformed')
os.system('mkdir ./images')
os.system('mkdir ./reformed')
os.system('mkdir ./reformed/txt')

os.system('python3 video_splitter.py')
os.system('python3 image_reader.py')
os.system('python3 video_generator.py')