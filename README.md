<p align="center">
  <img src="https://i.imgur.com/0J3QMlC.png">
</p>

# 7-Kabale (Solitaire / Klondike)

7-kabale is used to play a game of Top-Down solitaire with the use of Computer Vision & Machine Learning

## Getting Started

If you want to run the project on your own PC, there are a couple of prerequisites that 
are required before you go any further. 

The instructions listed below should work with Windows, though with Linux and Mac some tweaking may be required.

### Prerequisites

First of all, you need a CUDA compatible GPU, the CUDA driver & cuDNN library which is compatible with TensorFlow 1.15.2

[Check CUDA compatibility](https://developer.nvidia.com/cuda-gpus)

[Get CUDA driver](https://developer.nvidia.com/cuda-toolkit-archive)

[Get cuDNN](https://developer.nvidia.com/cudnn)

After installing the CUDA driver and downloaded the cuDNN library, navigate to the "NVIDIA GPU Computing Toolkit" directory usually located here

```
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0
```

And then move the following 4 files downloaded from the cuDNN library into the directory above

```
bin
include
lib
NVIDIA_SLA_cuDNN_Support.txt
```

Finally, all that's left is to add CUDA's PATH to environment variables. On Windows 10, type into the Windows search bar

```
system environment variables
```

Afterwards pressing the lower right button called "Environment Variables" and choosing the "path" variable under "User variables" and clicking edit

<p align="center">
  <img width="350px" src="https://i.imgur.com/49CUQDh.png">
  <img width="420px" src="https://i.imgur.com/qPa3Om7.png">
</p>

And inside of the path variable is where you finally define which path to specify to the CUDA directory, where you add new paths simply by clicking on new and pasting in the the path. Below you can see how it should be done if you have downloaded CUDA v10.0

<p align="center">
  <img src="https://i.imgur.com/JJMWwfQ.png">
</p>

Once you've got CUDA all setup, you also need to download 3 files that are used to run the inference & training.

[Download trained_weights_final.h5](https://drive.google.com/file/d/1XWYXZuZDu36aqsacIaJ7t28o4202fuCC/view?usp=sharing)

[Download yolo.h5](https://drive.google.com/file/d/13kQJDb11mOii8x5oPDFkPxJ2-mp75UpV/view?usp=sharing)

[Download yolo3.weights](https://drive.google.com/file/d/1Lj3IMwXmizpZbCaerbJeOF2YXEmHXsgq/view?usp=sharing)

From the main directory move trained_weights_final.h5 to the Model_Weights folder
```
7-Kabale\Model_Weights
```
From the main directory move yolo.h5 & yolo3.weights to the keras_yolo3 folder
```
7-Kabale\src\keras_yolo3
```

To detect cards, you need a webcam, but in this project DroidCam was implemented instead, so that a phone could be used as a substitute webcam. To be able to use DroidCam, download the client on your PC and app on your phone.

[DroidCam](https://www.dev47apps.com/)

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
cd C:\path\to\directory\7-Kabale
```

Open the environment you've created, if you used Anaconda do the following in the terminal

```
conda activate 7-kabale
```

Install the packages

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

## Running the application

1. Start DroidCam on your phone and PC or use your own webcam and skip the two next steps
    1. Both the phone and PC must be on the same WiFi
    1. The PC's device IP must match the phone's IP for it to be able to connect
2. Run the Detector_Mod.py program
3. Start detecting cards for every pile 
    1. Choose a pile to add the card to by pressing "1 - 7" or the arrow keys on the keyboard
    1. If a mistake was made, clear the pile by pressing "c"
    1. When done scanning press "e"
4. When all piles have been scanned, the game begins.
    1. Scan the waste pile when needed
    1. Try to follow the moves being indicated on the GUI
5. Have fun!

## Authors

* **Asama Hayder** - *CV & ML* - [asamahayder](https://github.com/asamahayder)
* **Christoffer A. Detlef** - *Project Manaegment* - [ChrisMizz](https://github.com/ChrisMizz)
* **Jákup V. Dam** - *Logic* - [jayveedee](https://github.com/jayveedee)
* **Simon Andersen** - *Project Manaegment* - [ThaDuyx](https://github.com/ThaDuyx)
* **Thaer Mhd. R. Almalla** - *Project Manaegment* - [Thaer91](https://github.com/Thaer91)

## Acknowledgments

* [qqwwee's keras implementation of YOLOv3](https://github.com/qqwweee/keras-yolo3)
* [geaxgx's playing card generation implementation](https://github.com/geaxgx/playing-card-detection)
* [AntonMu's implementation of training your own YOLO](https://github.com/AntonMu/TrainYourOwnYOLO)