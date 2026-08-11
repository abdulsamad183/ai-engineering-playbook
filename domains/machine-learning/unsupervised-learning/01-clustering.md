---
title: "1. Clustering"
description: "Group similar points without labels — goals, distance, and validation heuristics."
domain: machine-learning
tags: [unsupervised, clustering]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 1. Clustering

> Group similar points without labels — goals, distance, and validation heuristics.

## Definition

**Clustering** partitions (or densifies) data into groups so that points in a cluster are more similar to each other than to other clusters.

## Design choices

| Choice | Examples |
|--------|----------|
| Distance | Euclidean, cosine |
| Shape assumption | Spherical (k-means) vs density (DBSCAN) |
| k known? | Elbow / silhouette vs density params |

```mermaid
flowchart LR
  X[Features] --> Scale[Scale / embed]
  Scale --> Algo[Clustering algo]
  Algo --> Labels[Cluster IDs]
  Labels --> Check[Silhouette / domain check]
```

## Uses

- Customer segments, document themes, anomaly neighborhoods

---

## Continue

- **Section hub:** [Unsupervised Learning](README.md)
- **ML overview:** [Machine Learning](../README.md)
