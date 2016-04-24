# Explorations

This folder contains work-in-progress explorations of different models.

## Contents

### CNN

CNN is based on Lasagne + Theano + NoLearn. It is tricky running the environment with these packages as they've had conflicting versions recently. 

Safest option to run is as below:

* Continue to build conda as on main page (fkd)
* Install specifc combination of the packages as below:
	* ```pip install -r https://raw.githubusercontent.com/dnouri/kfkd-tutorial/master/requirements.txt```
* Launch jupyter notebook as below because of conflicts with MKL on OSX:
	* ```THEANO_FLAGS='blas.ldflags=' jupyter notebook```

