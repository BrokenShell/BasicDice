# Basic Game Dice
## Instructor Notes


### 0. Instructor Prep List (Prior to Workshop)


---
### 1. Engage Classroom (1-2 min.)


---
### 2. Getting Started (3-5 min.)
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
### 4. Let’s Build (30-40 min.)
Follow the lesson as described in the [lesson.ipynb](lesson.ipynb) file.


---
### 5. Wrap Up (7-10 min.)
