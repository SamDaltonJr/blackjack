#import library
import pygame 
from pygame.locals import *
import random
import copy



#load images
icon = pygame.image.load('resources/icon.png')
cBack = pygame.image.load('resources/cards/cardback.png')
diamondA = pygame.image.load('resources/cards/ad.png')
clubA = pygame.image.load('resources/cards/ac.png')
heartA = pygame.image.load('resources/cards/ah.png')
spadeA = pygame.image.load('resources/cards/as.png')
diamond2 = pygame.image.load('resources/cards/2d.png')
club2 = pygame.image.load('resources/cards/2c.png')
heart2 = pygame.image.load('resources/cards/2h.png')
spade2 = pygame.image.load('resources/cards/2s.png')
diamond3 = pygame.image.load('resources/cards/3d.png')
club3 = pygame.image.load('resources/cards/3c.png')
heart3 = pygame.image.load('resources/cards/3h.png')
spade3 = pygame.image.load('resources/cards/3s.png')
diamond4 = pygame.image.load('resources/cards/4d.png')
club4 = pygame.image.load('resources/cards/4c.png')
heart4 = pygame.image.load('resources/cards/4h.png')
spade4 = pygame.image.load('resources/cards/4s.png')
diamond5 = pygame.image.load('resources/cards/5d.png')
club5 = pygame.image.load('resources/cards/5c.png')
heart5 = pygame.image.load('resources/cards/5h.png')
spade5 = pygame.image.load('resources/cards/5s.png')
diamond6 = pygame.image.load('resources/cards/6d.png')
club6 = pygame.image.load('resources/cards/6c.png')
heart6 = pygame.image.load('resources/cards/6h.png')
spade6 = pygame.image.load('resources/cards/6s.png')
diamond7 = pygame.image.load('resources/cards/7d.png')
club7 = pygame.image.load('resources/cards/7c.png')
heart7 = pygame.image.load('resources/cards/7h.png')
spade7 = pygame.image.load('resources/cards/7s.png')
diamond8 = pygame.image.load('resources/cards/8d.png')
club8 = pygame.image.load('resources/cards/8c.png')
heart8 = pygame.image.load('resources/cards/8h.png')
spade8 = pygame.image.load('resources/cards/8s.png')
diamond9 = pygame.image.load('resources/cards/9d.png')
club9 = pygame.image.load('resources/cards/9c.png')
heart9 = pygame.image.load('resources/cards/9h.png')
spade9 = pygame.image.load('resources/cards/9s.png')
diamond10 = pygame.image.load('resources/cards/10d.png')
club10 = pygame.image.load('resources/cards/10c.png')
heart10 = pygame.image.load('resources/cards/10h.png')
spade10 = pygame.image.load('resources/cards/10s.png')
diamondJ = pygame.image.load('resources/cards/jd.png')
clubJ = pygame.image.load('resources/cards/jc.png')
heartJ = pygame.image.load('resources/cards/jh.png')
spadeJ = pygame.image.load('resources/cards/js.png')
diamondQ = pygame.image.load('resources/cards/qd.png')
clubQ = pygame.image.load('resources/cards/qc.png')
heartQ = pygame.image.load('resources/cards/qh.png')
spadeQ = pygame.image.load('resources/cards/qs.png')
diamondK = pygame.image.load('resources/cards/kd.png')
clubK = pygame.image.load('resources/cards/kc.png')
heartK = pygame.image.load('resources/cards/kh.png')
spadeK = pygame.image.load('resources/cards/ks.png')

pygame.display.set_icon(icon)

#Global constants - colors, sets of cards
black = (0,0,0)
white = (255,255,255)
gray = (192,192,192)

cards = [ diamondA, clubA, heartA, spadeA, \
          diamond2, club2, heart2, spade2, \
          diamond3, club3, heart3, spade3, \
          diamond4, club4, heart4, spade4, \
          diamond5, club5, heart5, spade5, \
          diamond6, club6, heart6, spade6, \
          diamond7, club7, heart7, spade7, \
          diamond8, club8, heart8, spade8, \
          diamond9, club9, heart9, spade9, \
          diamond10, club10, heart10, spade10, \
          diamondJ, clubJ, heartJ, spadeJ, \
          diamondQ, clubQ, heartQ, spadeQ, \
          diamondK, clubK, heartK, spadeK ]

cardA = [ diamondA, clubA, heartA, spadeA ]
card2 = [ diamond2, club2, heart2, spade2 ]
card3 = [ diamond3, club3, heart3, spade3 ]
card4 = [ diamond4, club4, heart4, spade4 ]
card5 = [ diamond5, club5, heart5, spade5 ]
card6 = [ diamond6, club6, heart6, spade6 ]
card7 = [ diamond7, club7, heart7, spade7 ]
card8 = [ diamond8, club8, heart8, spade8 ]
card9 = [ diamond9, club9, heart9, spade9 ]
card10 = [ diamond10, club10, heart10, spade10, \
            diamondJ, clubJ, heartJ, spadeJ, \
            diamondQ, clubQ, heartQ, spadeQ, \
            diamondK, clubK, heartK, spadeK ]


def shuffle(deck):
  return deck.shuffle(deck)

def dealCard(deck, xList):
  cA = 0
  card = deck.pop()
  xList.append(card)
  if card in cardA:
    cA = 1
  return card, cA

def getAmount(card):
  if card in cardA: return 11
  if card in card2: return 2
  if card in card3: return 3
  if card in card4: return 4
  if card in card5: return 5
  if card in card6: return 6
  if card in card7: return 7
  if card in card8: return 8
  if card in card9: return 9
  if card in card10: return 10
  else:
    print('getAmount broke')
    exit()

def getTotal(hand):
  total = 0
  value = 0
  for card in hand:
    value = getAmount(card)
    if value < 11:
      total += value
    elif value == 11:
      if total >= 11: total +=1
      else: total += 11
  return total


def initGame(cList, uList, dList):
  userA = 0
  dealA = 0
  discard(cList)
  card1, cA = dealCard(cList, uList)
  userA += cA
  card2, cA = dealCard(cList, dList)
  dealA += cA
  card3, cA = dealCard(cList, uList)
  userA += cA
  card4, cA = dealCard(cList, dList)
  dealA += cA
  dealerHand = [card2, card4]
  userHand = [card1, card3]
  return getTotal(userHand), userA, getTotal(dealerHand), dealA

def discard(deck):
  deck.pop()

def recommendation(dealer_hand, user_hand):
  feedback = ''
  card = dealer_hand[0]
  value = getAmount(card)
  player_total = getTotal(user_hand)
  if player_total > 16 or (player_total > 12 and value <7) or (player_total == 12 and value > 3 and value <7):
    feedback = 'You should stand'
  else:
    feedback = 'You should hit'
  return feedback


def main():
  #local variables
  deck = copy.copy(cards)
  random.shuffle(deck)
  original_deck_len = len(deck)
  stand = False
  user_hand = []
  dealer_hand = []
  winNum = 0
  loseNum = 0
  feedback = ''
  cardCount = 0


  #init game
  pygame.init()
  screen = pygame.display.set_mode((640,480))
  pygame.display.set_caption('Blackjack Card Counter')
  font = pygame.font.SysFont('arial', 15)
  hitTxt = font.render('Hit', 1, black)
  standTxt = font.render('Stand', 1, black)
  restartTxt = font.render('Restart', 1, black)
  gameoverTxt = font.render('GAME OVER', 1, white)
  feedbackTxt = font.render(feedback, 1, white)
  userSum, userA, dealSum, dealA = initGame(deck, user_hand, dealer_hand)

  #fill background
  background = pygame.Surface(screen.get_size())
  background = background.convert()
  background.fill((60,115,10))
  hitB = pygame.draw.rect(background, gray, (10, 445, 75, 25))
  standB = pygame.draw.rect(background, gray, (95, 445, 75, 25))
  ratioB = pygame.draw.rect(background, gray, (555, 420, 75, 50))

  #event loop
  while True:
    #check if game is over
    gameover = True if (userSum >= 21 and userA ==0) or len(user_hand) == 5 else False
    if len(user_hand) == 2 and userSum == 21:
      gameover = True
    elif len(dealer_hand) == 2 and dealSum == 21:
      gameover = True

    #background update for wins and losses
    winTxt = font.render('Wins: %i' % winNum, 1, black)
    loseTxt = font.render('Losses: %i' %loseNum, 1, black)


    #event listener on buttons
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
      elif event.type == pygame.MOUSEBUTTONDOWN and not (gameover or stand) and hitB.collidepoint(pygame.mouse.get_pos()):
        #hit and give player card, so long as player doesn't break blackjack rules
        card, cA = dealCard(deck, user_hand)
        userA += cA
        userSum = getTotal(user_hand)
        print('User %i' % userSum)
      elif event.type == pygame.MOUSEBUTTONDOWN and not gameover and standB.collidepoint(pygame.mouse.get_pos()):
        #when player stands, the dealer  plays
        stand = True
        while dealSum<= userSum and dealSum < 17:
          card, cA = dealCard(deck, dealer_hand)
          dealA += cA
          dealSum = getTotal(dealer_hand)
          print('Dealer: %i' % dealSum)
      elif event.type == pygame.MOUSEBUTTONDOWN and (gameover or stand) and restartB.collidepoint(pygame.mouse.get_pos()):
        if userSum == dealSum:
          pass
        elif userSum <= 21 and len(user_hand) == 5:
          winNum += 1
        elif userSum <= 21 and dealSum < userSum or dealSum > 21:
          winNum += 1
        else:
          loseNum += 1
        gameover = False
        stand = False
        user_hand = []
        dealer_hand = []
        if len(deck) <=10:
          print('Shuffling deck')
          deck = copy.copy(cards)
          random.shuffle(deck)
        userSum, userA, dealSum, dealA = initGame(deck, user_hand, dealer_hand)
        restartB = pygame.draw.rect(background, (60,115,10),(270,225,75,25))
    
    screen.blit(background, (0,0))
    screen.blit(hitTxt, (39, 448))
    screen.blit(standTxt, (116, 448))
    screen.blit(winTxt, (565, 423))
    screen.blit(loseTxt, (565,448))

    for card in dealer_hand:
      x = 10 + dealer_hand.index(card)*110
      screen.blit(card, (x,10))
    screen.blit(cBack, (120, 10))

    for card in user_hand:
      x = 10 + user_hand.index(card)*110
      screen.blit(card, (x, 295))

    if gameover or stand:
      screen.blit(gameoverTxt, (270, 200))
      restartB = pygame.draw.rect(background, gray, (270,225,75, 25))
      screen.blit(restartTxt, (287, 228))
      screen.blit(dealer_hand[1], (120, 10))
    
    pygame.display.update()







if __name__ == '__main__':
    main()