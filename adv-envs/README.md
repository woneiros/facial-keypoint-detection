# Advanced Environments

*NOTE - The following environment especification files are **not** necessary for running the basic models and some of the preprocessors*  

These environments have been created for the sole purpose of using specialized tools for specific preprocessings (or implementing cleaner, more powerful Neural Networks). They are built on top of the base environment (fkd) specified in the `environment.yml` in the root directory.  

## Contents

* `ocv` - includes [OpenCV](https://opencv-python-tutroals.readthedocs.org/en/latest/#) for advanced image preprocessing (although most algorithms have been later ported to skimage, included within the base environment).  
  
* `lnet` - adds to the the base environment specific builds of [Theano](http://deeplearning.net/software/theano/), [Lasagne](http://lasagne.readthedocs.org/en/latest/) and [nolearn](https://pythonhosted.org/nolearn/).  

## Usage

These advanced environments have only been created to ensure a conda build.

*  Clone the environment as provided in `environment.yml`:  
```bash
$ conda env create -f adv-env/environment-ocv.yml
$ source activate fkd
```

### Specific configurations for CNN

CNN is based on Lasagne + Theano + NoLearn. It is tricky running the environment with these packages as they've had conflicting versions recently. 

Safest option to run is as below:

* Continue to build conda as on main page (fkd)
* Install specifc combination of the packages as below:
	* ```pip install -r https://raw.githubusercontent.com/dnouri/kfkd-tutorial/master/requirements.txt```
* Launch jupyter notebook as below because of conflicts with MKL on OSX:
	* ```THEANO_FLAGS='blas.ldflags=' jupyter notebook```


