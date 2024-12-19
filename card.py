import random
import pygame
import os


class Card:
    def __init__(self):
        self.__value = random.randint(0, 13)
        self.__color = random.randint(0, 3)
        self.__played = False
        self.__position = (0, 0)
        self.__rotation = random.randint(0, 360)

    def getValue(self):
        """
        Retrieve the value of the card.

        Returns:
            int: The value of the card.
        """
        return self.__value

    def getColor(self):
        """
        Returns the color of the card based on its value and color attributes.

        Returns:
            str: The color of the card. Possible values are "black", "blue", "red", "green", or "yellow".
        """
        if self.__value == 12 or self.__value == 13:
            return "black"
        elif self.__color == 0:
            return "blue"
        elif self.__color == 1:
            return "red"
        elif self.__color == 2:
            return "green"
        elif self.__color == 3:
            return "yellow"

    def __str__(self):
        """
        Returns a string representation of the card.

        The string representation is a tuple containing the card's value and color.

        Returns:
            str: A string representation of the card in the format (value, color).
        """
        return str((self.getValue(), self.getColor()))

    def select(self):
        """
        Check if the mouse cursor is within the bounds of the card.

        This method checks the current position of the mouse cursor and determines
        if it is within the rectangular area defined by the card's position and its
        dimensions (130x100 pixels).

        Returns:
            bool: True if the mouse cursor is within the card's bounds, False otherwise.
        """
        mouse_pos = pygame.mouse.get_pos()
        if (
            self.__position[0] < mouse_pos[0] < self.__position[0] + 130
            and self.__position[1] < mouse_pos[1] < self.__position[1] + 100
        ):
            return True
        return False

    def playable(self, pile_cards, update):
        """
        Determines if the card can be played on the current pile of cards.

        Args:
            pile_cards (list): The list of cards currently in the pile.
            update (bool): If True, updates the card's played status.

        Returns:
            bool: True if the card can be played, False otherwise.
        """
        if self.__played:
            return False
        if not pile_cards:
            return True
        last_card = pile_cards[-1]
        if (
            self.getValue() == last_card.getValue()
            or self.getColor() == last_card.getColor()
            or last_card.getColor() == "black"
            or self.getColor() == "black"
        ):
            if update:
                self.__played = True
            return True
        return False

    def displayCard(
        self,
        WIN,
        x,
        y,
        visible,
        CARD_BACK,
        BLUE_BASE,
        RED_BASE,
        GREEN_BASE,
        YELLOW_BASE,
        _0,
        _1,
        _2,
        _3,
        _4,
        _5,
        _6,
        _7,
        _8,
        _9,
        _draw2,
        _skip,
        _wild,
        _draw4,
    ):
        """
        Displays the card on the given window at the specified position.

        Parameters:
        self (Card): The card object.
        WIN (pygame.Surface): The window surface to draw the card on.
        x (int): The x-coordinate of the card's position.
        y (int): The y-coordinate of the card's position.
        visible (bool): Whether the card is visible or not.
        CARD_BACK (pygame.Surface): The image for the back of the card.
        BLUE_BASE (pygame.Surface): The base image for blue cards.
        RED_BASE (pygame.Surface): The base image for red cards.
        GREEN_BASE (pygame.Surface): The base image for green cards.
        YELLOW_BASE (pygame.Surface): The base image for yellow cards.
        _0 (pygame.Surface): The image for the card with value 0.
        _1 (pygame.Surface): The image for the card with value 1.
        _2 (pygame.Surface): The image for the card with value 2.
        _3 (pygame.Surface): The image for the card with value 3.
        _4 (pygame.Surface): The image for the card with value 4.
        _5 (pygame.Surface): The image for the card with value 5.
        _6 (pygame.Surface): The image for the card with value 6.
        _7 (pygame.Surface): The image for the card with value 7.
        _8 (pygame.Surface): The image for the card with value 8.
        _9 (pygame.Surface): The image for the card with value 9.
        _draw2 (pygame.Surface): The image for the draw 2 card.
        _skip (pygame.Surface): The image for the skip card.
        _wild (pygame.Surface): The image for the wild card.
        _draw4 (pygame.Surface): The image for the draw 4 card.
        """
        self.__position = (x, y)
        temp_img = CARD_BACK
        if self.getColor() == "blue":
            temp_img = BLUE_BASE
        elif self.getColor() == "red":
            temp_img = RED_BASE
        elif self.getColor() == "green":
            temp_img = GREEN_BASE
        elif self.getColor() == "yellow":
            temp_img = YELLOW_BASE
        if visible:
            img = temp_img
        else:
            img = CARD_BACK
        WIN.blit(img, (x, y))
        if self.getValue() == 0:
            temp_img = _0
        elif self.getValue() == 1:
            temp_img = _1
        elif self.getValue() == 2:
            temp_img = _2
        elif self.getValue() == 3:
            temp_img = _3
        elif self.getValue() == 4:
            temp_img = _4
        elif self.getValue() == 5:
            temp_img = _5
        elif self.getValue() == 6:
            temp_img = _6
        elif self.getValue() == 7:
            temp_img = _7
        elif self.getValue() == 8:
            temp_img = _8
        elif self.getValue() == 9:
            temp_img = _9
        elif self.getValue() == 10:
            temp_img = _draw2
        elif self.getValue() == 11:
            temp_img = _skip
        elif self.getValue() == 12:
            temp_img = _wild
        elif self.getValue() == 13:
            temp_img = _draw4
        if visible:
            img = temp_img
        else:
            img = CARD_BACK
        WIN.blit(img, (x, y))
