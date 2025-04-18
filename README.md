# CNN + Transfer Learning Models in TensorFlow (Google Colab)

This project explores image classification using one custom Convolutional Neural Network (CNN) and four popular pre-trained models via Transfer Learning:
- Custom CNN
- VGG16
- ResNet50
- EfficientNetV2B3
- DenseNet

All training is done using **TensorFlow/Keras in Google Colab** notebooks.

# Structure
```
cnn-transfer-learning-colab/
├── notebooks/
│   ├── custom_model.ipynb
│   ├── DenseNet.ipynb
│   ├── EfficientNetV2B3.ipynb
│   ├── resnet50_model.ipynb
│   └── vgg16_model.ipynb
├── requirements.txt
├── main.cpp
└── README.md
```

## How to use
### 1. Clone the Repository
```
!git clone https://github.com/AxelSierra1/cnn-transfer-learning-colab.git
%cd cnn-transfer-learning-colab
```
### 2. Run in Google Colab
You can open each notebook directly in Colab. Each notebook is self-contained and walks through the process of:
- Loading and preprocessing data
- Building and training the model
- Evaluating performance

## Dataset


## Saving & Loading Models
Trained models are saved in the .keras format. To avoid large files in version control, they are stored in google drive

## Requirements

## Results

