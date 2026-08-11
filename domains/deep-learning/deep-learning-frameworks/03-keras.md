---
title: "3. Keras"
description: "High-level neural net API — fast iteration on top of TensorFlow (and historically multi-backend)."
domain: deep-learning
tags: [frameworks, keras]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 3. Keras

> High-level neural net API — fast iteration on top of TensorFlow (and historically multi-backend).

## Definition

**Keras** emphasizes ergonomic model building (`Sequential`, Functional API, subclassing) and a simple `fit` loop.

## Code

```python
from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    layers.Input(shape=(20,)),
    layers.Dense(64, activation="relu"),
    layers.Dense(1),
])
model.compile(optimizer="adam", loss="mse")
model.fit(X_train, y_train, epochs=5, validation_split=0.1)
```

---

## Continue

- **Section hub:** [Deep Learning Frameworks](README.md)
- **DL overview:** [Deep Learning](../README.md)
