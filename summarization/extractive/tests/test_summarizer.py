import unittest

from summarizer import sentence_scores, summarize, top_sentence


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

    def test_sentence_scores(self) -> None:
        text = "Search ranking teaches retrieval. Retrieval needs test data."
        scores = sentence_scores(text)
        self.assertEqual(len(scores), 2)
        self.assertGreaterEqual(scores[0][1], 1)

    def test_top_sentence(self) -> None:
        text = "Search ranking teaches retrieval. Retrieval needs test data."
        best = top_sentence(text)
        self.assertIsNotNone(best)
        self.assertIsInstance(best[0], str)


if __name__ == "__main__":
    unittest.main()
