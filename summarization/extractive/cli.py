from __future__ import annotations

from summarizer import summarize


SAMPLE_TEXT = (
    "A fictional city library launched a local reading campaign this month. "
    "The campaign offers weekend storytelling sessions for children and parents. "
    "Volunteers also provide study circles that help students prepare for exams. "
    "Organizers reported strong attendance during the first two weekends."
)


def main() -> None:
    print("Extractive Summarizer Demo")
    print("Source text:")
    print(SAMPLE_TEXT)
    print("\nSummary:")
    for sentence in summarize(SAMPLE_TEXT, max_sentences=2):
        print(f"- {sentence}")


if __name__ == "__main__":
    main()
