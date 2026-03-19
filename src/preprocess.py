# src/preprocess.py

import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    # Chỉ drop duplicates ở đây, KHÔNG fillna hay scale toàn cục
    df = df.drop_duplicates()
    return df

def split_data(df, target_col='Potability', test_size=0.2, random_state=42):
    # Tách X, y và chia Train/Test ngay từ đầu để tránh Data Leakage
    X = df.drop(target_col, axis=1)
    y = df[target_col]
    return train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)

def save_data(df, path):
    df.to_csv(path, index=False)