import random

words = ["python", "cpp", "java", "html", "coding", "hello", "deepak", "namaste"]


word = random.choice(words)

guessed = []
attempt = 6
len_word = len(word)
print("Welcome to hangman Game!")

while attempt > 0 :
    
    display = ""
    
    for letter in word:
        if letter in guessed :
            display += letter
        else:
            display += "_"
    
    print("Word:",display)
    
    if display == word:
        print("Congratulations! you guessed the correct word.")
        break
    
        
            
    guess = input("Enter the letter: ").lower()
    
    if guess in word:
        guessed.append(guess)
        print("correct guess!")
    
    elif guess in guessed:
        print("you already guess!")
        
    else: 
        guessed.append(guess)
        attempt -= 1
        
        print("worng guess! attemped left :",attempt)

if attempt == 0:
    print("Game Over! The word was:",word)

        
    
        