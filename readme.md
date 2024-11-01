# Higher Lower Game

This Python project is a simple follower-count comparison game where users guess which social media personality has more followers. The game uses data from `game_data.py` to compare two personalities and keeps score based on correct guesses.

## Project Structure

- **higherlower.py**: This is the main file that contains the game logic. Run this file to play the game.
- **art.py**: This file contains ASCII art used for game visuals, such as logos and versus graphics.
- **game_data.py**: Contains a list of dictionaries with information about social media personalities, including names, descriptions, countries, and follower counts.

## Installation

1. Ensure you have Python 3 installed on your system.
2. Clone or download the repository to your local machine.
3. Place `higherlower.py`, `art.py`, and `game_data.py` in the same folder.
4. Open a terminal and navigate to the project directory.
5. Run the game with the following command:

   ```bash
   python higherlower.py

## How to Play
1. Upon starting the game, you'll be shown two personalities, labeled "A" and "B," along with their descriptions and countries.
2. Enter "A" if you believe the personality in the "A" position has more followers, or "B" if you believe the personality in the "B" position has more followers.
3. If you guess correctly, your score will increase, and a new comparison will appear.
4. If you guess incorrectly, the game will end, and your final score will be displayed.

## Example Gameplay
The game will display as follows:
```bash
Compare A: Taylor Swift, a Musician, from the USA.
vs
Against B: Cristiano Ronaldo, a Footballer, from Portugal.
Who has more followers? Type 'A' or 'B':
```

If you guess correctly, the game continues; if not, it will show your final score.