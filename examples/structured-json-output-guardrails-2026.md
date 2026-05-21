# Structured JSON Output Guardrails for OpenAI-Compatible LLMs (May 2026)

![License](https://img.shields.io/github/license/XidaoApi/xidao-python-examples) ![Stars](https://img.shields.io/github/stars/XidaoApi/xidao-python-examples?style=social) ![Last Commit](https://img.shields.io/github/last-commit/XidaoApi/xidao-python-examples)

Robust Python helpers for validating and normalizing structured JSON output from modern LLMs in 2026.

This example focuses on a real production pain point: models often wrap JSON in markdown fences, prepend commentary, leak reasoning tags, or return subtly invalid payloads. The utility below extracts the most likely JSON object/array, validates it against a lightweight schema, and works with any **OpenAI-compatible** endpoint — including **XiDao API Gateway** for provider switching across Claude Sonnet 4.7, GPT-5.5 mini, Gemini 2.5 Pro, DeepSeek V3.1, Qwen3, and more.

## Why this matters

- **Structured outputs still fail in production** when prompts are long, tools are enabled, or providers differ.
- **Provider portability** is easier if your app can tolerate small formatting quirks.
- **Gateway routing** lets you swap providers without rewriting your app logic.

## Python snippet

```python
import json
import re
from typing import Any, Iterable

FENCE_RE = re.compile(r"^```(?:json)?\s*|\s*```$", re.IGNORECASE)
THINK_RE = re.compile(r"<think>.*?</think>", re.DOTALL | re.IGNORECASE)


def strip_wrappers(text: str) -> str:
    text = THINK_RE.sub("", text).strip()
    text = FENCE_RE.sub("", text).strip()
    return text


def extract_json_candidate(text: str) -> str:
    text = strip_wrappers(text)

    # Fast path: already valid JSON
    try:
        json.loads(text)
        return text
    except json.JSONDecodeError:
        pass

    # Look for the first balanced object or array
    starts = [i for i, ch in enumerate(text) if ch in '{[']
    for start in starts:
        stack = []
        in_string = False
        escape = False
        for i, ch in enumerate(text[start:], start=start):
            if in_string:
                if escape:
                    escape = False
                elif ch == '\\':
                    escape = True
                elif ch == '"':
                    in_string = False
                continue

            if ch == '"':
                in_string = True
            elif ch in '{[':
                stack.append(ch)
            elif ch in '}]':
                if not stack:
                    break
                opener = stack.pop()
                if (opener, ch) not in {('{', '}'), ('[', ']')}:
                    break
                if not stack:
                    candidate = text[start:i + 1]
                    json.loads(candidate)  # raises if invalid
                    return candidate

    raise ValueError('No valid JSON object/array found in model output')


def validate_required_keys(payload: dict[str, Any], required: Iterable[str]) -> None:
    missing = [key for key in required if key not in payload]
    if missing:
        raise ValueError(f"Missing required keys: {missing}")


def normalize_structured_output(raw_text: str, required_keys: Iterable[str] = ()) -> dict[str, Any] | list[Any]:
    candidate = extract_json_candidate(raw_text)
    data = json.loads(candidate)
    if isinstance(data, dict) and required_keys:
        validate_required_keys(data, required_keys)
    return data
```

## XiDao usage example

```python
from openai import OpenAI

client = OpenAI(
    api_key='YOUR_XIDAO_KEY',
    base_url='https://api.xidaoapi.com/v1',
)

response = client.chat.completions.create(
    model='gpt-5.5-mini',
    temperature=0,
    messages=[
        {'role': 'system', 'content': 'Return JSON with keys: sentiment, summary, action_items'},
        {'role': 'user', 'content': 'Summarize this support conversation and suggest next steps.'},
    ],
)

raw = response.choices[0].message.content
structured = normalize_structured_output(raw, required_keys=['sentiment', 'summary', 'action_items'])
print(structured)
```

## Production tips

1. **Validate after every call** even if a provider advertises structured output support.
2. **Store the raw text** alongside the normalized payload for debugging.
3. **Keep schemas small** when routing across multiple providers.
4. **Use XiDao routing** to A/B test provider reliability for the same schema.

More OpenAI-compatible examples: https://github.com/XidaoApi/xidao-python-examples
XiDao API Gateway: https://xidaoapi.com/
