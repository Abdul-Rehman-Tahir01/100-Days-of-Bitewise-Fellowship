# Classifying Traffic Signs Using Deep Learning Models

This project involves the classification of traffic signs using different deep learning models in Jupyter Notebook and it also contains a UI - an API endpoint (using Flask) which can give predictions based on user inputs. The dataset contains a large number of traffic sign low resolution images.  Through this analysis, we aim to build an AI-driven system that accurately classify and identify the traffic signs based on the visual images.

## Dataset

The dataset used for this classification is the famous <b>German Traffic Sign Recognition Benchmark (GTSRB)</b> dataset which includes 50 thousand traffic sign images out of which 40 thousand are for training and remaining 10 thousand are for testing the models, out of 43 different classes. Since this dataset is large, so can't be provided directly inside the GitHub repository. The link to the kaggle site from where the dataset is used is provided below: <br>
<a href='https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign' alt='Dataset Link'>Dataset Download Link</a>

## Prerequisites

Before running the code, make sure you have the following dependencies installed:

- Python (3.x)
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Tensorflow/keras
- Opencv-python
- Pillow
- Flask
- Tensorflow-hub

All these dependencies are given in the requirements.txt file. To download these dependencies, run the following command on your terminal (make sure you are in the project directory):

  ``` pip install -r requirements.txt ```

To check if pip is installed, run command:

  ``` pip --version ```

<br>

## Analysis Overview

The Jupyter notebook provides a step-by-step guide to classify traffic signs using two different deep learning models. The analysis includes the following tasks:

- Loading and understanding the dataset
- Data cleaning and preprocessing
- Data Augmentation
- Using a pre-trained ESRGAN model for image super-resolution.
- Training the CNN model for classification purpose.
- Evaluating the model's performance using metrics such as training accuracy, validation accuracy, training loss and validation loss.
- Making predictions on new data

The aim is to create an AI-driven system that can identify traffic signs with great accuracy to help self-driving cars make run-time decisions.

## Usage

This project has two parts. 

- The first part is the .ipynb jupyter notebook file which contains the actual analysis project file.
- The second part is the .py file which is actually the UI or API endpoint of the model (model deployment), made using flask library. It takes the input from the user and classify the traffic sign. To run this UI, run the following commands:
  1. Install the Streamlit library.
     
     ``` pip install flask ```
     
  2. Locate to the project's directory where the UI.py file is located and run:
     
     ``` python UI.py ```

     This will provide you with a link that you can open up in your browser which will contain UI of the project looking something like this:

     ![image](https://github.com/user-attachments/assets/de0df5cf-c6cc-4053-b705-917d02adc9d4)



<br>

## Results and Insights

After enhancing the training images using ESRGAN and training the CNN model and evaluating their performances, you will gain insights into the performance of these models and how these model integrate together to create to an AI-driven classification system. The notebook includes performance metrics and visualizations to assess the accuracy of the model. Feel free to refer to the notebook for detailed results and interpretations.

## Customization

You can customize the analysis to suit your specific requirements. For example, you can experiment with different techniques for enhancing images, try different CNN architecture, or incorporate additional models to improve the system's accuracy.

## Acknowledgments

- This classification is inspired by the need to identify the traffic road signs, which can be useful for self-driving cars in understanding the traffic flow and create a smooth experience.
- This analysis was assigned to us by Bytewise Fellowship Program ML/DL 2024.

## Contribution

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
