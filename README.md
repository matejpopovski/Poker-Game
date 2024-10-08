# Poker Game

## Overview

The Poker Game project is an interactive graphical implementation of a poker game built using Python and Pygame. This project allows players to engage in a digital poker experience. The game features a user-friendly interface, animated card movements, and realistic card mechanics, making it an enjoyable experience for poker enthusiasts.

<table style="border-collapse: separate; border-spacing: 20px;">
    <tr>
        <td><img src="images/Screenshot1.png" alt="Screenshot1" width="500"/></td>
        <td><img src="images/Screenshot2.png" alt="Screenshot2" width="500"/></td>
    </tr>
</table>

In this poker game, Player 1 and Player 2 each receive 2 cards, while 3 cards are dealt on the table. In contrast to traditional Texas Hold'em poker, where the dealer places 5 cards on the table, this variation features only 3 cards, resulting in reduced odds of forming a strong hand. The player with the better hand wins the game, and you can immediately play another round with a simple click anywhere on the screen.

## Tools and Technologies

This project leverages several Python libraries and frameworks, including:

- **Ctypes Integration**: Ctypes is used in this project to manage DPI scaling, ensuring that game elements are displayed correctly across different screen resolutions, especially for high-DPI environments.
- **Pygame**: The core library used for creating the game’s graphics, handling user input, and managing the game loop. Pygame provides essential functionalities like drawing shapes, loading images, and handling events.
- **Random**: A built-in Python library used to introduce randomness in card dealing and animations, ensuring a unique experience for each game session.


## Features

- **Graphical User Interface (GUI)**: The game is developed with a visually appealing GUI, designed to provide a seamless and immersive experience. Players can easily view their cards, the community cards.
- **Dynamic Card Animation**: Cards are animated when dealt, providing a smooth transition and enhancing the game's visual appeal. The cards can rotate and scale to create an engaging user experience.
- **Game Logic**: The underlying game logic handles the rules of poker, including dealing cards, evaluating hands, and determining the winner, ensuring a fair and competitive environment.

## Installation and Usage

To run the game, ensure you have Python and Pygame installed on your system. Clone this repository and navigate to the project directory:

```bash
git clone https://github.com/matejpopovski/poker-game.git
cd Poker-Game
python3 main.py 

```

🔊 Soon to be added: Card Sounds, Tip The Dealer Animation, Poker Odds Calculator

