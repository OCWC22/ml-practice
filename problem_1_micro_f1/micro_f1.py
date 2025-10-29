"""Micro-F1 score helper.

This module keeps the implementation intentionally small and
easy-to-review while adding plain-language guidance for readers
without a machine-learning background, per project guidelines.
"""

from typing import Sequence


def micro_f1(y_true: Sequence[int], y_pred: Sequence[int]) -> float:
    """Compute the micro-averaged F1 score for single-label multi-class data.

    Args:
        y_true: The actual labels (think: the answer key).
        y_pred: The predicted labels (think: the model's guesses).

    Returns:
        A Python float between 0.0 and 1.0 representing the micro-F1 score.

    Raises:
        ValueError: If the input sequences are different lengths or empty.
    """

    # Step 1 — Vocabulary so a non-technical leader can follow along:
    # "F1 score" is a single number that balances two business-centric ideas:
    #   • Precision → Of the things we predicted as "positive", how many were right?
    #   • Recall    → Of the actual positives that existed, how many did we catch?
    # "Micro" means we total every success and miss across all categories before
    # doing the math, so common categories naturally carry more weight.

    if len(y_true) != len(y_pred):
        raise ValueError("y_true and y_pred must be the same length")

    if not y_true:
        raise ValueError("Micro-F1 is undefined for empty inputs")

    # Step 2 — Translate inputs into everyday language so intent is clear:
    # y_true = ground-truth answers (what really happened).
    # y_pred = our system's guesses (what we thought would happen).
    # We'll now count outcomes item by item.
    true_positive_count = 0
    mismatch_count = 0

    for actual, predicted in zip(y_true, y_pred):
        # Step 3 — Define what counts as a "true positive":
        # When the guess matches reality, we record a success.
        if actual == predicted:
            true_positive_count += 1
        else:
            # Step 4 — Every mismatch means two things:
            #   • We wrongly claimed something (a "false positive").
            #   • We missed the real answer (a "false negative").
            mismatch_count += 1

    # Step 5 — Convert the counts into the classic F1 math:
    false_positive_count = mismatch_count
    false_negative_count = mismatch_count

    # Step 6 — Carry out the F1 formula while guarding against division by zero.
    denominator = (2 * true_positive_count +
                   false_positive_count +
                   false_negative_count)

    if denominator == 0:
        # This only happens when no positives were predicted or observed.
        return 0.0

    # Step 7 — Compute and return the final score as a plain Python float.
    return float((2 * true_positive_count) / denominator)


__all__ = ["micro_f1"]


if __name__ == "__main__":  # pragma: no cover - manual smoke test only
    # Manual verification flow (requested): run `python -m problem_1_micro_f1.micro_f1`
    # Expected console output:
    # Scenario 1 – Partial match (2 correct of 3): 0.6666667
    # Scenario 2 – Perfect match (4 correct of 4): 1.0000000
    # Scenario 3 – Three correct of four:         0.7500000
    demo_cases = [
        ("Scenario 1 – Partial match (2 correct of 3)", [0, 1, 1], [0, 1, 0]),
        ("Scenario 2 – Perfect match (4 correct of 4)", [0, 1, 2, 2], [0, 1, 2, 2]),
        ("Scenario 3 – Three correct of four", [2, 2, 1, 0], [1, 2, 1, 0]),
    ]

    for label, truth, guess in demo_cases:
        score = micro_f1(truth, guess)
        print(f"{label}: {score:.7f}")
