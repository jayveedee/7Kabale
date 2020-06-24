# 7-Kabal (Solitaire / Klondike)

This program is used to play Top-Down solitaire game by using Computer Vision & Machine Learning

## Getting Started

If you want to start playing a game og Klondike on your own PC, there are a couple of prerequisites that need to be installed and ready to use before you go any further. The instructions listed below should work with Windows, though with Linux and Mac tweaking may be required.

### Prerequisites

First of all, you need a CUDA compatible GPU and the drivers that are compatible with TensorFlow 1.15.2

[Check CUDA compatibility](https://developer.nvidia.com/cuda-gpus)

[Get CUDA driver](https://developer.nvidia.com/cuda-toolkit-archive)

[Get cuDNN](https://developer.nvidia.com/rdp/cudnn-archive)

Once you've got CUDA all setup, you also need to download 3 files that are used to run the inference, which are the weight files.

[Download trained_weights_final.h5](https://drive.google.com/file/d/1XWYXZuZDu36aqsacIaJ7t28o4202fuCC/view?usp=sharing)

[Download yolo.h5](https://drive.google.com/file/d/13kQJDb11mOii8x5oPDFkPxJ2-mp75UpV/view?usp=sharing)

[Download yolo3.weights](https://drive.google.com/file/d/1Lj3IMwXmizpZbCaerbJeOF2YXEmHXsgq/view?usp=sharing)

Move trained_weights_final.h5 to the directory:
```
7-Kabal\Model_Weights
```
Move yolo.h5 & yolo3.weights to the directory
```
7-Kabal\src\keras_yolo3
```

Lastly, you need a virtual environment to install all the required packages in the next step. One of which is Anaconda.

[Anaconda Python 3.7](https://www.anaconda.com/products/individual)

To setup the environment recommended in this project, all you need to do is create a environment with the python version 3.7
In the terminal:
```
conda create -n 7-kabal python=3.7.0
```

### Installing

After downloading and installing/setting up all the prerequisites, all that's left is to install all the required packages inside of the virutal environment.


Firstly get into the main directory of the project

```
cd C:\path\to\directory\7-Kabal
```

Install packages

```
pip install -r requirements.txt
```

To see if everything worked as it should, change directory to the inference folder

```
cd Inference
```

Run the Detector_Mod.py program

```
python Detector_Mod.py
```

If everything works as it should, the terminal should be initializing tensorflow and all of the required classes without fail.

## Authors

* **Asama Hayder** - *CV & ML* - [asamahayder](https://github.com/asamahayder)
* **Christoffer A. Detlef** - *Project Manaegment* - [ChrisMizz](https://github.com/ChrisMizz)
* **Jákup V. Dam** - *Logic* - [jayveedee](https://github.com/jayveedee)
* **Simon Andersen** - *Project Manaegment* - [ThaDuyx](https://github.com/ThaDuyx)
* **Thaer Mhd. R. Almalla** - *Project Manaegment* - [Thaer91](https://github.com/Thaer91)

## Acknowledgments

* [qqwwee's keras implementation of YOLOv3](https://github.com/qqwweee/keras-yolo3)
* [geaxgx's playing card generation implementation](https://github.com/geaxgx/playing-card-detection)
