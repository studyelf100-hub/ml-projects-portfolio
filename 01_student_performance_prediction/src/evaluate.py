"""
Evaluation utilities for cross-system model comparison.
"""

from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns


def evaluate_model(model, X_test, y_test, class_names, title="Model Evaluation"):
    y_pred = model.predict(X_test)
    print(f"\n=== {title} ===")
    print(classification_report(y_test, y_pred, target_names=class_names))

    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt="d", xticklabels=class_names, yticklabels=class_names, cmap="Blues")
    plt.title(title)
    plt.ylabel("Actual")
    plt.xlabel("Predicted")
    plt.tight_layout()
    plt.savefig(f"../results/figures/{title.replace(' ', '_').lower()}.png", dpi=150)
    plt.show()
