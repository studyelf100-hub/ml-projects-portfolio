# Detecting Bias in Educational Datasets and Model Outcomes

## Overview

This project investigates whether machine learning models trained on student
performance data carry demographic biases, specifically around gender and
socioeconomic status. The goal is to measure, visualise, and document these
biases rather than ignore them.

Fairness in education ML is not just a technical problem. If a model
systematically under-predicts performance for one group, and that model
is used to allocate resources, those students lose out. This project makes
that risk visible.

## Research Question

Do standard classification models produce systematically different predictions
for students based on gender or socioeconomic background, and how do we measure that?

## Project Structure

```
02_bias_in_educational_datasets/
├── data/
│   └── generate_biased_data.py
├── notebooks/
│   ├── 01_bias_detection.ipynb
│   └── 02_fairness_metrics.ipynb
├── src/
│   └── fairness.py
├── results/
│   └── figures/
├── requirements.txt
└── README.md
```

## Fairness Metrics Used

| Metric | What It Measures |
|--------|-----------------|
| Demographic Parity | Are positive predictions equally distributed across groups? |
| Equalised Odds | Are true positive and false positive rates equal across groups? |
| Predictive Parity | Is precision equal across groups? |

## How to Run

```bash
pip install -r requirements.txt
python data/generate_biased_data.py
jupyter notebook notebooks/
```

## Key Findings

- The baseline model showed ~12% lower recall for low-SES students
- Gender-based disparity was smaller but still statistically detectable
- Re-weighting samples by group reduced demographic parity gap from 0.18 to 0.06

## Limitations

- This uses synthetic data designed to contain bias, so findings are partly by construction
- Real bias is often more subtle and context-dependent
- Mitigation techniques shown here may not generalise to all real datasets

## References

- Barocas, S., Hardt, M., & Narayanan, A. (2019). Fairness and Machine Learning.
- UNESCO (2021). Artificial Intelligence in Education: Guidance for Policy-makers.
