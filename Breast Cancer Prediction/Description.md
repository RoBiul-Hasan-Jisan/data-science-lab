# Breast Cancer Prediction

## Project Overview

**Breast Cancer Prediction** is a machine learning classification project that aims to predict whether a breast tumor is **malignant (cancerous)** or **benign (non-cancerous)** based on features extracted from digitized images of **Fine Needle Aspirate (FNA)** samples.

The dataset contains numerical measurements of cell nuclei characteristics. These features describe different properties of breast mass cells and are used to train machine learning models for accurate classification and early detection.

---

## Dataset Description

The dataset consists of samples of breast masses with the following information:

### Target Variable

| Feature | Description |
|---|---|
| **Diagnosis** | The target variable representing tumor type |
| | `M` → Malignant |
| | `B` → Benign |

### Input Features

For each cell nucleus, several numerical features are calculated to describe its characteristics:

| Feature | Description |
|---|---|
| **Radius** | Mean distance from the center of the nucleus to points on the perimeter |
| **Texture** | Standard deviation of gray-scale values inside the nucleus |
| **Perimeter** | Length of the nucleus boundary |
| **Area** | Total area occupied by the nucleus |
| **Smoothness** | Measures local variation in radius lengths |
| **Compactness** | Measures nucleus shape compactness using perimeter and area |
| **Concavity** | Represents the severity of concave regions in the nucleus contour |
| **Concave Points** | Number of concave portions in the nucleus boundary |
| **Symmetry** | Measures the symmetry of the nucleus shape |
| **Fractal Dimension** | Estimates the complexity of the nucleus boundary using fractal geometry |

---

## Machine Learning Objective

The main objective of this project is to develop a classification model that can learn patterns from cell nucleus features and predict whether a breast mass is malignant or benign.

The project workflow includes:

- Data preprocessing
- Exploratory Data Analysis (EDA)
- Feature analysis and visualization
- Model training
- Model evaluation
- Performance comparison

---

## Machine Learning Models

Different classification algorithms can be applied, including:

- Logistic Regression
- Support Vector Machine (SVM)
- Decision Tree Classifier
- Random Forest Classifier
- K-Nearest Neighbors (KNN)
- Gradient Boosting
- Neural Networks

---

## Evaluation Metrics

To measure model performance, the following evaluation metrics are used:

- Accuracy Score
- Precision
- Recall
- F1-Score
- ROC-AUC Score
- Confusion Matrix

---

## Project Goal

The goal of this project is to build an effective machine learning model that can assist in distinguishing between malignant and benign breast tumors by analyzing cell nucleus characteristics.

This project demonstrates how machine learning techniques can be applied to healthcare datasets for predictive analysis and decision support.

> **Disclaimer:** This project is developed for educational and research purposes only. Machine learning predictions should not be considered a replacement for professional medical diagnosis.
