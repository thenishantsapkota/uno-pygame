import pygame


def draw_window(
    WIN, BACKGROUND, DECK, player_hand, bot_hand, pile, VICTORY, DEFEAT, assets
):
    WIN.blit(BACKGROUND, (0, 0))
    WIN.blit(DECK, (1000, 250))  
    display_pile(WIN, pile, assets)
    display_hand(WIN, player_hand, bot_hand, assets)
    if not player_hand:
        WIN.blit(VICTORY, (400, 200))  
    if not bot_hand:
        WIN.blit(DEFEAT, (400, 200))  
    pygame.display.update()


def display_hand(WIN, player_hand, bot_hand, assets):
    position = 1200 / 10 
    for i in player_hand:
        i.displayCard(WIN, position, 700 - 120, True, *assets)
        position += 65
    position = 1200 / 10  
    for j in bot_hand:
        j.displayCard(WIN, position, -105, False, *assets)
        position += 65


def display_pile(WIN, pile_cards, assets):
    if not pile_cards:
        return
    for i in pile_cards:
        i.displayCard(
            WIN, 500, 250, True, *assets
        )  


def card_effect(card):
    if card in [True, False]:
        return
    if card.getValue() == 10:
        return 1
    if card.getValue() == 11:
        return 2
    if card.getValue() == 12:
        return 3
    if card.getValue() == 13:
        return 4


def bot_turn(hand, pile_cards):
    card = None
    for j in hand:
        if j.playable(pile_cards, False):
            card = j
    return card if card else False
