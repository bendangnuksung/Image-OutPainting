import numpy as np
import os
from random import shuffle


DATA_PATH = "data/prepared_data/train"
TEST_PATH = "data/prepared_data/test"


class Data():

	def __init__(self):
		self.X_counter = 0
		self.file_counter = 0
		self.files = os.listdir(DATA_PATH)
		self.files = [file for file in self.files if '.npy' in file]
		shuffle(self.files)
		self._load_data()

	def _load_data(self):
		datas = np.load(os.path.join(DATA_PATH, self.files[self.file_counter]))
		self.X = []
		for data in datas:
			self.X.append(data)
		shuffle(self.X)
		self.X = np.asarray(self.X)
		self.file_counter += 1

	def get_data(self, batch_size):
		if self.X_counter >= len(self.X):
			if self.file_counter > len(self.files) - 1:
				print("Data exhausted, Re Initialize")
				self.__init__()
				return None
			else:
				self._load_data()
				self.X_counter = 0

		if self.X_counter + batch_size <= len(self.X):
			remaining = len(self.X) - (self.X_counter)
			X = self.X[self.X_counter: self.X_counter + batch_size]
		else:
			X = self.X[self.X_counter: ]

		self.X_counter += batch_size
		return X


class TestData():

	def __init__(self):
		self.X_counter = 0
		self.file_counter = 0
		self.files = os.listdir(TEST_PATH)
		self.files = [file for file in self.files if '.npy' in file]
		shuffle(self.files)
		self._load_data()

	def _load_data(self):
		datas = np.load(os.path.join(TEST_PATH, self.files[self.file_counter]))
		self.X = []
		for data in datas:
			self.X.append(data)
		shuffle(self.X)
		self.X = np.asarray(self.X)
		self.file_counter += 1

	def get_data(self, batch_size):
		if self.X_counter >= len(self.X):
			if self.file_counter > len(self.files) - 1:
				print("Data exhausted, Re Initialize")
				self.__init__()
				return None
			else:
				self._load_data()
				self.X_counter = 0

		if self.X_counter + batch_size <= len(self.X):
			remaining = len(self.X) - (self.X_counter)
			X = self.X[self.X_counter: self.X_counter + batch_size]
		else:
			X = self.X[self.X_counter: ]

		self.X_counter += batch_size
		return X
