import random

def computer_guess(x):
 low = 1
 high = x
 
 feedback = ''

 while(feedback != 'c') :
  




  if low !=high:
   random_num = random.randint(low ,high)
  else:
   print(f"{low} is your number") 

  print(f"is {random_num} is your number")
  feedback = input("Is it high (h) low (l) or correct(c) : ")
  if feedback == 'h' :
   high = random_num - 1
  if feedback == 'l' :
   low = random_num + 1


 print(f"Computer guessed it .your number is {random_num}")  





computer_guess(1000)