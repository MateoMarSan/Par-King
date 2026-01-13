# Par-King

Par-King is a console-based implementation of the classic Rush Hour sliding puzzle game.
The objective is to move the main (red) car horizontally until it exits the board by sliding
other vehicles out of the way.

The project focuses on grid-based logic, movement constraints, and basic file handling in Python.

---

## Requirements

- Python 3.8 or higher
- Terminal / Command Prompt
- No external libraries required

---

## Project Structure

```
├── Par-King.py      # Main game file
├── niveles.txt      # Level definitions
├── records.txt      # Best scores per level
```

---

## How to Run

1. Clone or download the repository
2. Make sure all files are in the same directory
3. Open a terminal in that directory
4. Run the game with:

```bash
python Par-King.py
```

---

## How to Play

- Each car is assigned a letter (`a`, `b`, `c`, ...)
- You control the cars by typing letters:
  - Lowercase letter → move forward
  - Uppercase letter → move backward
- You can input multiple moves in one turn

### Example

```
Movimientos = aBc
```

Each valid movement counts as one move.

---

## Game Rules

- The board is a 6×6 grid
- Cars can only move in their orientation:
  - H → horizontal
  - V → vertical
- Cars cannot overlap or pass through walls
- The level is completed when the main horizontal car reaches the exit

---

## Levels and Records

- Levels are loaded from `niveles.txt`
- Best scores are stored in `records.txt`
- Records are updated automatically

---

## License

This project is intended for academic and learning use.
