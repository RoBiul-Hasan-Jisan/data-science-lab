# Belarus Car Price Prediction

Dataset: https://www.kaggle.com/datasets/slavapasedko/belarus-used-cars-prices

## Project Overview

The **Belarus Car Price Prediction** project focuses on predicting vehicle prices in the Belarusian automotive market using machine learning techniques. The project analyzes important vehicle attributes such as manufacturer, model, production year, condition, mileage, fuel type, engine volume, color, transmission, drive unit, and car segment.

The dataset contains **56,244 car records with 12 features**, where the objective is to identify the key factors influencing car prices and develop a predictive model capable of estimating vehicle values accurately.

---

## Dataset Information

### Data Dictionary

| Feature | Description |
|---------|-------------|
| make | Car manufacturer/brand |
| model | Specific car model |
| price USD | Car price in USD (Target Variable) |
| year | Year of production |
| condition | Vehicle condition at the time of sale |
| mileage | Total mileage in kilometers |
| fuel type | Fuel category (electric, petrol, diesel) |
| volume(cm3) | Engine volume in cubic centimeters |
| color | Exterior color of the vehicle |
| transmission | Transmission type |
| drive unit | Vehicle drivetrain system |
| segment | Vehicle market segment |

---

## Exploratory Data Analysis Insights

The exploratory data analysis revealed several important patterns in the Belarus car market:

- Car prices increased significantly for vehicles manufactured after the year 2000.
- Petrol vehicles with automatic transmission generally had higher prices compared to diesel vehicles with manual transmission.
- Electric vehicles showed considerably higher prices compared to traditional fuel-based vehicles.
- All-wheel-drive vehicles had the highest average prices among different drivetrain categories.
- Specialty segment vehicles were the most expensive, followed by luxury European, American, and Asian vehicle segments.

These insights demonstrate how vehicle specifications and market segments influence pricing trends.

---

## Machine Learning Model

A **Decision Tree Regressor** was implemented to predict car prices.

### Model Performance

- **Algorithm:** Decision Tree Regressor
- **Evaluation Metric:** R² Score
- **Performance:** 85.29% R² Score

The model achieved strong predictive performance, demonstrating that machine learning can effectively estimate vehicle prices based on historical market data.

---

## Feature Importance

The feature importance analysis showed that the most influential factors affecting car prices were:

1. **Year of Production**
2. **Engine Volume (cm³)**

These features played the largest role in determining the predicted market value of vehicles.

---

## Project Impact

This project provides valuable insights into the Belarus automotive market and can help:

- Buyers estimate fair vehicle prices.
- Sellers understand important pricing factors.
- Automotive analysts identify market trends.
- Businesses develop data-driven pricing strategies.

Overall, this project demonstrates the practical application of machine learning for real-world price prediction problems.
