# XiDao Python Examples

Affordable OpenAI-compatible AI API gateway examples for Python developers.

## Why this repo exists

If your app already uses the OpenAI Python SDK, you can often switch to XiDao API with only three changes:

1. change the API key
2. change the base URL
3. choose the target model

That makes it easier to reduce AI API cost without rebuilding your product.

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
    base_url="https://api.xidao.online/v1"
)
```

## Included examples

- `examples/chat_completion.py`
- `examples/embeddings.py`
- `examples/cost_aware_summary.py`

## Use cases

- migrate from OpenAI with minimal code changes
- prototype AI features faster
- reduce API spend for production workloads
- test lower-cost routing options

## Related guides

- `../xidao-cookbook/guides/migrate-from-openai.md`
- `../xidao-cookbook/guides/openai-compatible-rollout-checklist.md`
- `../xidao-cookbook/guides/reduce-api-costs.md`

## Links

- Website: https://global.xidao.online/
- Support: support@xidao.online
- Telegram: https://t.me/ccyu085
