from enum import Enum
import random


class Toy(Enum):
    toy_1 = "Bulb"
    toy_2 = "Angel"
    toy_3 = "Dog"
    toy_4 = "Lion"
    toy_5 = "Ball"
    toy_6 = "Flake"
    toy_7 = "Rabbit"
    toy_8 = "Cat"
    toy_9 = "Candy"
    toy_10 = "Jewel"




class Color(Enum):
    color_1 = "Red"
    color_2 = "Blue"
    color_3 = "Yellow"
    color_4 = "Green"
    color_5 = "Purple"
    color_6 = "Silver"
    color_7 = "Gold"
    color_8 = "Grey"
    color_9 = "Brown"
    color_10 = "Violet"



def get_random_toy() -> int:
    toy = random.choice(list(Toy))
    color = random.choice(list(Color))
    print(f"{color.value} {toy.value}")
    return 0