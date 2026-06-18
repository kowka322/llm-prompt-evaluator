

PROMPTS = {
    "bare": (
        "Classify the following customer message into exactly one category: "
        "spam, question, complaint, or request.\n"
        "Answer with only one word, the category name in lowercase, nothing else.\n"
        "Message: {text}\n"
        "Category:"
    ),

    "definitions": (
        "Classify the following customer message into exactly one category.\n"
        "Categories:\n"
        "- spam: advertising, scams, or junk not related to support\n"
        "- question: the customer asks for information and expects an answer\n"
        "- complaint: the customer expresses dissatisfaction or files a grievance\n"
        "- request: the customer asks for an action to be done, without complaining\n"
        "Answer with only one word, the category name in lowercase, nothing else.\n"
        "Message: {text}\n"
        "Category:"
    ),

    "examples": (
        "Classify the following customer message into exactly one category: "
        "spam, question, complaint, or request.\n"
        "Examples:\n"
        "Message: how much does shipping cost? -> question\n"
        "Message: cancel my order now -> request\n"
        "Message: your support is awful, I want to file a claim -> complaint\n"
        "Message: WIN a free prize, click here -> spam\n"
        "Answer with only one word, the category name in lowercase, nothing else.\n"
        "Message: {text}\n"
        "Category:"
    ),
}