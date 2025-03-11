# Boss Rush Game

A fast-paced, action-packed boss rush game built with Python and Pygame. Face off against powerful bosses, use dashes to evade attacks, and time your melee strikes to defeat enemies!

## Gameplay Preview

![Gameplay Preview](gameplay_0.mov)

## Features

- **Smooth Player Movement**: Move in all directions with dashing mechanics.
- **Melee Combat**: Attack with a short cooldown and knockback effect.
- **Challenging Boss Fight**: The boss has a health system and reacts to attacks.
- **Minimalistic Design**: Simple shapes and colors for clarity.

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/boss-rush-game.git
   cd boss-rush-game
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Run the game:

   ```sh
   python src/main.py
   ```

## Controls

- **WASD / Arrow Keys** - Move
- **Left Shift** - Dash
- **Spacebar** - Attack
- **Esc** - Quit

## Project Structure

```bash
├── src
│   ├── main.py       # Game loop and main logic
│   ├── player.py     # Player movement, attack mechanics
│   ├── boss.py       # Boss behavior and health system
│   ├── settings.py   # Game settings
│   ├── utils.py      # Utility functions (if any)
├── assets           # Game assets (sprites, sounds, etc.)
├── docs             # Documentation (if applicable)
├── gameplay_0.mov   # Gameplay preview
├── requirements.txt # Python dependencies
├── LICENSE          # License information
└── README.md        # This file
```

## Future Improvements

- Add multiple bosses with unique attack patterns.
- Implement a health system for the player.
- Introduce visual effects and animations.
- Add sound effects for attacks and damage.

## License

This project is licensed under the MIT License.

---

Feel free to contribute or suggest improvements!
