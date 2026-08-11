---
title: "2. TensorFlow"
description: "Google's DL platform — graphs/eager, TF Serving, and TFX pipelines."
domain: deep-learning
tags: [frameworks, tensorflow]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 2. TensorFlow

> Google's DL platform — graphs/eager, TF Serving, and TFX pipelines.

## Definition

**TensorFlow** is an end-to-end ML platform (training + serving). Modern TF uses eager execution with Keras as the high-level API.

## Sketch

```python
import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(10),
])
model.compile(optimizer="adam", loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True))
```

## Docs

- https://www.tensorflow.org/

---

## Continue

- **Section hub:** [Deep Learning Frameworks](README.md)
- **DL overview:** [Deep Learning](../README.md)
