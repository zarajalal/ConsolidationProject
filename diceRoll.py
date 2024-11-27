# Rolls the dice three times to initialze points
import random

def dice_roll():
    return [random.randint(1, 6) for _ in range(3)]