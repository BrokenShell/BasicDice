# Basic Game Dice
## Instructor Notes


### 0. Instructor Prep List
Read through the code and make sure the `main.py` file executes without error.

---
### 1. Engage Classroom
Personalize the experience by asking the group what games they like to play that involve dice. Suggest that they could implement many of those games with some fairly simple code. At the least, they could implement the dice portion of the game. And that's what we're doing today!

---
### 2. Getting Started
- Function definitions
  - def
  - args
  - return
- Using the standard library
  - random.randint
- Builtins
  - print
  - input
  - sum
  - range
  - int


---
### 3. What Are We Building? (2-3 min.)
Show an example of the finished product if applicable.
```python
import random


def d(sides: int) -> int:
    return random.randint(1, sides)


def dice(rolls: int, sides: int) -> int:
    return sum(d(sides) for _ in range(rolls))

```

---
### 4. Let’s Build Some Dice!
Code the lesson following the main.py file.

---
### 5. Wrap Up
Resources for learning Python...
