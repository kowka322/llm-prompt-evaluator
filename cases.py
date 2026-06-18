
#all categories: spam, question, complaint, request.

TEST_CASES = [
    {"text": "how long does the delivery take?", "expected": "question"},
    {"text": "what are your allowed payment methods?", "expected": "question"},
    {"text": "when will I get a refund?", "expected": "question"},
    
    
    {"text": "set up another shipping address", "expected": "request"},
    {"text": "send me the invoice", "expected": "request"},
    {"text": "help me get a refund", "expected": "request"},
    
    
    {"text": "I am not happy with your work, lodge a complaint", "expected": "complaint"},
    {"text": "I'm not happy with your service help me to file a claim", "expected": "complaint"},
    
    
    {"text": "WIN a FREE iPhone now, click bit.ly/xxx", "expected": "spam"},
    {"text": "Make $5000 a week from home, DM me", "expected": "spam"},
    {"text": "Up to $500 Off Gaming Gear, celebrate Dads and Grads, shop now", "expected": "spam"},
    {"text": "Up to 56% Off Displays Built For Gaming, graduation sale, save now", "expected": "spam"},
]