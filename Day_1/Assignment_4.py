import random

words = ["python", "java", "hello", "function", "program"]
word = random.choice(words)

# Scramble the word
scramble = "".join(random.sample(word, len(word)))

print("Scrambled word is:", scramble)

chances = 3
score=0

while chances>0:
    guess=input("Enter your guess word:")
    if guess==word:
     score+=1
    print("Correct answer")
    print("Score:",score)
    break
else:
    chances-=1
print("Wrong answer,chances left:",chances)

