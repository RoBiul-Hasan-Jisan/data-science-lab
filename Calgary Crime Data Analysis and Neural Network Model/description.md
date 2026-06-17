# Calgary Crime Data Analysis and Neural Network Prediction

## Project Overview

**Calgary Crime Data Analysis and Neural Network Prediction** is a data science and deep learning project focused on analyzing crime patterns in Calgary and predicting future crime occurrences using historical crime data.

The project uses the **Crime and Disorder Data** provided by the City of Calgary, covering crime records from **2018 to 2024**. The dataset contains monthly crime statistics across different communities, allowing for the exploration of crime trends, seasonal patterns, and geographical distributions.

The primary goal is to perform comprehensive data analysis and develop an **LSTM (Long Short-Term Memory) neural network model** to forecast future crime trends.

---

## Project Objectives

The main objectives of this project are:

- Analyze historical crime patterns in Calgary
- Identify high-risk and low-risk communities
- Understand crime category distributions
- Discover seasonal and yearly crime trends
- Build a time-series forecasting model using LSTM
- Predict future crime occurrences based on historical patterns

---

## Project Workflow

The project follows these major steps:

### 1. Data Loading and Understanding

- Importing the crime dataset
- Exploring dataset structure and features
- Understanding crime categories, locations, and time information

### 2. Data Preprocessing

Data preparation steps include:

- Handling missing values
- Cleaning inconsistent records
- Converting data types
- Preparing time-series data for modeling

### 3. Exploratory Data Analysis (EDA)

Detailed analysis was performed to discover:

- Crime distribution by community
- Crime category frequency
- Yearly crime trends
- Monthly crime patterns
- Relationships between communities and crime categories

### 4. Neural Network Modeling

A deep learning model was developed using:

- **LSTM (Long Short-Term Memory)** neural network
- Time-series sequence learning
- Historical crime patterns for future prediction

### 5. Model Training and Optimization

The model was trained by:

- Creating sequential input data
- Splitting data into training, validation, and testing sets
- Optimizing model parameters
- Monitoring training and validation loss

### 6. Future Crime Prediction

The trained model was used to forecast future crime occurrences based on previous crime trends.

---

# Exploratory Data Analysis Insights

## 1. Community Crime Distribution

Analysis of crime distribution across Calgary communities revealed:

### Highest Crime Communities

| Rank | Community | Crime Percentage |
|---|---|---|
| 1 | Beltline | 11.4% |
| 2 | Forest Lawn | 10.7% |
| 3 | Downtown Commercial Core | 10.2% |

### Lowest Crime Communities

| Rank | Community | Crime Percentage |
|---|---|---|
| 1 | 13M | 22.7% |
| 2 | 02K | 13.6% |
| 3 | 02B | 13.6% |

---

## 2. Crime Category Analysis

The most common crime categories were:

| Crime Category | Percentage |
|---|---|
| Theft from Vehicle | 21.7% |
| Theft of Vehicle | 16.7% |
| Break and Enter - Commercial | 13.8% |

The analysis shows that property-related crimes represent a significant portion of reported incidents.

---

## 3. Yearly Crime Trends

Key observations:

- **2019** recorded the highest number of reported crimes.
- **2022** and **2018** also showed significant crime activity.
- The **2024 dataset was incomplete**, containing only partial yearly records.

---

## 4. Monthly Crime Patterns

Monthly analysis revealed variations in crime frequency, suggesting the presence of:

- Seasonal crime patterns
- Periodic changes in crime rates
- Time-dependent trends

---

## 5. Community and Crime Category Relationship

Different communities showed different crime patterns:

- Forest Lawn had higher occurrences of **Break and Enter - Other Premises**.
- Marlborough showed lower occurrences of **Commercial Robbery**.
- Certain crime categories were concentrated in specific areas.

---

# Neural Network Model

## LSTM Time-Series Forecasting Model

An **LSTM (Long Short-Term Memory)** neural network was used because it is highly effective for time-series forecasting and can capture long-term dependencies in sequential data.

---

## Model Development Process

### Sequence Preparation

- Historical crime records were transformed into sequential data.
- Previous time periods were used to predict future crime counts.

### Train-Test Split

The dataset was divided into:

- Training data
- Validation data
- Testing data

to evaluate model performance.

---

## Model Architecture

The LSTM model architecture consists of:
