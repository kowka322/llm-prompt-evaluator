
from collections import Counter


categories = ["spam", "question", "complaint", "request"]


def evaluate_case(answers: list[str], expected: str) -> dict:
    total = len(answers)
    counts = Counter(answers)
    accuracy = counts[expected] / total
    consistency = counts.most_common(1)[0][1] / total
    return {"accuracy": accuracy, "consistency": consistency}