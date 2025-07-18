# src/preprocess.py
import pandas as pd

def load_and_preprocess(file_path, is_train=True):
    df = pd.read_csv(file_path)

    if is_train:
        df = df[['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']]
    else:
        df = df[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']]

    df['Age'].fillna(df['Age'].median(), inplace=True)
    df['Fare'].fillna(df['Fare'].median(), inplace=True)
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

    return df
