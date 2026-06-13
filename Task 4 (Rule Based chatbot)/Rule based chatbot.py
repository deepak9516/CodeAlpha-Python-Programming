print("Bot: Hey dude! What's going on? 😄")

answers = {
    "good": " Thats sounds great! You wants to ask something?",
    
    "ml": "machine learning means a computer learn pattern from data and make decisions or prediction without being explicitly programmed for every task.",
    
    "machine learning": "machine learning means a computer learn pattern from data and make decisions or prediction without being explicitly programmed for every task.",
    
    "ai": "artificial intelligence is a technology that allows machine to think, learn, and make decision like humans. ",
    
    "artificial intelligence" : "artificial intelligence is a technology that allows machine to think, learn, and make decision like humans. ",
    
    "cn" : "A computer network is a system of interconnected computers and devices that act as a medium to transmit data between a local computer and the wider network, and vice-versa.",
    
    "computer network" : "A computer network is a system of interconnected computers and devices that act as a medium to transmit data between a local computer and the wider network, and vice-versa.",
    
    "quiz" : "nice, if you want to play then type any no. form 1 to 6.",
    
    "thank": "Most Welcome "
    
}

Quiz = {
    "1" : '''What is the output of:
print(type(5))''',
"2" : '''Which loop runs until condition becomes false?''',
"3" : '''Which keyword is used to create a function in Python?''',
"4" : '''What does ML stand for?''',
"5" : '''Which language is most used in AI?''',
"6" : '''Which library is used for numerical computing in Python?'''
}
Quiz_ans = {
    "1": "<class 'int'>",
    "2": "while loop",
    "3": "def",
    "4": "machine learning",
    "5": "python",
    "6": "NumPy"
}
marks = 0

# for general talk
def chatbot_response(user):
    for key in answers:
        if key in user:
            return answers[key]
    return None

# for quiz
def ask_quiz(user):
    global marks
    
    print("Bot:", Quiz[user])
    
    user_ans = input("your answer: ").lower()
    
    correct_ans = Quiz_ans[user].lower()

    if user_ans == correct_ans:
        marks += 1
        print("Bot: Correct ans ✅")
        print("Bot: Marks is:",marks)
    
    else:
        print("Bot: Worng ans ❌")
        print("Bot: Correct ans is:",correct_ans)
        
while True:
    user = input("You: ").lower()

    if user == "bye":
        print("Bot: goodbye! bro...")
        break

    found = True
    
    # quiz start
    if user in Quiz:
        
        ask_quiz(user)
        found = True
    else:
        response = chatbot_response(user)
        
        if response:
            print("Bot:",response)
            found = True

    if not found:
        print("Bot: sorry,I did not understand what you said!")
        
        