# src/train.py

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

def train_logistic(X_train, y_train):
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    return model

def train_rf(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)
    return model