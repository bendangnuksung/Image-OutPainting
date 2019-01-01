import numpy as np
import os
import cv2
import random
from augment_image import aug_image

# raw_data_path: directory where the downloaded images are
# save_path: directory where the numpy images will be
raw_data_path = "data/raw_data/beach_image"
train_save_path = "data/prepared_data/train"
test_save_path = "data/prepared_data/test"

# Train/Test Data split
train_percen = 0.9

files = os.listdir(raw_data_path)
random.shuffle(files)
train_files = files[: int(len(files) * train_percen)]
test_files = files[int(len(files) * train_percen) + 1:]


total_train_images = 0
total_test_images = 0

# Augment both train and test dataset by N times
augment_times = 2

input_shape = (256, 256)

# batch: each file will have N images
batch = 2000

# Dumping numpy batch images to save_path
train_dump_counter = 0
test_dump_counter = 0
def dump_numpy(data, is_train_data=True):
	global train_dump_counter, test_dump_counter
	random.shuffle(data)
	if is_train_data:
		train_dump_counter += 1
		path = os.path.join(train_save_path, 'train_data_' + str(train_dump_counter))
	else:
		test_dump_counter += 1
		path = os.path.join(test_save_path, 'test_data_' + str(test_dump_counter))
	np.save(path, data)


def create_data(files_path, is_train_data=True, augment_times=augment_times):
	global total_test_images, total_train_images
	bulk = []
	image_counter = 0
	for i, file in enumerate(files_path, 1):
		image_path = os.path.join(raw_data_path, file)
		try:
			image = cv2.imread(image_path)
			image = cv2.resize(image, input_shape)
			bulk.append(image)
			image_counter += 1
			for _ in range(augment_times):
				new_image = aug_image(image)
				image_counter += 1
				bulk.append(new_image)
		except Exception as e:
			print("error: ", e)
			print("file name: ", image_path)

		print("Proccessed: ", image_counter)

		if len(bulk) >= batch or i == len(files_path):
			print("Dumping batch: ", len(bulk))
			dump_numpy(bulk, is_train_data=is_train_data)
			bulk = []

	if is_train_data:
		total_train_images += image_counter
	else:
		total_test_images += image_counter

# Create Train Dataset
print("CREATING TRAIN DATASET")
create_data(train_files, is_train_data=True)

# CREATE TEST DATASET
print("CREATING TEST DATASET")
create_data(test_files, is_train_data=False)

print("*"*50)
print("Data preparation completed")
print("*"*50)
print("Total train images: ", total_train_images)
print("Total test images: ", total_test_images)