# import necessary libraries
import tkinter as tk
import numpy as np

# define the probability density function for a particle in a box
def probability_density(x, x1, x2, n):
    return (np.sin(n * np.pi * x / (x2 - x1)) / (np.pi * (x - x1)))**2

# create a Tkinter window and canvas
window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=300)
canvas.pack()

# set the range of x values and the number of energy levels
x1, x2 = 0, 10
n_levels = 3

# create a list of x values
x = np.linspace(x1 + 1, x2, 100)

# plot the probability densities for each energy level
for n in range(1, n_levels + 1):
    y = probability_density(x, x1, x2, n)
    points = [(i * 4, j * 3) for i, j in zip(x, y)]
    canvas.create_line(points, fill=f'#{n}00000')

# add a barrier at x = 5
canvas.create_line((200, 0), (200, 300), fill='black')

# run the Tkinter window
window.mainloop()
