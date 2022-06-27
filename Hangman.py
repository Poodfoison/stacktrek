from random import choice
from threading import Thread
from time import *

words = ["negative", "channel", "lamb", "pension", "dorm", "statement", "sensitive", "lean", "suitcase", "research", "attack"]
word = choice(words)
lettersguessed = ""
word_completion = "_ " * len(word)
wrong = 6

print(f"H A N G M A N \nYou have 30 seconds to guess the word?")
print(f"{word_completion} ")

#for the timer 
def countdown ():
    global timer 

    timer = 30

    for x in range(30):
        timer = timer - 1
        sleep (1)

    print("\nTime is up!")

count = Thread(target=countdown)
count.start()

while timer > 0:

    while wrong > 0:
        
        guess = input("Enter letter:")
    
        if guess in word:
            print(f"Correct! There is {guess} in the word")
        else:
            wrong -= 1
            print(f"Incorrect. There is no {guess} in the word. {wrong} turn(s) left")

        lettersguessed = lettersguessed + guess
        wrongcount = 0

        for letter in  word:
            if  letter in lettersguessed:
                print(f"{letter}", end=" ")
            else:
                print("_", end=" ")
                wrongcount +=1

        print("")
        #end of the timer
        if timer == 0:
            break

        if wrongcount == 0:
            print (f"Congratulation! The word is {word}")
            break
        
    else:
        print(f"The word was {word}. Try Again")
        break