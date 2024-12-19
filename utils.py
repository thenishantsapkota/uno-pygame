import pygame


def draw_window(
    WIN, BACKGROUND, DECK, player_hand, bot_hand, pile, VICTORY, DEFEAT, assets
):
    """
    Draws the game window with the current game state.

    Parameters:
    WIN (pygame.Surface): The main game window surface.
    BACKGROUND (pygame.Surface): The background image surface.
    DECK (pygame.Surface): The deck image surface.
    player_hand (list): List of cards in the player's hand.
    bot_hand (list): List of cards in the bot's hand.
    pile (list): List of cards in the pile.
    VICTORY (pygame.Surface): The victory image surface.
    DEFEAT (pygame.Surface): The defeat image surface.
    assets (dict): Dictionary containing various game assets.

    Returns:
    None
    """
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
    """
    Displays the player's and bot's hands on the game window.

    Args:
        WIN: The game window where the cards will be displayed.
        player_hand (list): A list of card objects representing the player's hand.
        bot_hand (list): A list of card objects representing the bot's hand.
        assets (tuple): A tuple containing assets required for displaying the cards.

    Returns:
        None
    """
    position = 1200 / 10
    for i in player_hand:
        i.displayCard(WIN, position, 700 - 120, True, *assets)
        position += 65
    position = 1200 / 10
    for j in bot_hand:
        j.displayCard(WIN, position, -105, False, *assets)
        position += 65


def display_pile(WIN, pile_cards, assets):
    """
    Displays the pile of cards on the given window.

    Args:
        WIN: The window or surface where the cards will be displayed.
        pile_cards (list): A list of card objects to be displayed.
        assets (tuple): Additional assets required for displaying the cards.

    Returns:
        None
    """
    if not pile_cards:
        return
    for i in pile_cards:
        i.displayCard(WIN, 500, 250, True, *assets)


def card_effect(card):
    """
    Determines the effect of a given card in the UNO game.

    Parameters:
    card (Card): The card object to evaluate. The card object should have a method getValue() that returns an integer value.

    Returns:
    int or None: Returns an integer representing the effect of the card if the card's value is between 10 and 13 inclusive.
                 Returns None if the card is a boolean value or if the card's value is not between 10 and 13.
    """
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
    """
    Determines the bot's turn by selecting a playable card from its hand.

    Args:
        hand (list): A list of card objects representing the bot's hand.
        pile_cards (list): A list of card objects representing the pile of cards on the table.

    Returns:
        card (object or bool): The first playable card object from the bot's hand if available, 
                               otherwise returns False if no playable card is found.
    """
    card = None
    for j in hand:
        if j.playable(pile_cards, False):
            card = j
    return card if card else False
