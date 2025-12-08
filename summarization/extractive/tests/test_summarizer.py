import unittest

from summarizer import summarize


class SummarizerTests(unittest.TestCase):
    def test_returns_requested_sentence_count(self) -> None:
        text = (
            "Python helps beginners learn programming quickly. "
            "Python syntax is often concise and readable. "
            "Databases are useful for storing records."
        )
        result = summarize(text, max_sentences=2)
        self.assertEqual(len(result), 2)

    def test_handles_empty_text(self) -> None:
        self.assertEqual(summarize("", max_sentences=2), [])


if __name__ == "__main__":
    unittest.main()
