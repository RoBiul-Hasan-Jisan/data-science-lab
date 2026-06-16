import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create sample data: heights and weights
data = {
    'Height_cm': np.random.normal(170, 10, 100),
    'Weight_kg': np.random.normal(65, 15, 100),
    'Gender': np.random.choice(['Male', 'Female'], 100)
}

df = pd.DataFrame(data)

# Basic stats
print("Data Head:")
print(df.head())

print("\nSummary Statistics:")
print(df.describe())

# Plot: Distribution of Height by Gender
sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='Height_cm', hue='Gender', kde=True, bins=20)
plt.title('Height Distribution by Gender')
plt.xlabel('Height (cm)')
plt.ylabel('Count')
plt.show()
