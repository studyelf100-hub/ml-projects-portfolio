"""
Generates synthetic student datasets for Nigeria and Portugal education systems.
Run this before opening the notebooks.
"""

import numpy as np
import pandas as pd

np.random.seed(42)

def generate_nigeria(n=500):
    data = {
        "study_hours_per_week": np.random.normal(12, 4, n).clip(1, 30),
        "attendance_rate": np.random.beta(7, 2, n),
        "parent_education_level": np.random.choice([0, 1, 2, 3], n, p=[0.3, 0.35, 0.25, 0.1]),
        "has_internet": np.random.choice([0, 1], n, p=[0.45, 0.55]),
        "extracurricular": np.random.choice([0, 1], n, p=[0.4, 0.6]),
        "school_type": np.random.choice([0, 1], n, p=[0.6, 0.4]),  # 0=public, 1=private
        "teacher_student_ratio": np.random.normal(35, 8, n).clip(15, 60),
        "previous_score": np.random.normal(58, 15, n).clip(0, 100),
        "system": "nigeria"
    }
    df = pd.DataFrame(data)
    # Performance score influenced by features
    score = (
        0.3 * df["previous_score"]
        + 8 * df["study_hours_per_week"]
        + 15 * df["attendance_rate"]
        + 5 * df["has_internet"]
        + 3 * df["extracurricular"]
        + 4 * df["parent_education_level"]
        - 0.2 * df["teacher_student_ratio"]
        + np.random.normal(0, 8, n)
    )
    df["final_grade"] = pd.cut(score, bins=3, labels=["low", "medium", "high"])
    return df

def generate_portugal(n=500):
    data = {
        "study_hours_per_week": np.random.normal(10, 3, n).clip(1, 25),
        "attendance_rate": np.random.beta(8, 1.5, n),
        "parent_education_level": np.random.choice([0, 1, 2, 3], n, p=[0.15, 0.3, 0.35, 0.2]),
        "has_internet": np.random.choice([0, 1], n, p=[0.2, 0.8]),
        "extracurricular": np.random.choice([0, 1], n, p=[0.35, 0.65]),
        "school_type": np.random.choice([0, 1], n, p=[0.75, 0.25]),
        "teacher_student_ratio": np.random.normal(20, 5, n).clip(10, 35),
        "previous_score": np.random.normal(65, 12, n).clip(0, 100),
        "system": "portugal"
    }
    df = pd.DataFrame(data)
    score = (
        0.35 * df["previous_score"]
        + 7 * df["study_hours_per_week"]
        + 12 * df["attendance_rate"]
        + 4 * df["has_internet"]
        + 2 * df["extracurricular"]
        + 5 * df["parent_education_level"]
        - 0.15 * df["teacher_student_ratio"]
        + np.random.normal(0, 7, n)
    )
    df["final_grade"] = pd.cut(score, bins=3, labels=["low", "medium", "high"])
    return df

if __name__ == "__main__":
    ng = generate_nigeria()
    pt = generate_portugal()
    combined = pd.concat([ng, pt], ignore_index=True)

    ng.to_csv("nigeria_students.csv", index=False)
    pt.to_csv("portugal_students.csv", index=False)
    combined.to_csv("combined_students.csv", index=False)
    print("Datasets generated successfully.")
    print(f"Nigeria: {len(ng)} rows | Portugal: {len(pt)} rows")
