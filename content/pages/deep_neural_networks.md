Title: Deep Neural Networks for Fair Market Value pricing
Slug: deep-neural-networks
Date: 2025-12-27
Category: Projects
Tags: Deep Learning, AI, Aviation

# Deep Neural Networks for Fair Market Value Pricing

**Trend:** *Deep Learning*

## Introduction

In the aviation industry, determining the Fair Market Value (FMV) of assets is a complex task involving numerous variables. Usually, the Fair Market Value of an aircraft is determined by a combination of factors, including the aircraft's age, maintenance history, market cycle position, and configuration, and calculated specifically for comparison by summing the values of the aircraft's components, each known as an "Aircraft Rotable". Traditional methods effectively utilize linear regression and historical data, but they often struggle with non-linear relationships and high-dimensional data. This project explores the application of **Deep Neural Networks (DNNs)** to enhance the accuracy of FMV estimations.

## Methodology

We propose a multi-layered perceptron (MLP) model that takes in various aircraft parameters—age, maintenance history, market cycle position, and configuration—to predict the current market value.

(What is a Deep Neural Network?)

(Where does the data come from?)

### Data Preprocessing

Before feeding data into the neural network, it must be normalized. Here is a snippet demonstrating how we handle categorical variables like 'Aircraft Type' using one-hot encoding:

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def preprocess_data(df):
    """
    Preprocesses the aircraft data for the neural network.
    """
    # Separate numerical and categorical features
    numerical_features = ['age', 'total_hours', 'cycles']
    categorical_features = ['aircraft_type', 'engine_model']
    
    # Normalize numerical features
    scaler = StandardScaler()
    df[numerical_features] = scaler.fit_transform(df[numerical_features])
    
    # One-hot encode categorical features
    encoder = OneHotEncoder(sparse=False)
    encoded_cats = encoder.fit_transform(df[categorical_features])
    
    # Combine back into a single dataframe
    df_processed = pd.concat([
        df[numerical_features], 
        pd.DataFrame(encoded_cats)
    ], axis=1)
    
    return df_processed
```

## The Model Framework

We utilize TensorFlow/Keras to build the model. The architecture consists of an input layer, three hidden layers with ReLU activation, and a final output layer for the predicted price.

```python
import tensorflow as tf
from tensorflow.keras import layers, models

def build_fmv_model(input_shape):
    """
    Constructs a Deep Neural Network for FMV prediction.
    """
    model = models.Sequential([
        # Input Layer
        layers.InputLayer(input_shape=input_shape),
        
        # Hidden Layers
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.2), # Prevent overfitting
        layers.Dense(64, activation='relu'),
        layers.Dense(32, activation='relu'),
        
        # Output Layer (Linear activation for regression)
        layers.Dense(1, activation='linear')
    ])
    
    model.compile(
        optimizer='adam',
        loss='mean_squared_error',
        metrics=['mae'] # Mean Absolute Error
    )
    
    return model
```

## Results & Visualizations

*(Placeholder for Training Loss Graph)*
![Training Loss Graph - Coming Soon]({static}/images/placeholder_loss_graph.png)

*(Placeholder for Predicted vs Actual Valuation)*
![Valuation Scatter Plot - Coming Soon]({static}/images/placeholder_scatter_plot.png)

## Future Work

This model is an open-source tool which is open source, free to use and the details can be found on GitHub. Any templates used here are based around mock generated data and are not real aircraft data.


---
*For more information or to contribute to this project, please visit the [Contact Page]({filename}/pages/contact.md).*
