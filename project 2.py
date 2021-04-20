# the guesssing game
# user guessing

import random

def numberguess(x):
 random_num = random.randint(1,x)
 

 guess = 0

 while(guess != random_num):
  guess = int(input(f"Guess a number between 1 & {x}: "))
  if guess<random_num:
   print("LOW")
  if guess>random_num:
   print("HIGH")
 print("success")



numberguess(10)
