# Extractive Text Summarizer

This miniature project builds a local, rules-based extractive summarizer using only synthetic/fictional text.

## What it does

- Splits input into sentences.
- Scores sentences with word-frequency statistics.
- Returns top-ranked sentences in original order.

## Concepts it teaches

- Tokenization and stopword filtering
- Frequency-based sentence ranking
- Extractive (not generative) summarization

## Install

No third-party dependencies.

```bash
python --version
```

## Run

```bash
cd summarization/extractive
python cli.py
```

## Test

```bash
cd summarization/extractive
python -m unittest discover -s tests -p "test_*.py"
```

## Representative output

```text
Summary:
- ...
- ...
```

## Main components

- `summarizer.py`: sentence splitting and scoring
- `cli.py`: runnable demo
- `tests/test_summarizer.py`: correctness checks

## Data note

All text examples are fictional/synthetic.

## Limitations and exercises

- Ranking is frequency-based and can miss nuance.
- Try adding position bias, TF-IDF weighting, or sentence-length normalization.

## Disclosure

This is a retrospective educational addition created now. Historical author dates may be used for commit metadata and do not indicate the actual execution date of this work.
