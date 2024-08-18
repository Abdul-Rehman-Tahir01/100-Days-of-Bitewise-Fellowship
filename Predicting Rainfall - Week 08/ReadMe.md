# Predicting Rainfall using Different Machine Learning Models

This project involves the prediction of rainfall using different machine learning models in Jupyter Notebook and it also contains a UI (using streamlit) which can give predictions based on user inputs. The dataset contains features such as pressure, humidity, temperature, and more. Through this analysis, we aim to build a model that accurately predicts the occurence of rainfall based on the given input features.

## Dataset

The rainfall dataset used for this prediction includes various features related to rainfall occurence, such as pressure, humidity, temperature, and the target variable: rainfall. This dataset is provided in the project directory or it can be downloaded directly by visiting the following link:
<a href=' https://media.geeksforgeeks.org/wp-content/uploads/20240510131249/Rainfall.csv' alt='Dataset Link'>Dataset Download Link</a>

## Prerequisites

Before running the code, make sure you have the following dependencies installed:

- Python (3.x)
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- imblearn
- streamlit
- joblib

All these dependencies are given in the requirements.txt file. To download these dependencies, run the following command on your terminal (make sure you are in the project directory):

  ``` pip install -r requirements.txt ```

To check if pip is installed, run command:

  ``` pip --version ```

<br>

## Analysis Overview

The Jupyter notebook provides a step-by-step guide to predict rainfall using five different machine learning models. The analysis includes the following tasks:

- Loading and understanding the dataset (Exploratory Data Analysis - EDA)
- Data cleaning and preprocessing
- Splitting the dataset into training and testing sets
- Training the models. The models trained were: ``` LOGISTIC REGRESSION, DECISION TREES, RANDOM FOREST, GRADIENT BOOSTING MACHINES and SUPPORT VECTOR MACHINES (SVM) ```
- Evaluating the model's performance using classification metrics such as accuracy, precision, recall, F1 score and ROC-AUC score.
- Making predictions on new data

The aim is to find the model which model perfomrs the best in this scenario.

## Usage

This project has two parts. 

- The first part is the .ipynb jupyter notebook file which contains the actual analysis project file.
- The second part is the .py file which is actually the UI of the model, made using streamlit library. It takes the input from the user and predicts whether it'll rain or not. To run this UI, run the following commands:
  1. Install the Streamlit library.
     
     ``` pip install streamlit ```
     
  3. Locate to the project's directory where the UI.py file is located and run:
     
     ``` streamlit run UI.py ```

     This will open up your browser with UI of the project looking something like this:

     ![image](https://github.com/user-attachments/assets/61d027be-8e30-4045-8cc4-addbe114604f)

<br>

## Results and Insights

After training these models and evaluating their performances, you will gain insights into the different models and that the best performing model is Logistic Regression model which predicts the rainfall occurence most accurately. The notebook includes performance metrics and visualizations to assess the accuracy of the model. Feel free to refer to the notebook for detailed results and interpretations.

## Customization

You can customize the analysis to suit your specific requirements. For example, you can experiment with different feature engineering techniques, try different classification algorithms, or incorporate additional features from the dataset to improve the model's accuracy.

## Acknowledgments

- This prediction is inspired by the need to predict rainfall correctly, which can be useful for metrological professionals in understanding rainfall patterns and planning appropriate interventions.
- This analysis was assigned to us by Bytewise Fellowship Program ML/DL 2024.

## Contribution

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
