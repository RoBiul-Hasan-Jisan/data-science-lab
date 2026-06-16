import numpy as np
import pandas as pd
import os
import joblib

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Models
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from catboost import CatBoostRegressor

# --- Load Data ---
df = pd.read_csv(r"D:\ml_lern\data\kc_house_data.csv")

# Drop unwanted columns
for col in ['id', 'date']:
    if col in df.columns:
        df.drop(col, axis=1, inplace=True)

X = df.drop('price', axis=1).values
y = df['price'].values

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Polynomial features (degree 2)
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train_scaled)
X_test_poly = poly.transform(X_test_scaled)

# Create model save directory
model_dir = r"D:\ml_lern\model"
os.makedirs(model_dir, exist_ok=True)

def evaluate_and_save(model, name, X_tr, X_te, save_name):
    model.fit(X_tr, y_train)
    y_pred = model.predict(X_te)

    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    cv_r2 = cross_val_score(model, X, y, cv=5, scoring='r2').mean()

    print(f"\n📌 Model: {name}")
    print(f"R² Score: {r2:.4f}")
    print(f"MAE: {mae:.4f}")
    print(f"MSE: {mse:.4f}")
    print(f"RMSE: {rmse:.4f}")
    print(f"Cross-Validated R² (5-fold): {cv_r2:.4f}")

    # Save model
    path = os.path.join(model_dir, save_name)
    joblib.dump(model, path)
    print(f" Saved {name} model at: {path}")

# Run & save all models:

# Linear family
evaluate_and_save(LinearRegression(), "Simple Linear Regression", X_train_scaled, X_test_scaled, "linear_regression.pkl")
evaluate_and_save(LinearRegression(), "Multiple Linear Regression", X_train_scaled, X_test_scaled, "multiple_linear_regression.pkl")
evaluate_and_save(LinearRegression(), "Polynomial Regression (degree=2)", X_train_poly, X_test_poly, "polynomial_regression.pkl")

# Regularized
evaluate_and_save(Ridge(alpha=1.0), "Ridge Regression", X_train_scaled, X_test_scaled, "ridge_regression.pkl")
evaluate_and_save(Lasso(alpha=0.1), "Lasso Regression", X_train_scaled, X_test_scaled, "lasso_regression.pkl")
evaluate_and_save(ElasticNet(alpha=0.1, l1_ratio=0.5), "Elastic Net", X_train_scaled, X_test_scaled, "elastic_net.pkl")

# Advanced
evaluate_and_save(SVR(kernel='rbf', C=100, epsilon=0.1), "Support Vector Regression", X_train_scaled, X_test_scaled, "svr.pkl")
evaluate_and_save(DecisionTreeRegressor(max_depth=6), "Decision Tree Regressor", X_train, X_test, "decision_tree.pkl")
evaluate_and_save(RandomForestRegressor(n_estimators=100, max_depth=6), "Random Forest Regressor", X_train, X_test, "random_forest.pkl")
evaluate_and_save(XGBRegressor(n_estimators=100, learning_rate=0.1, verbosity=0), "XGBoost Regressor", X_train, X_test, "xgboost.pkl")
evaluate_and_save(LGBMRegressor(n_estimators=100, learning_rate=0.1), "LightGBM Regressor", X_train, X_test, "lightgbm.pkl")
evaluate_and_save(CatBoostRegressor(verbose=0), "CatBoost Regressor", X_train, X_test, "catboost.pkl")
evaluate_and_save(KNeighborsRegressor(n_neighbors=5), "KNN Regressor", X_train_scaled, X_test_scaled, "knn.pkl")

# Save scaler and polynomial features
joblib.dump(scaler, os.path.join(model_dir, "scalers.pkl"))
print(f" Saved scaler at: {os.path.join(model_dir, 'scalers.pkl')}")

joblib.dump(poly, os.path.join(model_dir, "polys.pkl"))
print(f" Saved polynomial features transformer at: {os.path.join(model_dir, 'polys.pkl')}")
