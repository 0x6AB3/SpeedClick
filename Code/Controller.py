import threading

from Keyboard import Keyboard
from Mouse import Mouse
from ClickSequence import ClickSequence
import tkinter as tk
from tkinter import messagebox


class Controller:
    def __init__(self):
        self.mouse = Mouse(self)
        self.keyboard = Keyboard(self)
        self.save_clicks = False
        self.saved_clicks = ClickSequence()

        # popups box stuff
        self.root = tk.Tk()
        self.root.withdraw()
        self.top = tk.Toplevel()
        self.top.withdraw()
        self.top.attributes("-topmost", True)

        self.thread = threading.Thread(target=self.check_input())
        self.thread.start()

        print("Controller ready.")

    def check_input(self):
        while True:
            if self.keyboard.recent_key == 's':
                self.save_clicks = not self.save_clicks
                print(f"Click saving: {self.save_clicks}")

            elif self.keyboard.recent_key == 'e':
                self.save_clicks = False
                self.saved_clicks.execute()

            elif self.keyboard.recent_key == 'v':
                clicks = [f"{x},{y}" for (x, y) in self.saved_clicks]
                tk.messagebox.showinfo("Current selection", f"{clicks}", parent=self.top)

            elif self.keyboard.recent_key == 'd':
                self.saved_clicks.clear()
                tk.messagebox.showinfo("Saved clicks", f"Sequence is now empty", parent=self.top)

            elif self.keyboard.recent_key == 'q':
                pass
            self.keyboard.recent_key = None