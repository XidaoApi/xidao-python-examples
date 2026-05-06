# XiDao Python Examples


[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) [![GitHub release](https://img.shields.io/github/v/release/XidaoApi/xidao-python-examples)](https://github.com/XidaoApi/xidao-python-examples/releases) [![GitHub stars](https://img.shields.io/github/stars/XidaoApi/xidao-python-examples?style=social)](https://github.com/XidaoApi/xidao-python-examples/stargazers)


OpenAI-compatible Python examples for developers who want a practical starting point, not just the first hello-world request.

## Why this repo exists

If your app already uses the OpenAI Python SDK, you can often test a new endpoint with only three changes:

1. change the API key
2. change the base URL
3. choose the target model

That makes this repo useful for teams working on:
- OpenAI-compatible migration tests
- rollout validation
- fallback and routing experiments
- cost-aware workload splitting

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export XIDAO_API_KEY="***"
python examples/chat_completion.py
```

## Base configuration

```python
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ["XIDAO_API_KEY"],
    base_url="https://global.xidao.online/v1"
)
```

## Included examples

- `examples/chat_completion.py` — minimal OpenAI-compatible chat completion
- `examples/embeddings.py` — embedding request example
- `examples/cost_aware_summary.py` — simple low-value-task cost control example

## Production-minded extensions to add next

- streaming example
- retry boundary example
- structured output / JSON validation example
- fallback handoff example

## Related guides

- `../xidao-cookbook/guides/migrate-from-openai.md`
- `../xidao-cookbook/guides/openai-compatible-rollout-checklist.md`
- `../xidao-cookbook/guides/llm-failover-routing-patterns.md`
- `../xidao-cookbook/guides/vercel-ai-sdk-openai-compatible.md`
- `../xidao-cookbook/guides/reduce-api-costs.md`

## Related repos

- `../llm-failover-router-demo`
- `../xidao-cookbook`

## Links

- Website: https://global.xidao.online/
- Support: support@xidao.online
- Telegram: https://t.me/ccyu085
