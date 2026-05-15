# Bias in Educational Datasets

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)  ![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3.0-F7931E?logo=scikit-learn&logoColor=white)  ![pandas](https://img.shields.io/badge/pandas-2.1.0-150458?logo=pandas&logoColor=white)  ![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)  ![License](https://img.shields.io/badge/License-MIT-green)  ![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

---

My maths teacher mentioned once that some schools in the UK use algorithmic tools to predict which students need extra support. I started thinking about what those tools were trained on. If the training data came from a school system that already had inequalities built into it, the model would just learn those inequalities and present them as predictions. Nobody would necessarily notice.

That question is what this project is about.

## What I was trying to find out

Two things, which are actually quite different problems.

First: does a model trained on student data perform differently for students from lower socioeconomic backgrounds compared to higher ones?

Second: if there is a gap, is the model creating it or is it already in the data?

Those lead to different solutions. If the model is creating the gap then you fix the model. If the gap is already in the data then fixing the model alone doesn't actually help the students. You'd need to address what's upstream of the data.

## Fairness metrics

I used demographic parity and equalised odds.

Demographic parity asks: does the model predict "pass" at the same rate for both groups? It's the blunter of the two metrics.

Equalised odds asks: when students do pass, does the model catch them at the same rate for both groups? And when students fail, does it incorrectly flag them at the same rate for both groups? It's more precise about which kind of error you're measuring.

These two metrics can actually contradict each other. You can satisfy one and violate the other at the same time. There's a set of impossibility theorems about this in the fairness literature that I read about after finishing this project. I didn't go deep enough on that and it's probably worth a whole separate investigation.

## What the results showed

The demographic parity gap was bigger than I expected. The model was predicting "pass" at noticeably different rates for high-SES and low-SES students. But it wasn't doing anything strange. The features used for prediction (study hours, internet access, previous scores) are all correlated with socioeconomic status. The model was just following the data.

The gender gap was smaller but it showed up in the false positive rate. The model was more likely to incorrectly flag female students as failing when they weren't. I don't have a clean explanation for why that happened. It might be a feature correlation issue in how I generated the data.

## Project structure

```
02_bias_in_educational_datasets/
├── data/
│   └── generate_data.py
├── notebooks/
│   ├── 01_eda_and_group_distributions.ipynb
│   ├── 02_model_training.ipynb
│   └── 03_fairness_audit.ipynb
├── src/
│   └── fairness.py
├── results/
│   └── figures/
├── requirements.txt
└── README.md
```

## How to run it

```bash
pip install -r requirements.txt
python data/generate_data.py
# notebooks in order: 01, 02, 03
```

## What I would do differently

I computed the fairness metrics after training and then adjusted the threshold as a mitigation. That's the most common approach but it's a patch on top of a model that was built without fairness in mind. There are methods that build fairness into the training process directly. I read about adversarial debiasing after finishing this project. Threshold adjustment works but it would be worth comparing it to something more integrated.

I also only looked at SES and gender as separate axes. I didn't look at what happens at the intersection, specifically low-SES female students. That's called intersectional fairness analysis. I just didn't think to do it while I was building the project.

## Limitations

The bias I'm measuring here is partly bias I introduced when generating the synthetic data. I tried to make the correlations reflect real patterns from education research but it's not real data, so there's a ceiling on how much I can claim about what these results mean for actual school systems.