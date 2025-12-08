from __future__ import annotations

import re
from collections import Counter


WORD_PATTERN = re.compile(r"[a-z0-9']+")
SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+")
STOPWORDS = {
    "the",
    "a",
    "an",
    "and",
    "or",
    "is",
    "are",
    "to",
    "in",
    "of",
    "for",
    "on",
    "with",
    "that",
    "this",
}


def split_sentences(text: str) -> list[str]:
    sentences = [s.strip() for s in SENTENCE_SPLIT.split(text.strip()) if s.strip()]
    return sentences


def tokenize(text: str) -> list[str]:
    return [w for w in WORD_PATTERN.findall(text.lower()) if w not in STOPWORDS]


def summarize(text: str, max_sentences: int = 2) -> list[str]:
    sentences = split_sentences(text)
    if not sentences:
        return []
    if len(sentences) <= max_sentences:
        return sentences

    frequencies = Counter(tokenize(text))
    scored = []
    for idx, sentence in enumerate(sentences):
        score = sum(frequencies[token] for token in tokenize(sentence))
        scored.append((idx, score, sentence))
    top = sorted(scored, key=lambda row: row[1], reverse=True)[:max_sentences]
    return [row[2] for row in sorted(top, key=lambda row: row[0])]
