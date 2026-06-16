import streamlit as st
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from sklearn.preprocessing import StandardScaler

st.title("Global Temperature Prediction ")

DATA_URL = "https://berkeley-earth-temperature.s3.us-west-1.amazonaws.com/Global/Land_and_Ocean_complete.txt"

@st.cache_data
def load_data():
    df_list = []
    with pd.io.common.urlopen(DATA_URL) as f:
        for line in f:
            line = line.decode("utf-8").strip()
            if line.startswith("#") or line == "":
                continue
            parts = line.split()
            if len(parts) >= 3:
                try:
                    year = float(parts[0])
                    month = float(parts[1])
                    anomaly = float(parts[2])
                    df_list.append([year, month, anomaly])
                except:
                    continue
    df = pd.DataFrame(df_list, columns=["Year", "Month", "Monthly_Anomaly"])
    return df

df = load_data()

# Sidebar input
st.sidebar.header("Input Date")
input_year = st.sidebar.number_input("Year", min_value=int(df['Year'].min()), max_value=int(df['Year'].max()) + 10, value=int(df['Year'].max()) + 1)
input_month = st.sidebar.number_input("Month", 1, 12, 1)
input_day = st.sidebar.number_input("Day", 1, 31, 1)

# Prepare training data
X = df[["Year", "Month"]].values.astype(np.float32)
y = df["Monthly_Anomaly"].values.astype(np.float32).reshape(-1,1)

# Scale data
scaler_X = StandardScaler()
scaler_y = StandardScaler()
X_scaled = scaler_X.fit_transform(X)
y_scaled = scaler_y.fit_transform(y)

X_tensor = torch.tensor(X_scaled, dtype=torch.float32)
y_tensor = torch.tensor(y_scaled, dtype=torch.float32)

# PyTorch model
class LinearRegressionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(2,1)
    def forward(self, x):
        return self.linear(x)

model = LinearRegressionModel()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Train silently
epochs = 1000
for epoch in range(epochs):
    optimizer.zero_grad()
    outputs = model(X_tensor)
    loss = criterion(outputs, y_tensor)
    loss.backward()
    optimizer.step()

# Predict
input_array = np.array([[input_year, input_month]], dtype=np.float32)
input_scaled = scaler_X.transform(input_array)
input_tensor = torch.tensor(input_scaled, dtype=torch.float32)
pred_scaled = model(input_tensor).detach().numpy()
predicted_anomaly = scaler_y.inverse_transform(pred_scaled)[0][0]

# Convert to temperature (approx baseline 14°C)
temp_c = 14 + predicted_anomaly
temp_f = temp_c * 9/5 + 32

st.write(f"### Predicted Temperature for {int(input_day)}/{int(input_month)}/{int(input_year)}")
st.write(f" Celsius: {temp_c:.2f} °C")
st.write(f" Fahrenheit: {temp_f:.2f} °F")
