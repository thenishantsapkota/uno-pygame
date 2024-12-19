import pygame
import random
import os
from card import Card
from utils import draw_window, card_effect, bot_turn


class Game:
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 1200, 700 
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("UNO!")
        self.FPS = 120
        self.STARTING_HAND = 8
        self.BOT_STARTING_HAND = 8
        self.PILE_X, self.PILE_Y = 500, 250 
        self.DECK_X, self.DECK_Y = 1000, 250  
        self.load_assets()
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_over = False
        self.pile_cards = []
        self.hand = []
        self.bot_hand = []
        for i in range(self.STARTING_HAND):
            self.hand.append(Card())
        for j in range(self.BOT_STARTING_HAND):
            self.bot_hand.append(Card())

    def load_assets(self):
        """
        Loads all the game assets such as images for the background, deck, victory, defeat, card backs, 
        and various card faces into the game. The loaded images are stored as attributes of the class 
        instance and also in a list called 'assets' for easy access.

        Attributes:
            BACKGROUND (pygame.Surface): The background image of the game.
            DECK_IMAGE (pygame.Surface): The image of the deck.
            DECK (pygame.Surface): The scaled image of the deck.
            VICTORY (pygame.Surface): The image displayed upon victory.
            DEFEAT (pygame.Surface): The image displayed upon defeat.
            CARD_BACK (pygame.Surface): The image of the back of a card.
            BLUE_BASE (pygame.Surface): The image of the blue base card.
            RED_BASE (pygame.Surface): The image of the red base card.
            GREEN_BASE (pygame.Surface): The image of the green base card.
            YELLOW_BASE (pygame.Surface): The image of the yellow base card.
            _0 (pygame.Surface): The image of the card with number 0.
            _1 (pygame.Surface): The image of the card with number 1.
            _2 (pygame.Surface): The image of the card with number 2.
            _3 (pygame.Surface): The image of the card with number 3.
            _4 (pygame.Surface): The image of the card with number 4.
            _5 (pygame.Surface): The image of the card with number 5.
            _6 (pygame.Surface): The image of the card with number 6.
            _7 (pygame.Surface): The image of the card with number 7.
            _8 (pygame.Surface): The image of the card with number 8.
            _9 (pygame.Surface): The image of the card with number 9.
            _draw2 (pygame.Surface): The image of the draw 2 card.
            _skip (pygame.Surface): The image of the skip card.
            _wild (pygame.Surface): The image of the wild card.
            _draw4 (pygame.Surface): The image of the wild draw 4 card.
            assets (list): A list containing all the loaded card images.
        """
        self.BACKGROUND = pygame.image.load(os.path.join("assets", "background.png"))
        self.DECK_IMAGE = pygame.image.load(os.path.join("assets", "deck.png"))
        self.DECK = pygame.transform.scale(self.DECK_IMAGE, (150, 180))
        self.VICTORY = pygame.image.load(os.path.join("assets", "victory.png"))
        self.DEFEAT = pygame.image.load(os.path.join("assets", "defeat.png"))
        self.CARD_BACK = pygame.image.load(os.path.join("assets", "back.png"))
        self.BLUE_BASE = pygame.image.load(os.path.join("assets", "blue_base.png"))
        self.RED_BASE = pygame.image.load(os.path.join("assets", "red_base.png"))
        self.GREEN_BASE = pygame.image.load(os.path.join("assets", "green_base.png"))
        self.YELLOW_BASE = pygame.image.load(os.path.join("assets", "yellow_base.png"))
        self._0 = pygame.image.load(os.path.join("assets", "_0.png"))
        self._1 = pygame.image.load(os.path.join("assets", "_1.png"))
        self._2 = pygame.image.load(os.path.join("assets", "_2.png"))
        self._3 = pygame.image.load(os.path.join("assets", "_3.png"))
        self._4 = pygame.image.load(os.path.join("assets", "_4.png"))
        self._5 = pygame.image.load(os.path.join("assets", "_5.png"))
        self._6 = pygame.image.load(os.path.join("assets", "_6.png"))
        self._7 = pygame.image.load(os.path.join("assets", "_7.png"))
        self._8 = pygame.image.load(os.path.join("assets", "_8.png"))
        self._9 = pygame.image.load(os.path.join("assets", "_9.png"))
        self._draw2 = pygame.image.load(os.path.join("assets", "_draw2.png"))
        self._skip = pygame.image.load(os.path.join("assets", "_skip.png"))
        self._wild = pygame.image.load(os.path.join("assets", "_wild.png"))
        self._draw4 = pygame.image.load(os.path.join("assets", "_wild_draw.png"))
        self.assets = [
            self.CARD_BACK,
            self.BLUE_BASE,
            self.RED_BASE,
            self.GREEN_BASE,
            self.YELLOW_BASE,
            self._0,
            self._1,
            self._2,
            self._3,
            self._4,
            self._5,
            self._6,
            self._7,
            self._8,
            self._9,
            self._draw2,
            self._skip,
            self._wild,
            self._draw4,
        ]

    def animate_card(self, card, start_pos, end_pos, duration=500):
        """
        Animates the movement of a card from a starting position to an ending position over a specified duration.

        Args:
            card (Card): The card object to be animated.
            start_pos (tuple): The starting (x, y) position of the card.
            end_pos (tuple): The ending (x, y) position of the card.
            duration (int, optional): The duration of the animation in milliseconds. Defaults to 500.

        Returns:
            None
        """
        start_time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start_time < duration:
            t = (pygame.time.get_ticks() - start_time) / duration
            current_x = start_pos[0] + t * (end_pos[0] - start_pos[0])
            current_y = start_pos[1] + t * (end_pos[1] - start_pos[1])
            draw_window(
                self.WIN,
                self.BACKGROUND,
                self.DECK,
                self.hand,
                self.bot_hand,
                self.pile_cards,
                self.VICTORY,
                self.DEFEAT,
                self.assets,
            )
            card.displayCard(self.WIN, current_x, current_y, True, *self.assets)
            pygame.display.update()
            self.clock.tick(self.FPS)
        card._Card__position = end_pos  

    def animate_draw_card(self, card, end_pos, duration=500):
        """
        Animates the drawing of a card from the deck to a specified position.

        Args:
            card (Card): The card object to be drawn.
            end_pos (tuple): The (x, y) coordinates where the card should end up.
            duration (int, optional): The duration of the animation in milliseconds. Defaults to 500.

        Returns:
            None
        """
        start_pos = (self.DECK_X, self.DECK_Y)
        start_time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start_time < duration:
            t = (pygame.time.get_ticks() - start_time) / duration
            current_x = start_pos[0] + t * (end_pos[0] - start_pos[0])
            current_y = start_pos[1] + t * (end_pos[1] - start_pos[1])
            draw_window(
                self.WIN,
                self.BACKGROUND,
                self.DECK,
                self.hand,
                self.bot_hand,
                self.pile_cards,
                self.VICTORY,
                self.DEFEAT,
                self.assets,
            )
            card.displayCard(self.WIN, current_x, current_y, True, *self.assets)
            pygame.display.update()
            self.clock.tick(self.FPS)
        card._Card__position = end_pos 
        self.hand.append(card)  

    def handle_mouse_click(self):
        """
        Handles the mouse click event during the game.

        If the game is over, the function returns immediately. Otherwise, it checks
        if the mouse click is on the deck area. If so, a new card is drawn and 
        animated to the player's hand. If the click is not on the deck, it checks 
        if any card in the player's hand is selected. If a selected card is playable, 
        it is removed from the hand, animated to the pile, and its effect is applied. 
        Depending on the card effect, the bot's hand may be updated, and the bot's 
        turn may be skipped. The game window is redrawn after each action.

        Returns:
            None
        """
        if self.game_over:
            return  

        mouse_pos = pygame.mouse.get_pos()
        if (
            self.DECK_X < mouse_pos[0] < self.DECK_X + 150
            and self.DECK_Y < mouse_pos[1] < self.DECK_Y + 180
        ):
            new_card = Card()
            self.animate_draw_card(
                new_card, (1200 / 10 + len(self.hand) * 65, 700 - 120)
            )
        else:
            selected_card = -1
            for i in self.hand:
                if i.select():
                    selected_card = i
            if selected_card != -1:
                bot_skip = False
                if selected_card.playable(self.pile_cards, True):
                    self.hand.remove(
                        selected_card
                    )  
                    self.animate_card(
                        selected_card,
                        selected_card._Card__position,
                        (self.PILE_X, self.PILE_Y),
                    )
                    self.pile_cards.append(selected_card)
                    effect = card_effect(selected_card)
                    if effect == 1:  
                        for i in range(2):
                            self.bot_hand.append(Card())
                    elif effect == 2: 
                        bot_skip = True
                    elif effect == 4: 
                        for i in range(4):
                            self.bot_hand.append(Card())
                    draw_window(
                        self.WIN,
                        self.BACKGROUND,
                        self.DECK,
                        self.hand,
                        self.bot_hand,
                        self.pile_cards,
                        self.VICTORY,
                        self.DEFEAT,
                        self.assets,
                    )
                    pygame.time.wait(1000)
                    if not bot_skip: 
                        self.bot_play_turn()

    def bot_play_turn(self):
        """
        Executes the bot's turn in the UNO game.

        If the game is over, the function returns immediately. Otherwise, it selects a card for the bot to play.
        If a card is selected, it is removed from the bot's hand, animated to the pile, and added to the pile.
        The card's effect is then applied:
            - If the effect is 1, the bot draws 2 cards.
            - If the effect is 2, the bot's turn ends.
            - If the effect is 4, the bot draws 4 cards.
        If no card is selected, the bot draws a card and attempts to play again.

        Returns:
            None
        """
        if self.game_over:
            return  

        card = bot_turn(self.bot_hand, self.pile_cards)
        if card:
            self.bot_hand.remove(card)  
            self.animate_card(card, card._Card__position, (self.PILE_X, self.PILE_Y))
            self.pile_cards.append(card)
            card.playable(self.pile_cards, True)
            effect = card_effect(card)
            if effect == 1:
                for i in range(2):
                    self.hand.append(Card())
            elif effect == 2: 
                return  
            elif effect == 4:
                for i in range(4):
                    self.hand.append(Card())
        else:
            self.bot_hand.append(Card())
            self.bot_play_turn()  

    def check_game_over(self):
        """
        Checks if the game is over by evaluating the player's hand and the bot's hand.
        
        If the player's hand is empty, sets the game state to over, stops the game loop,
        and displays the victory screen. If the bot's hand is empty, sets the game state
        to over, stops the game loop, and displays the defeat screen.
        """
        if not self.hand:
            self.game_over = True
            self.running = False
            self.display_game_over_screen("Victory")
        elif not self.bot_hand:
            self.game_over = True
            self.running = False
            self.display_game_over_screen("Defeat")

    def display_game_over_screen(self, result):
        """
        Displays the game over screen with the result and options to play again or quit.
        Args:
            result (str): The result of the game to be displayed (e.g., "You Win!" or "Game Over").
        The method performs the following actions:
        - Renders the result text at the center of the screen.
        - Displays "Play Again" and "Quit" buttons below the result text.
        - Waits for user interaction to either restart the game or quit.
        Note:
            This method assumes that the Pygame library is initialized and that the game loop is running.
        """
        font = pygame.font.Font(None, 74)
        text = font.render(result, True, (255, 255, 255))
        self.WIN.blit(
            text,
            (
                self.WIDTH // 2 - text.get_width() // 2,
                self.HEIGHT // 2 - text.get_height() // 2,
            ),
        )
        pygame.display.update()
        pygame.time.wait(2000)

        
        play_again_button = pygame.Rect(
            self.WIDTH // 2 - 100, self.HEIGHT // 2 + 50, 200, 50
        )
        quit_button = pygame.Rect(
            self.WIDTH // 2 - 100, self.HEIGHT // 2 + 120, 200, 50
        )
        pygame.draw.rect(self.WIN, (0, 255, 0), play_again_button, border_radius=10)
        pygame.draw.rect(self.WIN, (255, 0, 0), quit_button, border_radius=10)
        play_again_text = font.render("Play Again", True, (0, 0, 0))
        quit_text = font.render("Quit", True, (0, 0, 0))
        self.WIN.blit(
            play_again_text, (play_again_button.x + 10, play_again_button.y + 10)
        )
        self.WIN.blit(quit_text, (quit_button.x + 50, quit_button.y + 10))
        pygame.display.update()

        while self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.game_over = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if play_again_button.collidepoint(mouse_pos):
                        self.reset_game()
                    elif quit_button.collidepoint(mouse_pos):
                        self.running = False
                        self.game_over = False

    def reset_game(self):
        """
        Resets the game to its initial state by clearing the pile cards, player hand, and bot hand.
        Reinitializes the player's hand and bot's hand with the starting number of cards.
        Sets the game_over flag to False.
        """
        self.pile_cards = []
        self.hand = []
        self.bot_hand = []
        for i in range(self.STARTING_HAND):
            self.hand.append(Card())
        for j in range(self.BOT_STARTING_HAND):
            self.bot_hand.append(Card())
        self.game_over = False

    def run(self):
        """
        Runs the main game loop.

        This method handles the main game loop, which includes:
        - Updating the game clock.
        - Processing user input events such as quitting the game or mouse clicks.
        - Drawing the game window with the current game state.
        - Checking if the game is over.
        - Updating the display.

        The loop continues running until the `self.running` flag is set to False.
        """
        while self.running:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse_click()

            draw_window(
                self.WIN,
                self.BACKGROUND,
                self.DECK,
                self.hand,
                self.bot_hand,
                self.pile_cards,
                self.VICTORY,
                self.DEFEAT,
                self.assets,
            )

            self.check_game_over()

            pygame.display.update()
        pygame.quit()
