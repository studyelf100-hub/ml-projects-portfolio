"""
Generates a synthetic student dataset with known demographic bias patterns.
The bias is embedded intentionally so we can detect and measure it.
"""

import numpy as np
import pandas as pd

np.random.seed(0)
n = 800

gender = np.random.choice(["male", "female"], n, p=[0.5, 0.5])
ses = np.random.choice(["low", "medium", "high"], n, p=[0.35, 0.40, 0.25])

study_hours = np.where(ses == "high",
    np.random.normal(14, 3, n),
    np.where(ses == "medium", np.random.normal(11, 3, n), np.random.normal(8, 3, n))
).clip(1, 30)

attendance = np.where(ses == "high",
    np.random.beta(9, 1.5, n),
    np.where(ses == "medium", np.random.beta(7, 2, n), np.random.beta(5, 3, n))
)

prev_score = np.where(ses == "high",
    np.random.normal(70, 10, n),
    np.where(ses == "medium", np.random.normal(62, 12, n), np.random.normal(54, 14, n))
).clip(0, 100)

score = (
    0.3 * prev_score
    + 8 * study_hours
    + 15 * attendance
    + np.random.normal(0, 8, n)
)

threshold = np.median(score)
grade = (score > threshold).astype(int)

df = pd.DataFrame({
    "gender": gender,
    "socioeconomic_status": ses,
    "study_hours": study_hours,
    "attendance": attendance,
    "previous_score": prev_score,
    "passed": grade
})

df.to_csv("student_bias_data.csv", index=False)
print(f"Generated {n} rows.")
print("Pass rate by SES:")
print(df.groupby("socioeconomic_status")["passed"].mean().round(3))
print("Pass rate by gender:")
print(df.groupby("gender")["passed"].mean().round(3))
