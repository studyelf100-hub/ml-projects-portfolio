"""
Preprocessing utilities for student performance data.
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler


def load_and_prepare(filepath):
    df = pd.read_csv(filepath)
    df = df.dropna()

    feature_cols = [
        "study_hours_per_week", "attendance_rate", "parent_education_level",
        "has_internet", "extracurricular", "school_type",
        "teacher_student_ratio", "previous_score"
    ]

    X = df[feature_cols].copy()
    y = df["final_grade"].copy()

    le = LabelEncoder()
    y = le.fit_transform(y)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y, le.classes_
