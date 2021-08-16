import random
from art import logo

print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player = random.choices(cards, k =2)
computer = random.choices (cards, k =2)

#adding the card's score
def add_score(side):
  current_score= 0
  for card in side:
    current_score+= card
  return current_score

add_score(player)
add_score(computer)

#Prints out the current status of each side's card
def current_status():
  print(f"Your Cards: {player}  Your score: {add_score(player)}")
  print(f"Computers Cards: {computer}  Computer's score: {add_score(computer)}")

current_status()

#function for another card
def another_card():
  global computer
  global player
  x = input("Do you want to draw another card? Type 'y' or 'n' ").lower()
  while x == 'y':
    player = player + random.choices (cards, k =1)
    add_score(player)
    current_status()
    if add_score(player) > 21:
      print("BUST !! You lose")
      break
    else:
      x = input("Do you want to draw another card? Type 'y' or 'n' ").lower()
    

  if add_score(player) < 21:
    while add_score(computer) < 17:
      computer = computer + random.choices (cards, k =1)
      add_score(computer)
      current_status()

  if add_score(computer) > 21:
    print("Compter Busted !! You win")
  else:
    if add_score(player) < 21:
      if add_score(player) > add_score(computer):
        print("You win")
      elif add_score(computer) == add_score(player):
        print("Draw")
      else:
        print("YOU LOSE")


#defining the games rules
if add_score(player) == 21:
  print("BlackJack !!! YOU won !!")
elif add_score(computer) == 21:
  print("Computer got BlackJack, You lose")
elif add_score(player) > 21:
  if cards[0] in player:
    player[player.index(11)] = 1
    if add_score(player) > 21:
      print("You Lose")
    else:
      another_card()
  else:
    print("You Lose")
else:
  another_card()


    




