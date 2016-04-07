__project__ = 'fkd'

##  SUBMITION TOOLS module
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


def create_submission(test, models, label='baseline', verbose=False):
    ''' Predict and generate submission file 
    Inputs: 
        test - test dataset on which to predict
        models - list of tuples: [ (feature, model), ... ]
        label - label for identification of the submission file
    
    Usage: >> create_submission( <test_data>, <list_of_models> [, <label> ] )
    '''
    
    predicted_df = pd.DataFrame()
    
    # get predictions on test dataset
    for (f, mod) in models:  # 'models' is a list of tuples ('facial_feature', model)
        
        if verbose:
            print 'Predicting "{}"...'.format(f),
        
        _start = time.time()  # start timer
        predicted_df[f] = mod.predict(test.iloc[:,0].tolist())
        _elapsed = time.time() - _start
        
        if verbose:
            print 'done! ({:.1f}s)'.format(_elapsed)
    
    # create the csv file
    generate_csv(predicted_df, label)
    
    return predicted_df



def generate_csv(df, label):
    ''' Generate csv file with the submission format
    Inputs:
        df - dataframe with predictions
        label - label to identify the submission file
    
    Usage: >> generate_csv(<data_frame_with_predictions>, <label>)
    '''
    
    # Get full flat frame
    out = pd.DataFrame()
    out['Location'] = df.values.flatten()
    out['RowId'] = np.arange(1,len(out)+1)
    out = out[['RowId','Location']]
    
    # Unpivot data, filter with SampleSubmission
    unpivot = pd.melt(kn_predictions.reset_index(), id_vars='index')
    unpivot.columns = ['ImageId', 'FeatureName', 'Location']
    scored_sub = pd.merge(id_t[['RowId', 'ImageId', 'FeatureName']], unpivot,
                          on=['ImageId', 'FeatureName'], how='left')
        
    # Export only RowId and Location columns
    final = scored_sub[['RowId','Location']]
    with open('data/{}_submission.csv'.format(label), 'wb') as f:
        final.to_csv(f, index=False)
    
    print '... Created the csv file: data/{}_submission.csv'.format(label)

