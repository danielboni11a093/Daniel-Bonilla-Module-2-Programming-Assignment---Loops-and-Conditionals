import random

guess_me = random.randint(1,10)

while True:
    number = int(input("Guess a number between 1 and 10: "))
    
    if number == guess_me:
        print("Just Right")
        break
    elif number < guess_me:
        print("Too Low")
    else:
        print("Too High")
        
        
   
        