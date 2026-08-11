---
title: "4. Semi-Supervised Learning"
description: "Few labels, lots of unlabeled data — pseudo-labels and consistency."
domain: machine-learning
tags: [misc, semi-supervised]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 4. Semi-Supervised Learning

> Few labels, lots of unlabeled data — pseudo-labels and consistency.

## Definition

**Semi-supervised learning** uses a small labeled set plus abundant unlabeled data to improve models.

## Techniques

| Technique | Idea |
|-----------|------|
| Pseudo-labeling | Label unlabeled with model, retrain |
| Self-training | Iterative confidence filtering |
| Consistency | Agree under augmentation |
| Graph / label prop | Propagate labels on similarity graph |

## Uses

- Labeling is expensive (medical, moderation)  
- Bootstrap LLM preference / rubric data carefully

---

## Continue

- **Section hub:** [Miscellaneous ML](README.md)
- **ML overview:** [Machine Learning](../README.md)
