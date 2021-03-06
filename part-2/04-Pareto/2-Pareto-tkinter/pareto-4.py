import tkinter as tk
from init import *
from utils import *


def dots():
    n = 100
    for _ in range(n):
        x = rnd.randint(pole, w - pole)
        y = rnd.randint(pole, h - pole)
        fill_color = "#f50"
        canvas.create_oval(x-r, y-r, x+r, y+r, outline="#009", fill=fill_color)

window = tk.Tk()
canvas = tk.Canvas(window, width=w, height=h, bg='#fda')

btn_start = tk.Button(window,
    text='Pareto',
    width=15,
    command=dots
    # command=dots()
)

btn_start.pack()
canvas.pack()
print_axes(x0, y0, xm, ym, 'blue', canvas)
window.mainloop()
