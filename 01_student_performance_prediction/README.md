# Student Performance Prediction Across Different Education Systems

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)  ![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3.0-F7931E?logo=scikit-learn&logoColor=white)  ![XGBoost](https://img.shields.io/badge/XGBoost-1.7.6-189BE7)  ![pandas](https://img.shields.io/badge/pandas-2.1.0-150458?logo=pandas&logoColor=white)  ![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)  ![License](https://img.shields.io/badge/License-MIT-green)  ![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

---

I kept hearing two completely different explanations for why students fail. In Nigeria people usually say it's about effort, not studying enough, not being serious. In a lot of the education research I was reading online the answer was almost always about resources: internet access, whether your parents went to university, school funding. I wanted to see what the data actually said and whether a model trained on students in one country would even work on students somewhere else.

The answer I got was that both things matter, but in different proportions. Which is not a clean finding. I wasn't sure whether to be satisfied with it or not.

## What I was trying to find out

The main question was about cross-system transfer. Can you train a model on Nigerian student data and have it still be useful when you apply it to Portuguese students? This is harder than it sounds because even the same feature, like "study hours per week," means something different depending on context. Three hours of studying in Lagos is a different thing to three hours in Lisbon, in terms of what's competing for that time, what the home environment looks like, what the school expects.

I also wanted to know which features were stable across both systems. The ones that kept showing up as important no matter which dataset you trained on.

## The data

I generated synthetic datasets modelled on two real education systems. The Portugal one is based on a dataset that actually gets used in education research (Cortez and Silva, 2008), so I had real distributions to work from. The Nigeria one I built from PISA reports and what I know, which is imperfect but I didn't want to just invent everything.

Features in both:
- Study hours per week
- Attendance rate
- Previous exam scores
- Parent education level
- Internet access at home
- School type (public or private)
- Extracurricular participation
- Teacher-to-student ratio

## The models

I ran three. Looking back I probably could have run two and gotten to the same conclusions. I used Random Forest and XGBoost separately because I thought they would behave differently, and they really didn't. XGBoost was slightly stronger but not by enough to justify having both.

| Model | Why I used it |
|---|---|
| Logistic Regression | Simplest baseline, easy to read the coefficients |
| Random Forest | Handles mixed feature types, good feature importances |
| XGBoost | Usually strongest on tabular data, and it was |

## What the results showed

When I trained on Portugal data and tested on Nigeria data, F1 dropped from around 0.84 to about 0.61. That's a real drop. It tells you these are not just two versions of the same problem with different names on them.

Attendance rate and previous exam scores were the two features that stayed important in both systems. Everything else shifted around depending on which dataset you were looking at. The socioeconomic features, internet access and parent education, were strong in the Portugal data and much weaker in the Nigeria data. My best guess is there's less variance in those features in the Nigeria dataset because the students are more similar to each other on those dimensions.

## Project structure

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

## How to run it

```bash
pip install -r requirements.txt
python data/generate_data.py
# then open notebooks in order: 01, 02, 03
```

## What I would do differently

In notebook 02 I used cross-validation properly. In notebook 03 where I do the cross-system evaluation, I used a single train/test split. I should have done cross-validation there too, run it multiple times with different seeds and averaged the results, because one split's result depends on which specific students ended up in the test set. I knew cross-validation mattered when I wrote notebook 02 and then just didn't apply it consistently. That's the thing I'd fix first.

Also I treated this as a binary classification problem, pass or fail. Student performance is actually continuous and collapsing it into two categories loses information. A student at 51% and a student at 89% both become "pass" even though those are very different situations.

## Limitations

The data is synthetic so the cross-system findings are a signal, not a fact. I tried to ground the distributions in real reports but I can't claim these are real student records.

## References

- Cortez, P., and Silva, A. (2008). Using data mining to predict secondary school student performance.
- PISA (2022). Programme for International Student Assessment results.