# WIP - using numpy.random.randint to see if it can be converted to get an actual english word.

from numpy.random import randint

seq = randint(97, 123, 2)
print(''.join([chr(letter) for letter in seq]))
