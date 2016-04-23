# Facial Keypoint Detection

**Explorations on facial image keypoint detection.**  

**Contact: [Will](https://github.com/WillahScott)**

This project contains the explorations on face feature detection (for the [Kaggle competition](https://www.kaggle.com/c/facial-keypoints-detection)), as part of the final project for the 207-Machine Learning course for [Berkeley's Master in Information and Data Science](https://datascience.berkeley.edu/).  

The project was developed by: [Alex](https://github.com/keivahn), [Ankit](https://github.com/ankittharwani), [Nina](https://github.com/kuknina) and [Will](https://github.com/willahscott).  


## Presentation
We created a [prezi](https://prezi.com/an_apyqfaeaj/recognizing-key-facial-points/#) to showcase our ideas and explorations:

<iframe id="iframe_container" frameborder="0" webkitallowfullscreen="" mozallowfullscreen="" allowfullscreen="" width="550" height="400" src="https://prezi.com/embed/an_apyqfaeaj/?bgcolor=ffffff&amp;lock_to_path=1&amp;autoplay=0&amp;autohide_ctrls=0&amp;landing_data=bHVZZmNaNDBIWnNjdEVENDRhZDFNZGNIUE43MHdLNWpsdFJLb2ZHanI0U2p0UGtZb3daSFJVdjJCK0N2VDJ4TlZRPT0&amp;landing_sign=3XNOqv7OkiStnhLHqFa5OhvNR_NB9wftasVDFuY3Csg"></iframe> 


## Contents  

* **`scripts/`**  

	* **`explorations/`** contains dataset explorations, plots and initial modeling attempts  

	* **`modelers/`** contains all serious modeling attempts, including the generation of their submission files

	* **`tools/`** contains a set of additional tools that make the exploration and modeling cleaner. For example `submit.py` contains functions for creating the submission files in the appropriate folder  

* **`data/`**  

	* **`datasets/`** contains the original kaggle data  

	* **`submissions/`** contains the csv files submitted to the Kaggle competition  

	* **`models/`** contains the persistent storages of the models created. Each pickled model contains: name, alias, description, model-object, prediction-df, [training-time], [predicting-time]  

	* **`preprocessed/`** contains preprocessed datasets. For *temporal* time-consuming preprocessings   
  

## Pre-requisites

* First of all clone the repo's folder:

```bash
$ git clone https://github.com/WillahScott/facial-keypoint-detection.git
```

Use of a **virtual environment** is highly recommended (specially through [*conda*](http://conda.pydata.org/docs/using/envs.html)).  

*Should you choose to not create a virtualenv and just install directly on your raw machine just install the prereqs (follow step 2 for virtualenv instructions)*  


### With `conda`

*  Clone the environment as provided in `environment.yml`:  
```bash
$ conda env create -f environment.yml
$ source activate fkd
```
That's it!  
*For more info on using virtual environments with conda see [here](http://conda.pydata.org/docs/using/envs.html)*

### With `virtualenv`  

* Create a virtual env (from within the folder) and activate it:  
```bash
$ cd facial-keypoint-detection
$ virtualenv fkd
$ source fkd/bin/activate
```  
* Install pre-reqs:
```bash
$ pip install -r requirements.txt
```
  

## Usage

*Last update: April, 2016*
