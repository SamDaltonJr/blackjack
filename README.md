# blackjack

## Overview

My application is a blackjack app that lets you play 1-on-1 with the dealer and gives the player recommendations based on the circumstances of the game.

## What is Blackjack?

Blackjack is a gambling card game in which players try to acquire cards with a face value as close as possible to twenty-one without going over. The game is played with a 52-card deck where suit does not matter.

### Rules

1. Blackjack may be played with one to eight decks of 52-card decks.
2. Aces may be counted as 1 or 11 points toward the player's total, numerical cards 2 to 9 are counted as their face value, and face cards and 10's both count as ten points.
3. The value of a hand is the total of the point values of the player's individual cards. The highest possible value without losing is "blackjack", which consists of an ace and any 10-point card.
4. The dealer and each player receive two cards for an initial deal, but the dealer only shows one card.
5. Once all initial hands have been dealt, the player has the following choices:
    - Stand: the player keeps their hand as is.
    - Hit: the player draws another card from the deck, and the player may hit so long as their total does not exceed 21.
    - Double-Down (not featured yet): the player doubles their bet and gets one, and only one, more card.
    - Split (not featured): If the player has two of the same cards upon the initial deal, then they may choose to double his bet and         split his cards into two individual hands.
6. After the player has had their turn, the dealer will reveal their hidden card. If the dealer has 16 or less, then they will draw another card.
7. If the player goes over 21 points from hitting, then the player busts.
8. If the dealer goes over 21 points, then the dealer busts.
9. If the dealer does not bust, then the higher point total between the player and the dealer will win


## Features

### Live

- Basic game of blackjack where the user has a choice of [H]it, [S]tand, or [Q].
- Simulates a real deck of cards using a python list, that's shuffled between every hand.
- Gives a recommendation to the user on whether they should hit or stand.

### In Progress

- Multiple decks of cards and no shuffling between each hand until the deck is nearly empty.
- Counting cards as to help the user decide if the deck is favorable to them or the dealer.

### Future

- Add a chip total for players to place bets with
- Switching from command line to webpage interface to play
- Add multiple players
