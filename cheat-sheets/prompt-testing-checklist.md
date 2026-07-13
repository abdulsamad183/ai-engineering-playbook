# Prompt Testing Checklist

> Pre-production prompt validation. See [Prompt Testing](../domains/prompt-engineering/prompt-testing.md).

## Before Shipping

- [ ] Golden dataset with ≥20 representative cases
- [ ] Edge cases: empty input, very long input, ambiguous input
- [ ] Adversarial: instruction injection attempts in user content
- [ ] Regression suite runs in CI on prompt changes
- [ ] Output format validated programmatically (not eyeball)
- [ ] Temperature 0.0 for deterministic tasks; tested at prod temperature
- [ ] Token count within budget (system + user + max output)
- [ ] Tested on primary model AND fallback model
- [ ] Failure cases documented with expected behavior

## Per Change

- [ ] Version bumped in prompt metadata
- [ ] Changelog entry written
- [ ] A/B comparison on golden set (accuracy, not vibes)
- [ ] No PII in test fixtures committed to repo

## Red Flags

- Accuracy dropped >5% on golden set
- New failure mode not in failure catalog
- Output format parse errors increased

## See Also

- [Prompt Evaluation](../domains/prompt-engineering/prompt-evaluation.md)
- [example-prompt-evaluation.py](../examples/prompt-engineering/example-prompt-evaluation.py)
