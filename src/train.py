# src/train.py

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

def create_pipeline(model):
    # Pipeline giúp Impute và Scale độc lập trên tập Train, không rò rỉ sang tập Test
    return Pipeline([
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler()),
        ('model', model)
    ])

def train_logistic(X_train, y_train):
    # Thêm class_weight='balanced'
    model = LogisticRegression(max_iter=1000, class_weight='balanced', random_state=42)
    pipeline = create_pipeline(model)
    pipeline.fit(X_train, y_train)
    return pipeline

def train_rf(X_train, y_train):
    # Thêm class_weight='balanced'
    model = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
    pipeline = create_pipeline(model)
    pipeline.fit(X_train, y_train)
    return pipeline