import threading
from pynput import keyboard

# GPT-generated comments
class Keyboard:
    def __init__(self, controller):
        self.controller = controller
        self.recent_key = None

        # Listener runs in its own thread to prevent blocking the rest of the program
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.thread = threading.Thread(target=self.listener.start)
        self.thread.start()

    def on_press(self, key):
        # Store the most recent character key press for external use
        # Non-character keys (e.g. shift, ctrl) are ignored to avoid exceptions
        try:
            self.recent_key = key.char
            print(f"\nKey pressed: {key.char}")
        except AttributeError:
            pass
