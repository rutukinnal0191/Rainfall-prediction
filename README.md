# RAINFALL PREDICTION USING MACHINE LEARNING

# Project Overview

Rainfall prediction plays an important role in agriculture and weather planning.
This project focuses on predicting whether rainfall will occur or not using Logistic Regression

The project uses historical weather data, applies basic preprocessing, builds a prediction model, and visualizes the results using histograms.

# OBJECTIVES:

This project aims to:

Predict rainfall occurrence using Logistic Regression

Understand model prediction distribution using visualization

Apply machine learning concepts on real-world weather data

# DATASET INFORMATION:

The dataset contains weather-related features such as:

Temperature

Humidity

Wind Speed

Pressure

Rainfall (target variable)

# TECHONOLOGIES USED:

Python

Pandas

NumPy

Matplotlib

Scikit-learn

pickel

# PROJECT WORKFLOW:

Import Libraries

Imported required Python libraries for data handling, modeling, and visualization.

Data Loading

Loaded the rainfall dataset using Pandas.

Data Preparation

Selected relevant features

Converted target variable into binary form

Split dataset into training and testing sets

Model Building (Logistic Regression)

Applied Logistic Regression for rainfall prediction

Trained the model using training data

Generated predictions on test 

# KEY LEARNINGS:

Logistic Regression can be used for binary classification problems

Proper data preparation is crucial for accurate predictions

Machine learning models can be applied to real-world weather data

# Rainfall Prediction Model

This project predicts rainfall using Logistic Regression.

## How to use

1. Clone the repo:
   git clone <your-link>

2. Install dependencies:
   pip install -r requirements.txt

3. Run prediction:
   python predict.py

## Reusability

Model and scaler are saved as pickle files.
No need to retrain the model.

You can also import the function:

from predict import predict_rain
