#  Crop Yield Prediction 

## 📌 Project Overview
This project focuses on predicting agricultural crop yield using environmental and soil-related features. The goal is to build a machine learning model that can estimate crop productivity (Quintals per acre) based on key factors such as rainfall, temperature, fertilizer usage, and soil macronutrient levels.

Accurate yield prediction can help farmers, agronomists, and policymakers make better data-driven decisions to improve agricultural output and food security.

---

## 📊 Dataset Description

The dataset contains environmental and agricultural features that influence crop growth and yield.

| Feature Name        | Description                                  |
|---------------------|----------------------------------------------|
| Rain Fall (mm)      | Total rainfall in millimeters               |
| Temperature (°C)    | Average temperature in Celsius              |
| Fertilizer (kg)     | Amount of fertilizer used                   |
| Nitrogen (N)        | Nitrogen content in soil                    |
| Phosphorous (P)     | Phosphorus content in soil                  |
| Potassium (K)       | Potassium content in soil                   |
| Yield (Q/acres)     | Target variable: crop yield per acre        |

---

## 🧹 Data Preprocessing

- Removed invalid entries in the Temperature column (e.g., ":")
- Converted all numerical columns to appropriate data types
- Handled missing values using median imputation
- Checked and cleaned inconsistent data entries
- Normalized understanding of feature distributions for analysis

---

## 📈 Exploratory Data Analysis (EDA)

Key insights from the data:

- 🌱 The dataset likely contains **multiple crop types**, indicated by clustering patterns in features and yield.
- 🌧️ Rainfall and temperature show significant influence on crop yield.
- 🌾 Fertilizer usage generally improves yield, but with diminishing returns at higher levels.
- 🧪 Nitrogen, Phosphorus, and Potassium levels vary widely, suggesting different soil conditions.
- 🔥 Temperature is one of the most influential predictors of yield variation.

---

## 🤖 Model Building

Two regression models were trained and evaluated:

- Decision Tree Regressor  
- Random Forest Regressor  

### 📊 Model Performance

| Model               | R² Score |
|--------------------|----------|
| Decision Tree       | 0.77     |
| Random Forest       | 0.802    |

---

## 🏆 Results & Insights

- Random Forest outperformed Decision Tree due to better generalization and reduced overfitting.
- Temperature and rainfall are the most important features in predicting crop yield.
- Fertilizer and macronutrients also contribute significantly to model predictions.
- The dataset may contain hidden crop groupings affecting overall patterns.

---

## 🚀 Conclusion

This project demonstrates how machine learning can be used to predict agricultural crop yield based on environmental and soil data. The Random Forest model achieved the best performance with an R² score of **0.802**, making it a reliable model for prediction.

---

## 🔮 Future Improvements

- Add more features like humidity, soil pH, and crop type
- Try advanced models like XGBoost or LightGBM
- Perform clustering to separate crop types
- Apply hyperparameter tuning for better accuracy

---

## 📌 Tech Stack

- Python 🐍
- Pandas & NumPy
- Scikit-learn
- Matplotlib / Seaborn

---

## ⭐ Author

Developed as a Data Science portfolio project.
