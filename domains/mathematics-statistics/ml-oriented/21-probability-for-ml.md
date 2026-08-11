---
title: "21. Probability for ML"
description: "Uncertainty in models — likelihoods, softmax, calibration, and generative modeling."
domain: mathematics-statistics
tags: [ml-math, probability]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 21. Probability for ML

> Uncertainty in models — likelihoods, softmax, calibration, and generative modeling.

## Definition

**Probability for ML** treats predictions as distributions: classification probs, noise models, sampling from generative models, and calibrated uncertainty.

## Key ideas

| Idea | ML meaning |
|------|------------|
| Softmax | Categorical distribution over classes |
| Cross-entropy | Negative log-likelihood |
| MLE / MAP | Training objectives |
| Calibration | Predicted probs match frequencies |
| Latent variables | Generative / VAE-style models |
| Temperature | Softmax sharpness |

## Code

```python
import numpy as np

logits = np.array([2.0, 1.0, 0.1])
# temperature scaling
T = 1.5
p = np.exp(logits / T)
p = p / p.sum()
print(p)

# NLL of true class 0
nll = -np.log(p[0])
print("nll", nll)
```

## Uses

- Classification heads and loss design  
- Sampling strategies (top-k, nucleus)  
- Evaluating uncertainty / calibration  

## See also

- [4. Probability Theory](../mathematics/04-probability-theory.md) · [10. Probability Distributions](../statistics/10-probability-distributions.md)

---

## Continue

- **Section hub:** [ML-Oriented Mathematics](README.md)
- **Math & Stats overview:** [Mathematics & Statistics](../README.md)
