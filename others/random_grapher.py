# %%
from numpy.random import randint
import matplotlib.pyplot as plt

# %%
high = 10
main_counts = [0 for _ in range(high)]
counts = [0 for _ in range(high)]

# %%
def generate_random_list():
    for _ in range(100000):
        yield randint(0, 2, size = high)

# %%
for _ in range(10):
    for value in generate_random_list():
        for number in range(high):
            if value[number] == 1:
                counts[number] += 1
            else:
                counts[number] -= 1
    for index in range(high):
        if counts[index] > 0:
            main_counts[index] += 1

# %%
plt.bar(x = range(high), height = main_counts, )
