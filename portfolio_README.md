# ML Projects Portfolio

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3.0-F7931E?logo=scikit-learn&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.13-FF6F00?logo=tensorflow&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Projects](https://img.shields.io/badge/Projects-19-blueviolet)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

---

19 machine learning projects built across six domains — education, healthcare, finance, climate, agriculture, and NLP. Each one has a focused research question, clean reproducible code, and an honest account of what the results actually mean.

These are not tutorial reproductions. Every project starts with a problem, makes deliberate modelling choices, and ends with findings that include the limitations alongside the results.

---

## Project Index

### Education

| # | Project | Key Technique | Research Question |
|---|---------|---------------|-------------------|
| 01 | [Student Performance Prediction](./01_student_performance_prediction/) | Random Forest, XGBoost, cross-system transfer | Can a model trained in one country generalise to another? |
| 02 | [Bias in Educational Datasets](./02_bias_in_educational_datasets/) | Fairness metrics, demographic parity | Does the model perform equally across SES and gender groups? |
| 03 | [Ablation: Feature Importance](./03_ablation_feature_importance/) | Leave-one-out ablation, CV | Which features actually drive academic outcome predictions? |
| 04 | [Dropout Risk Prediction](./04_dropout_risk_prediction/) | Recall optimisation, threshold tuning | Can early warning systems be built from socioeconomic data? |

### Healthcare

| # | Project | Key Technique | Research Question |
|---|---------|---------------|-------------------|
| 05 | [Medical Diagnosis (Low Resource)](./05_medical_diagnosis_low_resource/) | Sample size experiments, 5 model types | How much data do you actually need for reliable predictions? |
| 06 | [Healthcare Fairness Audit](./06_healthcare_bias_fairness/) | Fairness metrics, re-weighting, threshold adjustment | Does a heart disease classifier perform equitably across groups? |

### Finance

| # | Project | Key Technique | Research Question |
|---|---------|---------------|-------------------|
| 07 | [Fraud Detection + Explainability](./07_fraud_detection_explainability/) | SMOTE, permutation importance, partial dependence | Can we explain which features drive fraud predictions? |
| 08 | [Stock Trend vs Random Baseline](./08_stock_trend_random_baseline/) | Forward-chain CV, portfolio simulation | Does stock trend prediction actually beat random guessing? |
| 09 | [Credit Risk Modelling](./09_risk_modeling_financial/) | Cost-sensitive evaluation, threshold optimisation | What is the real cost of false negatives in credit decisions? |

### Climate & Environment

| # | Project | Key Technique | Research Question |
|---|---------|---------------|-------------------|
| 10 | [Climate Data Forecasting](./10_climate_data_forecasting/) | Lag features, cyclical encoding, seasonal baseline | How well can ML forecast temperature and rainfall? |
| 11 | [Air Quality Prediction](./11_air_quality_prediction/) | Multi-step horizon forecasting, MAE-vs-horizon | How quickly does forecast accuracy degrade over time? |

### Agriculture

| # | Project | Key Technique | Research Question |
|---|---------|---------------|-------------------|
| 12 | [Crop Yield Prediction](./12_crop_yield_prediction/) | Feature sufficiency analysis, XGBoost | Can crop yield be predicted reliably with minimal sensor data? |
| 13 | [Missing Data in Agriculture](./13_missing_data_agricultural/) | MCAR/MAR missingness, 5 imputation strategies | Which imputation method holds up best under high missingness? |

### NLP

| # | Project | Key Technique | Research Question |
|---|---------|---------------|-------------------|
| 14 | [Text Classification (Educational)](./14_text_classification_educational/) | TF-IDF, LR/SVM/NB, error analysis | Can subject area be classified from short lesson text? |
| 15 | [Sentiment: Student Feedback](./15_sentiment_student_feedback/) | Sentiment classification, keyword theme extraction | What themes appear most in negative student feedback? |
| 16 | [Traditional ML vs Deep Learning (NLP)](./16_traditional_ml_vs_deep_learning_nlp/) | TF-IDF vs LSTM, training cost comparison | Does a neural network outperform SVM on short-text classification? |
| 17 | [Reproduce Kim (2014) TextCNN](./17_reproduce_research_paper_cnn/) | Multi-filter CNN, reproduction study | What does it actually take to reproduce a well-known NLP paper? |

### Robustness & Benchmarking

| # | Project | Key Technique | Research Question |
|---|---------|---------------|-------------------|
| 18 | [Model Robustness: Noise Injection](./18_model_robustness_noise_injection/) | Gaussian/masking/label noise, degradation curves | How much does performance drop — and at what rate — under real-world noise? |
| 19 | [Full Model Benchmarking Study](./19_benchmarking_multiple_models/) | 7 models, 5-fold CV, performance-cost tradeoff | Which model should you actually use, and what is the tradeoff? |

---

## How Each Project Is Structured

Every repository follows the same layout:

```
NN_project_name/
├── data/
│   └── generate_data.py        # Run this first to create the dataset
├── notebooks/
│   ├── 01_eda.ipynb            # Exploration and baseline
│   ├── 02_training.ipynb       # Model training and tuning
│   └── 03_analysis.ipynb       # Results, interpretation, limitations
├── src/
│   └── *.py                    # Reusable utility modules
├── results/
│   └── figures/                # Plots (generated by notebooks)
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

---

## How to Run Any Project

```bash
# 1. Clone this repo or download the individual project folder
# 2. Install dependencies
pip install -r requirements.txt

# 3. Generate the dataset
python data/generate_data.py

# 4. Open Jupyter and run notebooks in order (01, 02, 03)
jupyter notebook
```

Python 3.10+ recommended. For projects 16 and 17, TensorFlow is required.

---

## Themes Across the Series

A few things come up repeatedly because they matter in practice:

**Baselines first.** Every project establishes a naive baseline before running any model. If you cannot beat random guessing or a majority classifier, the model has not learned anything useful.

**Fairness is not optional.** Three projects explicitly audit models for demographic fairness. In education and healthcare especially, a model that works on average but fails for specific groups is not a safe model.

**Small data changes everything.** Several projects (05, 12, 13) focus on what happens when you have less data than you want. The answer is almost always: simpler models, more careful validation, and honesty about uncertainty.

**Deep learning is not automatically better.** Project 16 shows a linear SVM beating an LSTM on a small dataset. Project 17 shows that reproducing a CNN paper from scratch is harder than reading it.

**Robustness matters as much as accuracy.** Project 18 exists because a model's clean test performance tells you very little about how it behaves when data quality drops — which it always does in deployment.

---

## License

MIT. Use, modify, and build on anything here.
