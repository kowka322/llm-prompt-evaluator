from cases import CASES
from prompts import PROMPTS
from evaluator import evaluate_all

if __name__ == "__main__":
    results = evaluate_all(PROMPTS,CASES)
    for name, scores in results.items():
        acc = scores["accuracy"]
        cons = scores["consistency"]
        print(f"{name}: accuracy={acc:.2f}, consistency={cons:.2f}")