import ollama

MODEL = "qwen3:8b"
CATEGORIES = ["spam", "question", "complaint", "request"]


def combine(template: str, text: str) -> str:
    return template.format(text=text)



def call_model(prompt: str) -> str:
    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    return response["message"]["content"]



def run_repeats(template:str, text:str, n: int=5) -> list[str]:
    prompt = combine(template,text)
    answers = []
    for i in range(n):
        answers.append(call_model(prompt))
    return answers


def parse_answer(raw: str) -> str:
    text = raw.lower().strip()
    text = text.replace("category:", "").strip()
    words = text.split()
    
    for word in reversed(words):
        cleaned = word.strip(".,!*")
        if cleaned in CATEGORIES:
            return cleaned
    return "unknown"

