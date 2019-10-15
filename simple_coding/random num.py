# A python program that generate a random number

from random import seed
from random import shuffle
seed(1)
sequence = [i for i in range (50)]
shuffle(sequence)
print(sequence)
