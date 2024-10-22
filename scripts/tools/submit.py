__project__ = 'fkd'

##  SUBMISSION - TOOLS module
#     April, 2016
#  The following module contains tools for the Kaggle submission of
#   already trained set of facial keypoint detector models.
##

## Contents:
#	- create_submission
#	- generate_csv
##


import numpy as np
import pandas as pd
import time

# Feature ID lookup table
ID_LOOKUP = pd.read_csv('../../data/submissions/IdLookupTable.csv')


def create_submission(test, models, label='baseline', verbose=False):
    ''' Predict and generate submission file 
    Inputs: 
        test - test dataset on which to predict
        models - list of tuples: [ (feature, model), ... ]
        label - label for identification of the submission file
        verbose - print informative status updates
    
    Usage: >> create_submission( <test_data>, <list_of_models> [, <label> ] )
    '''
    
    predicted_df = pd.DataFrame()
    
    # get predictions on test dataset
    for (f, mod) in models:  # 'models' is a list of tuples ('facial_feature', model)
        
        if verbose:
            print 'Predicting "{}"...'.format(f),
        
        _start = time.time()  # start timer
        predicted_df[f] = mod.predict(test.tolist())
        _elapsed = time.time() - _start
        
        if verbose:
            print 'done! ({:.1f}s)'.format(_elapsed)
        
    return predicted_df



def generate_csv(df, label):
    ''' Generate csv file with the submission format
    Inputs:
        df - dataframe with predictions
        label - label to identify the submission file
    
    Usage: >> generate_csv(<data_frame_with_predictions>, <label>)
    '''

    # Get full flat frame, (unpivot data)
    df['ImageId'] = np.arange(1,len(df)+1)
    out = pd.melt(df.reset_index(), id_vars=['index','ImageId'])
    out.columns = ['index', 'ImageId', 'FeatureName', 'Location']

    # Merge with SampleSubmission
    final = pd.merge(ID_LOOKUP[['RowId', 'ImageId', 'FeatureName']],
                     out[['ImageId', 'FeatureName', 'Location']],
                     on=['ImageId', 'FeatureName'], how='left')
    
    # Export only RowId and Location columns
    sumission = final[['RowId', 'Location']]
    with open('../../data/submissions/{}_submission.csv'.format(label), 'wb') as f:
        sumission.to_csv(f, index=False)
    
    print '\n... Created the csv file: ../../data/submissions/{}_submission.csv'.format(label)



def create_generate(test, models, label='baseline', verbose=False):
    ''' Predicts using models and generates the csv file for submission.
    Wrapper for create_submission and generate_csv.
    Inputs: 
        test - test dataset on which to predict
        models - list of tuples: [ (feature, model), ... ]
        label - label for identification of the submission file
        verbose - print informative status updates

    Usage: >> create_generate( <test_data>, <list_of_models> [, <label> ] )
    '''

    # predict
    predicted_df = create_submission(test, models, label, verbose)
    
    # create the csv file
    generate_csv(predicted_df, label)


def create_generate_NN(predictions, columns, label='NN_base'):
    ''' Generates the csv file for submission for the predictions of a NN models
    Inputs: 
        predictions - predicted test values
        columns - the feature names (use FEATURES as loaded from getdata)
        label - label for identification of the submission file

    Usage: >> create_generate_NN( <y_pred>, FEATURES , <label> ] )
    '''
    predicted_df = pd.DataFrame(predictions, columns=columns)
    generate_csv(predicted_df, label)

