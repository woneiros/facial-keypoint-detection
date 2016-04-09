__project__ = 'fkd'

##  DATA LOADER - TOOLS module
#     April, 2016
#  The following module contains tools for the loading and preprocessing
#   the datasets of the Kaggle facial keypoint detector models.
##

## Contents:
#	- load_data
##

import pandas as pd
import numpy as np

PATH_TRAINING = '../../data/datasets/training.csv'
PATH_TEST = '../../data/datasets/test.csv'


def get_img(x):
	''' Preprocess images into unsigned 8byte integer arrays

	Usage: >> get_img(<string containing space-separated ints>)
	'''
	return np.uint8( map(int, x.split()) )


def load_data(dev, test=False, nonas=True):
	''' Loads the datasets (test as well, if specified), preprocess images
		unsigned 8byte integers
    Inputs: 
        dev - if 0<dev<1 percentage of datapoints assigned to dev (vs train)
              if dev > 1 number of observations assigned to dev
              if dev < 0 number of observations assigned to training (the rest for dev)
        test - boolean, return test data
        nonas - filter NA observations from dataset (removes whole row with any NA)
        verbose - print informative status updates

    Outputs: { 'training': {'data': <ndarray>, 'labels': <ndarray> }, ... }

	Usage: >> load_data(<dev-size>, test=False, nonas=True)
	'''

	out_dict = {}

	# Load data and preprocess images
	full_data = pd.read_csv(PATH_TRAINING)
	full_data['img_processed'] = map( get_img, full_data['Image'])

	# Filter na's if specified
	if nonas:
		full_data = full_data.dropna()

	# Add feature names
	out_dict['features'] = full_data.columns[:-2] #remove Image and img_processed

	# TRAINING + DEV DATA
	if dev >= 0 and dev <1:
		# specified % of obs for dev set
		_split = full_data.shape[0] * (1 - dev) 

	else:
		# specified obs for training set or dev set
		_split = -1 * dev

	train_data = full_data.iloc[:_split, 31].values
	train_labels = np.round(full_data.iloc[:_split, :30].values)
	out_dict['training'] = {'data': train_data, 'labels': train_labels}

	if dev != 0:
		dev_data = full_data.iloc[_split:, 31].values
		dev_labels = np.round(full_data.iloc[_split:, :30].values)
		out_dict['dev'] = {'data': dev_data, 'labels': dev_labels}

	# TEST DATA
	if test:
		# Load data and preprocess images
		full_test = pd.read_csv(PATH_TEST)
		full_test['img_processed'] = map( get_img, full_test['Image'])

		# Get training data
		test_data = full_test[['img_processed']].values
		out_dict['test'] = {'data': test_data}

	return out_dict


