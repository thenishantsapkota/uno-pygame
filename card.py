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
        return self.__value

    def getColor(self):
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
        return str((self.getValue(), self.getColor()))

    def select(self):
        mouse_pos = pygame.mouse.get_pos()
        if (
            self.__position[0] < mouse_pos[0] < self.__position[0] + 130
            and self.__position[1] < mouse_pos[1] < self.__position[1] + 100
        ):
            return True
        return False

    def playable(self, pile_cards, update):
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
