# WIP - deprecated
import tkinter as tk
import numpy as np


def probability_density(x, x1, x2, n):
    return (np.sin(n * np.pi * x / (x2 - x1)) / (np.pi * (x - x1)))**2


window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=300)
canvas.pack()


x1, x2 = 0, 10
n_levels = 3


x = np.linspace(x1 + 1, x2, 100)


for n in range(1, n_levels + 1):
    y = probability_density(x, x1, x2, n)
    points = [(i * 4, j * 3) for i, j in zip(x, y)]
    canvas.create_line(points, fill=f'#{n}00000')


canvas.create_line((200, 0), (200, 300), fill='black')


window.mainloop()
