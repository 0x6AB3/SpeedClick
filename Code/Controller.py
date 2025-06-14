import sys
import threading
import tkinter as tk
from tkinter import messagebox
from Code.Mouse import Mouse
from Code.Keyboard import Keyboard
from Code.ClickSequence import ClickSequence


class Controller:
    def __init__(self):
        self.mouse = Mouse(self)
        self.keyboard = Keyboard(self)
        self.save_clicks = False
        self.saved_clicks = ClickSequence()
        self.loaded_profile = '0'

        # popups box stuff
        self.root = tk.Tk()
        self.root.withdraw()
        self.top = tk.Toplevel()
        self.top.withdraw()
        self.top.attributes("-topmost", True)

        #self.thread = threading.Thread(target=self.check_input)
        #self.thread.start()
        #print("Controller ready.")
        self.check_input()

    def check_input(self):
        profile_numbers = [f"{i}" for i in range(0, 10)]

        print("SpeedClick is running...")
        print("Commands: (list them here)")
        while True:
            key = self.keyboard.recent_key
            if key == 's':
                self.save_clicks = not self.save_clicks
                print(f"Click saving: {self.save_clicks}")

            elif key == 'e':
                self.save_clicks = False
                position = self.mouse.get_position()
                self.saved_clicks.execute()
                self.mouse.set_position(position)

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
                self.loaded_profile = key
                print(f"Loading profile: {key}")
                self.saved_clicks.from_json(key)

            elif key == 'q':
                sys.exit(0)

            elif key == "n":
                self.mouse.noise()

            elif key == "f":
                self.saved_clicks.initial_clicks += 1
                print(f"SpeedClick will now click {self.saved_clicks.initial_clicks} time/s first at your current mouse position before executing the click sequence")

            elif key == "g":
                self.saved_clicks.initial_clicks -= 1
                print(f"SpeedClick will now click {self.saved_clicks.initial_clicks} time/s first at your current mouse position before executing the click sequence")

            elif key == "a":
                self.save_clicks = False
                self.mouse.toggle_auto_click()
                print(f"Auto click is on: {self.mouse.auto_click}")

            self.keyboard.recent_key = None