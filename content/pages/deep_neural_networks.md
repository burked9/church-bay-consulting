Title: Deep Neural Networks for Fair Market Value pricing
Slug: deep-neural-networks
Date: 2025-12-27
Category: Projects
Tags: Deep Learning, Pricing, AI, Aviation

> Applying non-linear deep learning architectures to capture high-dimensional asset valuations across rotables and airframe components.

## Introduction

In the aviation industry, determining the Fair Market Value (FMV) of assets is a complex task involving numerous interdependent variables. Traditionally, the Fair Market Value of an aircraft is determined by evaluating its physical age, total hours/cycles, maintenance history, market cycle position, and specific configuration—summing up the estimated valuations of individual components known as "Aircraft Rotables".

Traditional pricing methodologies rely on historical transaction and quote data using standard linear regression models. While linear models work well for simple trendlines, they frequently struggle to capture complex non-linear relationships, multi-variable interactions, and high-dimensional dynamics such as sudden market demand shifts, inventory scarcity, and operator-specific fleet variations.

This project outlines how **Deep Neural Networks (DNNs)** can be applied to enhance the accuracy of FMV estimations, providing a flexible framework for building predictive asset valuation models.

---

## Methodology

To address the limitations of linear models, we employ a Multi-Layer Perceptron (MLP) architecture capable of ingesting diverse aircraft parameters to estimate current market values.

### Understanding Deep Neural Networks in Asset Valuation
Unlike linear estimators, a Deep Neural Network passes input features through multiple hidden layers of non-linear activations (such as ReLU). This allows the network to learn intricate feature interactions—such as how the value depreciation curve of a high-demand avionics module changes as an airframe approaches a major heavy maintenance check (C-Check/D-Check).

Through backpropagation and optimization algorithms (like Adam), the network iteratively adjusts node weights to minimize valuation errors (Mean Absolute Error and Mean Squared Error) across historical training datasets.

### Data Sources & Feature Engineering
Accurate valuation models depend on robust feature representation. Inputs to the model generally fall into three key categories:
1. **Utilization & Age Metrics**: Total Time Since New (TTSN), Total Cycles Since New (TCSN), Time Since Overhaul (TSO).
2. **Configuration Metadata**: Part Number revisions, mod status, engine variant compatibility.
3. **Market Context**: Historical quote trends, active fleet utilization rates, and component scarcity indices.

### Data Preprocessing
Before feeding raw asset data into the network, continuous numerical metrics are scaled, and categorical identifiers (such as aircraft type or engine family) are encoded into numerical vectors:

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def preprocess_data(df):
    """
    Preprocesses aircraft and rotable data for the neural network.
    """
    numerical_features = ['age', 'total_hours', 'cycles']
    categorical_features = ['aircraft_type', 'engine_model']
    
    # Normalize numerical features to zero mean and unit variance
    scaler = StandardScaler()
    df[numerical_features] = scaler.fit_transform(df[numerical_features])
    
    # One-hot encode categorical variables
    encoder = OneHotEncoder(sparse_output=False)
    encoded_cats = encoder.fit_transform(df[categorical_features])
    
    # Combine normalized metrics and encoded categories
    df_processed = pd.concat([
        df[numerical_features].reset_index(drop=True), 
        pd.DataFrame(encoded_cats).reset_index(drop=True)
    ], axis=1)
    
    return df_processed
```

---

## Model Architecture

The neural network is constructed using TensorFlow/Keras. The architecture includes an input layer, three dense hidden layers with ReLU activations, dropout regularization to prevent overfitting on rare part numbers, and a linear output node for price estimation:

```python
import tensorflow as tf
from tensorflow.keras import layers, models

def build_fmv_model(input_shape):
    """
    Constructs a Multi-Layer Perceptron DNN for FMV regression.
    """
    model = models.Sequential([
        # Input Layer
        layers.InputLayer(input_shape=input_shape),
        
        # Hidden Layers with ReLU & Dropout
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.2), # Regularization
        layers.Dense(64, activation='relu'),
        layers.Dense(32, activation='relu'),
        
        # Output Layer (Linear regression output for dollar valuation)
        layers.Dense(1, activation='linear')
    ])
    
    model.compile(
        optimizer='adam',
        loss='mean_squared_error',
        metrics=['mae'] # Mean Absolute Error in USD
    )
    
    return model
```

---

## Key Performance Insights

During training evaluation on baseline sets:
- **Loss Convergence**: The model rapidly minimizes Mean Squared Error (MSE) within 50 epochs, with dropout layers effective in stabilizing validation loss.
- **Valuation Accuracy**: Compared to traditional linear regression baselines, the deep neural network exhibits significantly lower Mean Absolute Error (MAE) on complex, multi-option components.

---

## Future Work & Scope

This project serves as an open framework for exploring modern machine learning in aviation asset pricing. All code structures demonstrated here are designed for flexibility and can be adapted to specific internal fleet data or proprietary pricing databases.

---
*For questions or to discuss machine learning applications in aviation asset management, please reach out via the [Contact Page]({filename}/pages/contact.md).*
