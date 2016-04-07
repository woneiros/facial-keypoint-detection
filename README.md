# Facial Keypoint Detection

**Explorations on facial image keypoint detection.**  

**Contact: [Will](https://github.com/WillahScott)**

This project contains the explorations on face feature detection (for the [Kaggle competition](https://www.kaggle.com/c/facial-keypoints-detection)), as part of the final project for the 207-Machine Learning course for [Berkeley's Master in Information and Data Science](https://datascience.berkeley.edu/).  

The project was developed by: Alex, Ankit, Annalaissa, Nina and Will.  


## Contents  

* **`scripts/`**

	* **`explorations/`** contains dataset explorations, plots and initial modeling attempts  

	* **`modelers/`** contains all serious modeling attempts, including the generation of their submission files

	* **`tools/`** contains a set of additional tools that make the exploration and modeling cleaner. For example `submit.py` contains functions for creating the submission files in the appropriate folder.    

* **`data/`**

	**`datasets/`** contains the original kaggle data

	**`submissions/`** contains the csv files submitted to the Kaggle competition

	**`models/`** contains the persistent storages of the models created. Each pickled model contains: name, alias, description, model-object, prediction-df, <training-time>, <predicting-time>


## Pre-requisites

First of all clone the repo's folder:

```bash
$ git clone https://github.com/WillahScott/facial-keypoint-detection.git
```

Use of a **virtual environment** is highly recommended (specially through [*conda*](http://conda.pydata.org/docs/using/envs.html)).  

*Should you choose to not create a virtualenv and just install directly on your raw machine just disregard instruction 1.*  


### With `conda`

Clone the environment as provided in `environment.yml`:

```bash
$ conda fkd create -f environment.yml
$ source activate fkd
```


### With `virtualenv`  

Create a virtual env (from within the folder) and activate it:

```bash
$ cd facial-keypoint-detection
$ virtualenv fkd
$ source fkd/bin/activate
```

Install pre-reqs:

```bash
$ pip install -r requirements.txt
```
  

## Usage

*Last update: April, 2016*
