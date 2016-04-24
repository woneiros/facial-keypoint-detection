__project__ = 'fkd'

##  STORAGE AND RETRIEVAL TOOLS module
#     April, 2016
#  The following module contains tools for the storing and loading 
#   models and preprocessed datasets (preprod's).
##

## Contents:
#   - list_preprod
#	- save_preprod
#	- load_preprod
#
#   - list_models
#	- save_model
#	- load_model
##

import os
import cPickle as pk

PATH_MODELS = '../../data/models/'
PATH_PREPRODS = '../../data/preprocessed/'

ENTRY = "  + {lb} : {ds}"


def list_preprods():
	''' Lists the stored preprocessed datasets '''
	with open(PATH_PREPRODS + 'index.pk', 'rb') as f:
		index = pk.load(f)

	print "\n    PREPROC\'D DATASETS\n    ===================\n Total: {}\n".format(len(index))

	for k,_v in index.iteritems():
		print ENTRY.format(lb=k, ds=_v)


def save_preprod(preprod, label, description=None, overwrite=False):
	''' Saves a specific preprocessed dataset with a given label and description '''
	# add extension if necessary
	if label[-2:] != ".pk":
		label += ".pk"

	if os.path.isfile(PATH_PREPRODS + label) and not overwrite:
		print 'WARNING - file exists. For overwriting specify overwrite=True'
		return

	else:
		if description is None:
			description = label
			print 'Description not specified. It is not necessary but recommended.'
			print 'If you want to add a description, save again with description and overwrite=True'

		# Save preprod
		with open(PATH_PREPRODS + label, 'wb') as f:
			index = pk.dump(preprod, f)

		# Update index
		with open(PATH_PREPRODS + 'index.pk', 'rb') as f:
			index = pk.load(f)
		
		index[label] = description

		with open(PATH_PREPRODS + 'index.pk', 'wb') as f:
			index = pk.dump(index, f)


def load_preprod(label):
	''' Loads the preprocessed dataset specified (extension is optional) '''
	# add extension if necessary
	if label[-2:] != ".pk":
		label += ".pk"

	try:  # check if available
		with open(PATH_PREPRODS + label, 'rb') as f:
			preprod = pk.load(f)

	except:  # warn if not found
		print "No such preprod found (use list_preprod() for a list of all available)"

	else:
		print 'Loaded', label[-2:]
		return preprod



## Analogous for Models

def list_models():
	''' Lists the stored models '''
	with open(PATH_MODELS + 'index.pk', 'rb') as f:
		index = pk.load(f)

	print "\n    STORED MODELS\n    =============\n Total: {}\n".format(len(index))

	for k,_v in index.iteritems():
		print ENTRY.format(lb=k, ds=_v)


def save_model(model, label, description=None, overwrite=False):
	''' Saves a specific model with a given label and description '''
	# add extension if necessary
	if label[-2:] != ".pk":
		label += ".pk"

	if os.path.isfile(PATH_MODELS + label) and not overwrite:
		print 'WARNING - file exists. For overwriting specify overwrite=True'
		return

	else:
		if description is None:
			description = label
			print 'Description not specified. It is not necessary but recommended.'
			print 'If you want to add a description, save again with description and overwrite=True'

		# Save model
		with open(PATH_MODELS + label, 'wb') as f:
			index = pk.dump(model, f)

		# Update index
		with open(PATH_MODELS + 'index.pk', 'rb') as f:
			index = pk.load(f)
		
		index[label] = description

		with open(PATH_MODELS + 'index.pk', 'wb') as f:
			index = pk.dump(index, f)



def load_model(label):
	''' Loads the model specified (extension is optional) '''
	# add extension if necessary
	if label[-2:] != ".pk":
		label += ".pk"

	try:  # check if available
		with open(PATH_MODELS + label, 'rb') as f:
			model = pk.load(f)

	except:  # warn if not found
		print "No such model found (use list_models() for a list of all available)"

	else:
		print 'Loaded', label[-2:]
		return model


