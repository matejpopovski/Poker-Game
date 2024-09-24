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
        self.animation_start_time = pygame.time.get_ticks()
        self.animation_complete = False
        self.uuid = None
        self.position = None
        self.start_position = (0, 1080)
        self.orig_position = self.start_position
        self.data = CardTuple(value=input_value, suit=input_suit)

        # Ensure the value and suit are formatted correctly
        value_map = {
            '2': '2', '3': '3', '4': '4', '5': '5',
            '6': '6', '7': '7', '8': '8', '9': '9',
            '10': '10', 'J': 'jack', 'Q': 'queen', 'K': 'king', 'A': 'ace'
        }

        # Update the id to match the format: "2_of_clubs" instead of "T_of_clubs"
        self.id = f"{value_map[input_value]}_of_{input_suit}.png"
        self.img = f"graphics/cards/{self.id}"

        # Load the image
        self.card_img = pygame.image.load(self.img)

        # Set the desired width and height for the cards
        desired_width = 100  # Adjust as needed
        desired_height = 140  # Adjust as needed

        # Scale the image to the desired size
        self.card_img = pygame.transform.scale(self.card_img, (desired_width, desired_height))
        self.card_rotation_angle = random.uniform(-3, 3)
        self.card_rot = pygame.transform.rotate(self.card_img, self.card_rotation_angle)
        self.card_bounding_rect = self.card_rot.get_rect()  # Update this line
        self.card_surf = pygame.Surface(self.card_bounding_rect.size, pygame.SRCALPHA)
        
        # Calculate the position to blit the rotated image onto the surface
        blit_pos = (0, 0)
        self.card_surf.blit(self.card_rot, blit_pos)

        # Random y value for card
        self.card_y = (P1_C1[1] - self.card_surf.get_height() // 2) + random.randint(-20, 20)




class Player:
    def __init__(self):
        self.cards = []

class Flop:
    def __init__(self):
        self.cards = []
