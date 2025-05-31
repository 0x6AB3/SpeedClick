import threading
from pynput import mouse
from Code.Click import Click

# GPT-generated comments
class Mouse:
    def __init__(self, controller):
        self.controller = controller

        # Start mouse listener in a separate thread to avoid blocking the main program
        self.listener = mouse.Listener(on_click=self.on_click)
        self.thread = threading.Thread(target=self.listener.start)
        self.thread.start()

    def on_click(self, x, y, button, pressed):
        # Only record clicks if the controller has explicitly enabled it
        if pressed and self.controller.save_clicks:
            # Capture the click position as a Click object and store it via the controller
            click = Click(x, y)
            self.controller.saved_clicks.append(click)
            print(f"Click saved at ({x},{y})")
