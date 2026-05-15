# Student Performance Prediction Across Different Education Systems

## Overview

This project looks at whether machine learning models can predict how well students
will perform academically, and whether those predictions hold up across different
education systems (Nigeria, Portugal, and a simulated general dataset). The goal is
not just to get a high accuracy score, but to understand what actually drives student
outcomes and whether the same features matter everywhere.

## Research Question

Can a model trained on one education system's data generalise to another, and which
student features are most predictive of performance regardless of context?

## Project Structure

```
01_student_performance_prediction/
├── data/
│   ├── generate_data.py
│   ├── nigeria_students.csv
│   ├── portugal_students.csv
│   └── combined_students.csv
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_model_training.ipynb
│   └── 03_cross_system_evaluation.ipynb
├── src/
│   ├── preprocess.py
│   └── evaluate.py
├── results/
│   └── figures/
├── requirements.txt
└── README.md
```

## Methodology

1. Generate synthetic student datasets modelled after real education system structures
2. Run exploratory data analysis (EDA) on each dataset separately
3. Train multiple classifiers (Logistic Regression, Random Forest, Gradient Boosting)
4. Evaluate models trained on one system and tested on another (cross-system transfer)
5. Identify which features are consistently important across both systems

## Features Used

- Study hours per week
- Parent education level
- Attendance rate
- Access to internet at home
- Extracurricular participation
- School type (public/private)
- Teacher-to-student ratio
- Previous exam scores

## Models

| Model | Why It's Here |
|-------|--------------|
| Logistic Regression | Simple baseline, easy to interpret |
| Random Forest | Handles mixed feature types well |
| Gradient Boosting (XGBoost) | Usually strong on tabular data |

## Key Findings

See `notebooks/03_cross_system_evaluation.ipynb` for full results. Summary:
- Models trained on Portugal data performed moderately on Nigeria data (F1 ~0.61)
- Attendance rate and previous scores were the two most stable cross-system predictors
- Socioeconomic features (internet access, parent education) were more system-specific

## How to Run

```bash
pip install -r requirements.txt
python data/generate_data.py
jupyter notebook notebooks/
```

## Requirements

See `requirements.txt`. Python 3.9+.

## Limitations

- Data is synthetic, so real-world generalisation is not guaranteed
- Education systems are complex; this model captures surface-level patterns only
- Cross-system transfer assumes similar grading scales, which is a simplification

## References

- Cortez, P., & Silva, A. (2008). Using data mining to predict secondary school student performance.
- PISA (2022). Programme for International Student Assessment results.
