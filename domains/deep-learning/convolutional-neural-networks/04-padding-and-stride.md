---
title: "4. Padding & Stride"
description: "Control output size — same padding vs downsampling strides."
domain: deep-learning
tags: [cnn, padding-stride]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 4. Padding & Stride

> Control output size — same padding vs downsampling strides.

## Definition

- **Padding** adds border pixels so convolution can preserve (or grow) spatial size  
- **Stride** steps the kernel; stride > 1 downsamples  

## Mental model

| Setting | Effect on H×W |
|---------|----------------|
| stride=1, padding=same | ≈ preserve |
| stride=2 | ≈ halve |
| padding=0 | shrink by kernel edges |

## Code

```python
import torch.nn as nn

nn.Conv2d(3, 32, 3, stride=2, padding=1)
```

---

## Continue

- **Section hub:** [Convolutional Neural Networks](README.md)
- **DL overview:** [Deep Learning](../README.md)
