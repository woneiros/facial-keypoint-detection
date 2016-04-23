# Tools

This folder contains additional tools that may be imported and used for cleaner exploration and modeling.  

Some of this tools exist in a primordial state within notebooks of the first exploration-notebooks.  

## Contents

* `submit.py` - contains functions for Kaggle submission file generation  
* `getdata.py` - contains tools for the loading and preprocessing the datasets
* `save4later.py` - contains tools that implement a basic pickler for storing and retrieving (and listing the available) models and preprocessed dataset. *NOTE - use sparingly for prepocessed datasets, only for computationally intensive preprocessings*

## Importing the `tools`

Due to how imports work in iPython notebooks, the standard relative import does not work when using a Jupyter Notebook, which would be:

```python
from ..tools import submit
```

The easiest way around it is to temporarily add the path to the `scripts/` subfolder to our `python path` (the set of locations in which python will look to import packages). Basically:  

```python
import sys
sys.path.append('/Users/will/Github/facial-keypoint-detection/scripts')

# Import modules from our tools subfolder
from tools import submit, getdata, save4later
```


## Tool usage

#### `getdata`

Previous imports necesary:

```python
import numpy as np
import pandas as pd
```

Usage:

```python
# Load data (no dev)
_loaded = getdata.load_data(0, test=True, nonas=True)

FEATURES = _loaded['features']
print 'Number of features:', len(FEATURES)

train_data = _loaded['training']['data']
train_labels = _loaded['training']['labels']
print 'Training dataset size: ', train_data.shape

test_data = _loaded['test']['data']
print 'Test dataset size: ', test_data.shape
```




#### `save4later`

##### Models

Previous imports necesary:
**Important all the necessary sklearn classes must be imported prior to loading a model, if not it will fail to load**

```python
import numpy as np
import pandas as pd

from sklearn.neighbors import KNeighborsRegressor
```

Usage:

```python
knreg = KNeighborsRegressor()
knreg.fit(train_data.tolist(), train_labels[:,0])

save4later.save_model(knreg, 'KNRegressor', 'K-nearest neighbors regressor with no preprocessing')
```

*Take a break*

```python
import numpy as np
import pandas as pd

from sklearn.neighbors import KNeighborsRegressor

model = save4later.load_model('KNRegressor')
```

And you are set to go.  


##### Preprocessed data

The same applies, but this time we just need numpy and pandas for previous imports:

```python
import numpy as np
import pandas as pd

# Load and do a lot of heavy preprocessing
save4later.save_preprod(preprocessed_data, 'Blur-Hough', 'Gaussian blur + Hough transform')
```

*Take a break*

```python
import numpy as np
import pandas as pd

shiny_data = save4later.load_model('Blur-Hough')
```

And you are set to go.  



#### `submit`

Previous imports necesary:

```python
import numpy as np
import pandas as pd
```

Usage:

```python

models =  [ (FEATURES[0], knn), (FEATURES[1], gmm2) ]  # concatenate tuples of feature name and model

submit.create_generate(test_data, models, 'tools_example', verbose=True)
```


