---
title: "4. Bayesian Optimization"
description: "Model the score surface — pick promising trials (Optuna, BayesSearch)."
domain: machine-learning
tags: [optimization, bayesian]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 4. Bayesian Optimization

> Model the score surface — pick promising trials (Optuna, BayesSearch).

## Definition

**Bayesian optimization** fits a surrogate of validation score vs hyperparameters and chooses the next trial to balance explore/exploit.

## Code (Optuna sketch)

```python
# pip install optuna
import optuna
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import GradientBoostingClassifier

def objective(trial):
    params = {
        "learning_rate": trial.suggest_float("lr", 0.01, 0.3, log=True),
        "max_depth": trial.suggest_int("max_depth", 2, 6),
        "n_estimators": trial.suggest_int("n_estimators", 50, 300),
    }
    model = GradientBoostingClassifier(**params, random_state=42)
    return cross_val_score(model, X_train, y_train, cv=3, scoring="f1").mean()

study = optuna.create_study(direction="maximize")
study.optimize(objective, n_trials=40)
```

## When

- Expensive trials / many hyperparameters

---

## Continue

- **Section hub:** [Model Optimization](README.md)
- **ML overview:** [Machine Learning](../README.md)
