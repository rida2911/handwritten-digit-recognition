## Getting Started
git clone
cd Handwritten-Digit-Recognition
pip3 install -r requirements.txt 
python3 tf_cnn.py
```
* You can also run the `load_model.py` to skip the training of NN. It will load the pre saved model from `model.json` and `model.h5` files.
```
python3 load_model.py <path/to/image_file>
```
For example
```
python3 load_model.py assets/images/1a.jpg 
```
 
## Prerequisites

- Python 3.5
- OpenCV
```
sudo apt-get install python-opencv
``` 

