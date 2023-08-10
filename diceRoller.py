 # Import library
# Create array of int "sides"
# Create variable that takes on the value of the random function calling "sides"
# Print said variable

import random

sides = range(1, 7)

random_side = random.choice(sides)
print("You've rolled a: ", random_side)
