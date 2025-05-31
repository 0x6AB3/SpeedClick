import sys
import threading
import tkinter as tk
from Mouse import Mouse
from Keyboard import Keyboard
from tkinter import messagebox
from ClickSequence import ClickSequence


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
        profile_numbers = [f"{i}" for i in range(0, 10)]

        while True:
            key = self.keyboard.recent_key
            if key == 's':
                self.save_clicks = not self.save_clicks
                print(f"Click saving: {self.save_clicks}")

            elif key == 'e':
                self.save_clicks = False
                self.saved_clicks.execute()

            elif key == 'v':
                self.save_clicks = False
                clicks = [f"{x},{y}" for (x, y) in self.saved_clicks]
                tk.messagebox.showinfo("Current selection", f"{clicks}", parent=self.top)

            elif key == 'd':
                self.save_clicks = False
                self.saved_clicks.clear()
                tk.messagebox.showinfo("Saved clicks", f"Sequence is now empty", parent=self.top)

            elif key in profile_numbers:
                self.save_clicks = False
                self.saved_clicks.save(key)

            elif key == 'q':
                sys.exit(0)
            self.keyboard.recent_key = None