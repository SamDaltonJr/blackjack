import os
import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

def deal(deck):
  hand = []
  for i in range(2):
    card = deck.pop()
    if card == 11:card = "J"
    if card == 12:card = "Q"
    if card == 13:card = "K"
    if card == 14:card = "A"
    hand.append(card)
  return hand

def shuffle(deck):
  random.shuffle(deck)
  return deck

def discard(deck):
  deck.pop()
  return deck

def play_again():
  again = input("Do you want to play again? (Y/N) : ").lower()
  if again == "y":
    dealer_hand = []
    player_hand = []
    deck = [2,3,4,5,6,7,8,9,10,11,12,13,14]*4
    game()
  else:
    print("Bye!")
    exit()


def total(hand):
    total = 0
    for card in hand:
	    if card == "J" or card == "Q" or card == "K":
	        total+= 10
	    elif card == "A":
	        if total >= 11: total+= 1
	        else: total+= 11
	    else: total += card
    return total

def hit(hand):
	card = deck.pop()
	if card == 11:card = "J"
	if card == 12:card = "Q"
	if card == 13:card = "K"
	if card == 14:card = "A"
	hand.append(card)
	return hand

def clear():
	if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')

def recommendation(dealer_hand, player_hand):
  card = dealer_hand[0]
  if card == "J" or card == "Q" or card == "K" or card =="A":card=10
  player_total = total(player_hand)
  if player_total > 16:
    print('You should stand.')
  elif player_total > 12 and card < 7:
    print('You should stand.')
  elif player_total < 12:
    print('You should hit.')
  elif player_total < 17 and card > 6:
    print('You should hit.')
  elif player_total == 12 and card > 3 and card < 7:
    print('You should stand.')
  else:
    print('You should hit.')

def print_results(dealer_hand, player_hand):
	clear()
	print ("The dealer has a " + str(dealer_hand) + " for a total of " + str(total(dealer_hand)))
	print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))

def blackjack(dealer_hand, player_hand):
	if total(player_hand) == 21:
		print_results(dealer_hand, player_hand)
		print ("Congratulations! You got a Blackjack!\n")
		play_again()
	elif total(dealer_hand) == 21:
		print_results(dealer_hand, player_hand)		
		print ("Sorry, you lose. The dealer got a blackjack.\n")
		play_again()

def count_cards(dealer_hand, player_hand):
  count = 0
  hands = dealer_hand + player_hand
  for card in hands:
    if card == "J" or card == "Q" or card == "K" or card =="A":card=10
    if card < 6: count+=1
    elif card >= 10: count-=1
  print("The current count is " + str(count))


def score(dealer_hand, player_hand):
  if total(player_hand) == 21:
	  print_results(dealer_hand, player_hand)
	  print("Congratulations! You got a Blackjack!\n")
  elif total(dealer_hand) == 21:
	  print_results(dealer_hand, player_hand)		
	  print ("Sorry, you lose. The dealer got a blackjack.\n")
  elif total(player_hand) > 21:
	  print_results(dealer_hand, player_hand)
	  print ("Sorry. You busted. You lose.\n")
  elif total(dealer_hand) > 21:
    print_results(dealer_hand, player_hand)
    print ("Dealer busts. You win!\n")
  elif total(player_hand) < total(dealer_hand):
    print_results(dealer_hand, player_hand)
    print("Sorry. Your score isn't higher than the dealer. You lose\n")
  elif total(player_hand) > total(dealer_hand):
	  print_results(dealer_hand, player_hand)			   
	  print ("Congratulations. Your score is higher than the dealer. You win\n")



def game():
  choice = 0
  clear()
  print("WELCOME TO BLACKJACK!\n")
  live_deck = shuffle(deck)
  print(live_deck)
  discard(live_deck)
  print(live_deck)
  dealer_hand = deal(live_deck)
  print(live_deck)
  player_hand = deal(live_deck)
  print(live_deck)
  keep_hitting = True
  while choice != "q":
    while total(player_hand) < 21 and keep_hitting:
      print("The dealer is showing a " + str(dealer_hand[0]))
      print("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
      blackjack(dealer_hand, player_hand)
      recommendation(dealer_hand, player_hand)
      choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
      clear()
      if choice == "h":
        hit(player_hand)
      elif choice == "s":
        keep_hitting = False
      elif choice == "q":
        print("Bye!")
        exit()
    while total(dealer_hand) < 17:
      hit(dealer_hand)
    score(dealer_hand, player_hand)
    count_cards(dealer_hand, player_hand)
    play_again()

    

if __name__ == "__main__":
    game()
