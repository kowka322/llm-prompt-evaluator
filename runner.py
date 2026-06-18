import cases
import prompts
import ollama

def combine(template: str, text: str) -> str:
    return template.format(text=text)



def call_model(prompt: str) -> str:
    response = ollama.chat(
        model="qwen3:8b",
        messages=[{"role": "user", "content": prompt}],
    )
    return response["message"]["content"]



def run_repeats(template:str, text:str, n: int=5) -> list[str]:
    prompt = combine(template,text)
    answers = []
    for i in range(n):
        answers.append(call_model(prompt))
    return answers