import io
import time
import tkinter as tk
import math
import threading
from tkinter import filedialog
from PIL import Image


class MainWindow(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        self.title("Fractal")

        self.canvas = tk.Canvas(self, width=700, height=650, bg="#222222")
        self.canvas.pack()

        self.btn = tk.Button(self, text="Draw", command=self.draw)
        self.btn.pack(side=tk.LEFT)

        self.save_btn = tk.Button(self, text="Save Image", command=self.save_image_button)
        self.save_btn.pack(side=tk.RIGHT, pady=10)
        self.label = tk.Label(self, text="Level")
        self.label.pack()

        self.level = tk.Entry(self, width=5, justify=tk.CENTER)
        self.level.insert(tk.INSERT, "1")
        self.level.pack()

        self.thread = None

        self.mainloop()


    def save_image_button(self):
        filename = filedialog.asksaveasfilename(defaultextension=".tiff")
        if filename:
            self.save_image(filename)

    def save_image(self, filename):
        # Generate PostScript file
        ps_file = self.canvas.postscript(colormode='color')

        # Convert PostScript to PIL Image
        pil_image = Image.open(io.BytesIO(ps_file.encode('utf-8')),)
        pil_image = pil_image.crop(self.canvas.bbox('all'))

        # Save PIL Image as PNG file
        pil_image.save(filename, 'TIFF', dpi=(500, 500))

    def draw(self):
        # clear canvas
        self.canvas.delete("all")

        height = int(round(700*math.sqrt(3.0)/2.0))
        level = int(self.level.get())

        for level in range(1, level + 1):
            self.level.delete(0, tk.END)
            self.level.insert(tk.INSERT, str(level))
            self.recursion(level, 0, height, 350, 0, 700, height, "#80acf2", "#70fac5", "#c28ff7")
            self.update()
            time.sleep(0.125)
        
        print('done')
            

    def recursion(self, level, x1, y1, x2, y2, x3, y3, color1, color2, color3):
        if level <= 1:
            self.canvas.create_line(x1, y1, x2, y2, fill=color1, width=2)
            time.sleep(0.05)
            self.canvas.create_line(x2, y2, x3, y3, fill=color2, width=2)
            time.sleep(0.05)
            self.canvas.create_line(x3, y3, x1, y1, fill=color3, width=2)
            time.sleep(0.05)
        else:
            level = level - 1

            middle_x1 = (x1 + x2)/2
            middle_y1 = (y1 + y2)/2

            middle_x2 = (x2 + x3)/2
            middle_y2 = (y2 + y3)/2

            middle_x3 = (x3 + x1)/2
            middle_y3 = (y3 + y1)/2

            # self.recursion(level, x1, y1, middle_x1, middle_y1, middle_x3, middle_y3, color1, color2, color3)
            self.thread = threading.Thread(target=self.recursion, args=(level, x1, y1, middle_x1, middle_y1, middle_x3, middle_y3, color1, color2, color3))
            self.thread.start()
            self.update()
            time.sleep(0.05)

            # self.recursion(level, middle_x1, middle_y1, x2, y2, middle_x2, middle_y2, color2, color1, color3)
            self.thread = threading.Thread(target=self.recursion, args=(level, middle_x1, middle_y1, x2, y2, middle_x2, middle_y2, color2, color1, color3))
            self.thread.start()
            self.update()
            time.sleep(0.05)

            # self.recursion(level, middle_x3, middle_y3, middle_x2, middle_y2, x3, y3, color1, color2, color3)
            self.thread = threading.Thread(target=self.recursion, args=(level, middle_x3, middle_y3, middle_x2, middle_y2, x3, y3, color1, color2, color3))
            self.thread.start()
            self.update()
            time.sleep(0.05)

    def stop_thread(self):
        if self.thread is not None:
            self.thread.join()  # Wait for the drawing thread to complete
            self.thread = None

# create and start main window
MainWindow()
