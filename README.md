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
├── preprocessing/
│   ├── convert_and_split_test.py
│   └── convert_and_split_train.py
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
This project uses histopathology image data for colon cancer classification:

### Training & Validation
- Dataset: NCT-CRC-HE-100K
- Classes:
    - 0_non_cancer
    - 1_adenocarcinoma
- Preprocessing (done locally):
    - Converted .tif to .jpg
    - Labeled and classified into binary classes
    - Split into 80% training / 20% validation
 
### Testing
- Dataset: CRC-VAL-HE-7K
- Classes:
    - 0_non_cancer
    - 1_adenocarcinoma
- Preprocessing (done locally):
    - Converted .tif to .jpg
    - Labeled and classified into binary classes
 
Note: The data preparation was done locally, not in Colab. The training and evaluation pipelines assume the dataset is already preprocessed and structured in image folders by class.

## Saving & Loading Models
Trained models are saved in the .keras format. To avoid large files in version control, they are stored in google drive

## Requirements

## Results

