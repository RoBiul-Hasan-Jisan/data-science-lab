# src/predict.py
import pandas as pd
from preprocess import load_and_preprocess
from sklearn.linear_model import LogisticRegression

# Train model
train_df = load_and_preprocess('data/train.csv', is_train=True)
X_train = train_df.drop('Survived', axis=1)
y_train = train_df['Survived']
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predict test set
test_df = load_and_preprocess('data/test.csv', is_train=False)
predictions = model.predict(test_df)

# Load passenger IDs for submission
passenger_ids = pd.read_csv('data/test.csv')["PassengerId"]

# Match Kaggle's sample format
submission = pd.DataFrame({
    "PassengerId": passenger_ids,
    "Survived": predictions
})
submission.to_csv("submission/submission.csv", index=False)
print("✅ Submission created similar to gender_submission.csv")
