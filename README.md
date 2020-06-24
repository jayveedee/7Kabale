<p align="center">
  <img src="https://i.imgur.com/0J3QMlC.png">
</p>

# 7-Kabal (Solitaire / Klondike)

7-kabal is used to play a game of Top-Down solitaire with the use of Computer Vision & Machine Learning

## Getting Started

If you want to run the project on your own PC, there are a couple of prerequisites that 
are required before you go any further. 

The instructions listed below should work with Windows, though with Linux and Mac some tweaking may be required.

### Prerequisites

First of all, you need a CUDA compatible GPU, the CUDA driver & cuDNN library which is compatible with TensorFlow 1.15.2

[Check CUDA compatibility](https://developer.nvidia.com/cuda-gpus)

[Get CUDA driver](https://developer.nvidia.com/cuda-toolkit-archive)

[Get cuDNN](https://developer.nvidia.com/rdp/cudnn-archive)

Once you've got CUDA all setup, you also need to download 3 files that are used to run the inference & training.

[Download trained_weights_final.h5](https://drive.google.com/file/d/1XWYXZuZDu36aqsacIaJ7t28o4202fuCC/view?usp=sharing)

[Download yolo.h5](https://drive.google.com/file/d/13kQJDb11mOii8x5oPDFkPxJ2-mp75UpV/view?usp=sharing)

[Download yolo3.weights](https://drive.google.com/file/d/1Lj3IMwXmizpZbCaerbJeOF2YXEmHXsgq/view?usp=sharing)

From the main directory move trained_weights_final.h5 to the Model_Weights folder
```
7-Kabal\Model_Weights
```
From the main directory move yolo.h5 & yolo3.weights to the keras_yolo3 folder
```
7-Kabal\src\keras_yolo3
```

Lastly, you need a virtual environment to install all the required packages in the next step. One of which is Anaconda, that works well with this project.

[Anaconda Python 3.7](https://www.anaconda.com/products/individual)

Afterwards create a environment with the python version 3.7 which is the recommended python version for this project. Using the 
 terminal write:
```
conda create -n 7-kabal python=3.7.0
```

### Installing

After setting up all the prerequisites, all that's left is to install the required packages inside of the virtual environment.

Firstly move into the main directory of the project

```
cd C:\path\to\directory\7-Kabal
```

Install packages

```
pip install -r requirements.txt
```

To check if everything worked as intended, change directory to the inference folder

```
cd Inference
```

Run the Detector_Mod.py program

```
python Detector_Mod.py
```

If no errors appear, the project will have been successfully implemented.

## Authors

* **Asama Hayder** - *CV & ML* - [asamahayder](https://github.com/asamahayder)
* **Christoffer A. Detlef** - *Project Manaegment* - [ChrisMizz](https://github.com/ChrisMizz)
* **Jákup V. Dam** - *Logic* - [jayveedee](https://github.com/jayveedee)
* **Simon Andersen** - *Project Manaegment* - [ThaDuyx](https://github.com/ThaDuyx)
* **Thaer Mhd. R. Almalla** - *Project Manaegment* - [Thaer91](https://github.com/Thaer91)

## Acknowledgments

* [qqwwee's keras implementation of YOLOv3](https://github.com/qqwweee/keras-yolo3)
* [geaxgx's playing card generation implementation](https://github.com/geaxgx/playing-card-detection)
