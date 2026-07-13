# AI Evaluation Examples

> Phase 10 patterns. See [AI Evaluation Handbook](../../domains/ai-evaluation/README.md).

Uses `eval_utils.py` for shared patterns. Simplified implementations — install `ragas` / `deepeval` for production frameworks.

| Example | Pattern |
|---------|---------|
| [eval_utils.py](eval_utils.py) | Shared harness helpers |
| [example-ragas-evaluation.py](example-ragas-evaluation.py) | RAGAS-style RAG metrics |
| [example-deepeval-pipeline.py](example-deepeval-pipeline.py) | DeepEval-style asserts |
| [example-prompt-evaluation.py](example-prompt-evaluation.py) | Prompt regression |
| [example-rag-evaluation.py](example-rag-evaluation.py) | Retrieval metrics |
| [example-agent-evaluation.py](example-agent-evaluation.py) | Tool trace accuracy |
| [example-latency-measurement.py](example-latency-measurement.py) | P50/P95 latency |
| [example-cost-tracking.py](example-cost-tracking.py) | Per-request cost |
| [example-hallucination-detection.py](example-hallucination-detection.py) | Citation checks |
| [example-ab-testing.py](example-ab-testing.py) | A/B assignment |
| [example-evaluation-dashboard.py](example-evaluation-dashboard.py) | Dashboard aggregation |
| [example-regression-testing.py](example-regression-testing.py) | CI regression gate |

```bash
cd examples/ai-evaluation
python example-regression-testing.py
python example-ragas-evaluation.py
```
