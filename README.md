# Basic Game Dice
## Instructor Notes


### 0. Instructor Prep List


---
### 1. Engage Classroom


---
### 2. Getting Started
- Function definitions
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
### 4. Let’s Build


---
### 5. Wrap Up
