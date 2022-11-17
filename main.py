import random


def d(sides: int) -> int:
    """ Rolls one die of a given size, returns the value rolled """
    return random.randint(1, sides)


def dice(rolls: int, sides: int) -> int:
    """ Rolls multiple dice of a given size, returns the sum total """
    return sum(d(sides) for _ in range(rolls))


if __name__ == '__main__':
    n_rolls = int(input("How many dice? "))
    n_sides = int(input("What size dice? "))
    print(f"Your roll ({n_rolls}d{n_sides}):", dice(n_rolls, n_sides))
