import time
from tkinter import *
from tkinter import font
from tkinter.ttk import Style


class Game:
    def __init__(self, master):
        self.master = master
        self.start_time = 0
        self.end_time = 0
        self.score = 0
        self.low_score = 999

        my_font = font.Font(family="Helvetica", size=24, weight="bold")

        # Create a label to display the score
        self.score_label = Label(master, text="Score: 0", font=my_font)
        self.score_label.pack()

        # Create a label to display the high score
        self.low_score_label = Label(
            master, text="Low score: Start", font=my_font)
        self.low_score_label.pack()

        # Create a style for the button
        style = Style()
        style.configure("MyButton.TButton", background="#006699",
                        foreground="#ffffff", font=my_font, padx=20, pady=10)

        # Create a button to start the game
        self.button = Button(master, text="Start",
                             font=my_font, command=self.start)
        self.button.pack()

    def start(self):
        # Start the timer
        self.start_time = time.time()

        # Change the button text
        self.button.configure(text="Stop", command=self.stop)

    def stop(self):
        # Stop the timer
        self.end_time = time.time()

        # Calculate the score
        self.score = self.end_time - self.start_time

        # Update the score label
        self.score_label.configure(text=f"Score: {self.score:.2f}")

        # Update the low score if necessary
        if self.score < self.low_score:
            self.low_score = self.score
            self.low_score_label.configure(
                text=f"Low score: {self.low_score:.2f}")

        # Change the button text
        self.button.configure(text="Start", command=self.start)


root = Tk()
root.wm_title("Click as fast as you can")
root.geometry("800x600+100+100")
game = Game(root)
root.mainloop()
