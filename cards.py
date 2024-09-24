from collections import namedtuple
from settings import *
import pygame
import random

CardTuple = namedtuple('Card', ['value', 'suit'])

# Define card values
cardvalues = [
    2, 3, 4, 5, 6, 7, 8, 9, "T",
    "J",  # Jack
    "Q",  # Queen
    "K",  # King
    "A"   # Ace
]

# Define card suits
cardsuits = ['clubs', 'diamonds', 'hearts', 'spades']

# class Card:
#     def __init__(self, input_value, input_suit):
#         self.animation_start_time = pygame.time.get_ticks()
#         self.animation_complete = False
#         self.uuid = None
#         self.position = None
#         self.start_position = (0, 1080)
#         self.orig_position = self.start_position
#         self.data = CardTuple(value=input_value, suit=input_suit)
        
#         # Change the id format to match the new naming convention
#         # Handle values and suits appropriately
#         if input_value == "A":
#             value_name = "ace"
#         elif input_value == "K":
#             value_name = "king"
#         elif input_value == "Q":
#             value_name = "queen"
#         elif input_value == "J":
#             value_name = "jack"
#         elif input_value == "T":
#             value_name = "10"  # Use '10' instead of 'T'
#         else:
#             value_name = str(input_value)  # Use string representation for numbers

#         self.id = f"{value_name}_of_{self.data.suit}.png"
#         self.img = f"graphics/cards/{self.id}"
        
#         # Load and scale the card image
#         self.card_img = pygame.image.load(self.img)
#         self.card_img = pygame.transform.scale(self.card_img, (self.card_img.get_width() * 4, self.card_img.get_height() * 4))
        
#         # Rotate the card image
#         self.card_rotation_angle = random.uniform(-3, 3)
#         self.card_rot = pygame.transform.rotate(self.card_img, self.card_rotation_angle)
        
#         # Create bounding rectangle for the rotated image
#         self.card_bounding_rect = self.card_rot.get_rect()
#         self.card_surf = pygame.Surface(self.card_bounding_rect.size, pygame.SRCALPHA)

#         # Calculate the position to blit the rotated image onto the surface
#         blit_pos = (0, 0)
#         self.card_surf.blit(self.card_rot, blit_pos)

#         # Random y value for card
#         self.card_y = (P1_C1[1] - self.card_surf.get_height() // 2) + random.randint(-20, 20)

class Card:
    def __init__(self, input_value, input_suit):
        # Other initializations...
        
        self.card_y = 0  # Initialize card_y attribute (set to an appropriate default value)
        
        # Example for setting the card image
        value_dict = {
            '2': '2', '3': '3', '4': '4', '5': '5',
            '6': '6', '7': '7', '8': '8', '9': '9',
            'T': '10',  # Map 'T' to '10'
            'J': 'jack', 'Q': 'queen', 'K': 'king', 'A': 'ace'
        }

        input_value_str = str(input_value)

        if input_value_str in value_dict:
            self.id = f"{value_dict[input_value_str]}_of_{input_suit}.png"
        else:
            raise ValueError(f"Invalid card value: {input_value}")

        # Load the card image and other attributes if needed
        self.card_img = pygame.image.load(self.id)  # Assuming id contains the correct image path
        self.position = (0, self.card_y)  # You can set initial position as needed





class Player:
    def __init__(self):
        self.cards = []

class Flop:
    def __init__(self):
        self.cards = []
