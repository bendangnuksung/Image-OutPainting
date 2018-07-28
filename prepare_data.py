import numpy as np
import os
import cv2

# raw_data_path: directory where the downloaded images are
# save_path: directory where the numpy images will be
raw_data_path = "data/raw_data/coast"
save_path = "data/prepared_data/"

files = os.listdir(raw_data_path)
input_shape = (256, 256)

# batch: each file will have N images
batch = 1000


# Dumping numpy batch images to save_path
counter = 1
def dumpy_numpy(data):
	global counter
	file_path = os.path.join(save_path, str(counter))
	np.save(file_path, data)
	counter += 1


# Converting to numpy files
bulk = []
if not len(files):
	print("No images in: ", raw_data_path)
for i, file in enumerate(files, 1):
	try:
		image_path = os.path.join(raw_data_path, file)
		image = cv2.imread(image_path)
		image = cv2.resize(image, input_shape)
		bulk.append(image)
	except Exception as e:
		print("error: ", e)
		print("file name: ", image_path)

	print("Proccessed: %s / %s image" %(i, len(files)))

	if len(bulk) >= batch or i == len(files):
		print("Dumping batch: ", len(bulk))
		dumpy_numpy(bulk)
		bulk = []