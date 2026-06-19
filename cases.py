
#all categories: spam, question, complaint, request.

CASES = [
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
    
    
    
    
    #some tough questions
    
    
    {"text": "your delivery is late again, can you check where my order is", "expected": "request"},
    {"text": "I have been waiting two weeks, this is unacceptable, when will it arrive", "expected": "question"},
    {"text": "can you please cancel my order, the quality was terrible last time", "expected": "request"},
    {"text": "why does your app keep logging me out, fix this please", "expected": "request"},
    {"text": "I'd like to know if I can get my money back for this broken item", "expected": "question"},
    {"text": "great, another failed payment, how am I supposed to pay now", "expected": "complaint"},
    {"text": "please update my address, the old one keeps causing failed deliveries", "expected": "request"},
    {"text": "is there any way to speak to a real person, the bot is useless", "expected": "question"},
    {"text": "limited offer just for you, claim your reward before midnight", "expected": "spam"},
    {"text": "I sent three emails already and nobody replied, what is going on", "expected": "question"},

]