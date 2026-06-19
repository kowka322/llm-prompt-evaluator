from collections import Counter
from runner import run_repeats, parse_answer



def evaluate_case(answers: list[str], expected: str) -> dict:
    total = len(answers)
    counts = Counter(answers)
    accuracy = counts[expected] / total
    consistency = counts.most_common(1)[0][1] / total
    return {"accuracy": accuracy, "consistency": consistency}



def evaluate_prompt_case(template: str, case: dict, n: int = 5) -> dict:
    text = case["text"]
    expected = case["expected"]
    raw = run_repeats(template, text, n)
    parsed = [parse_answer(r) for r in raw]
    return evaluate_case(parsed, expected)




def evaluate_prompt(template: str, cases: list[dict], n: int = 5) -> dict:
    accuracies = []
    consistencies = []
    case_results = []
    for case in cases:
        result = evaluate_prompt_case(template, case, n)
        accuracies.append(result["accuracy"])
        consistencies.append(result["consistency"])
        case_results.append({"text": case["text"], "expected": case["expected"], **result})
    avg_accuracy = sum(accuracies) / len(accuracies)
    avg_consistency = sum(consistencies) / len(consistencies)
    return {"accuracy": avg_accuracy, "consistency": avg_consistency, "cases": case_results}




def evaluate_all(prompts: dict, cases: list[dict], n: int = 5) -> dict:
    results = {}
    for name, template in prompts.items():
        results[name] = evaluate_prompt(template, cases, n)
    return results