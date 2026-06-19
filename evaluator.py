from collections import Counter
from runner import run_repeats, parse_answer



def evaluate_case(answers: list[str], expected: str) -> dict:
    total = len(answers)
    counts = Counter(answers)
    accuracy = counts[expected] / total
    consistency = counts.most_common(1)[0][1] / total
    return {"accuracy": accuracy, "consistency": consistency}



def evaluate_prompt_case(template: str, case: dict) -> dict:
    text = case["text"]
    expected = case["expected"]
    raw = run_repeats(template, text)
    parsed = [parse_answer(r) for r in raw]
    return evaluate_case(parsed, expected)




def evaluate_prompt(template: str, cases: list[dict]) -> dict:
    accuracies = []
    consistencies = []
    for case in cases:
        result = evaluate_prompt_case(template, case)
        accuracies.append(result["accuracy"])
        consistencies.append(result["consistency"])
    avg_accuracy = sum(accuracies) / len(accuracies)
    avg_consistency = sum(consistencies) / len(consistencies)
    return {"accuracy": avg_accuracy, "consistency": avg_consistency}




def evaluate_all(prompts: dict, cases: list[dict]) -> dict:
    results = {}
    for name, template in prompts.items():
        results[name] = evaluate_prompt(template, cases)
    return results