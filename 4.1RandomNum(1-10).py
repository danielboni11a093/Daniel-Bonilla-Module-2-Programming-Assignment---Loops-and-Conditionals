import random

secret = random.randint(1,10)
num_guess = 0
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    num_guess += 1
    
    if guess == secret:
        print("Just Right")
        break
    elif guess < secret:
        print("Too Low")
    else:
        print("Too High")
        
print(f'Got it in {num_guess} tries!')
   
        