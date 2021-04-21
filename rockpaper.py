import random

def play():
 user = input("choose one : \n 'r' for rock \n 'p' paper \n 's' scissors \n")
 computer = random.choice(['r' ,'p' ,'s' ])

 if  user == computer:
  return 'tie!' 


 if win(user,computer):
  return 'won'
 
 return 'lost'



def win(player , opponent):
 if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'r'):
  return True
 
print(play())
