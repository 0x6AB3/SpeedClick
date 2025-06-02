import time
import threading

import pyautogui
from pynput.mouse import Controller
from pynput import mouse
from pynput.mouse import Controller as MouseController
from Code.Click import Click
from Code.Drag import Drag



# GPT-generated comments
class Mouse:
    def __init__(self, controller):
        self.controller = controller
        self.mouse = MouseController()
        self.dragging = False
        self.drag_positions = []
        self.recent_click = None
        self.recent_click_time = None
        self.auto_click = False

        # Start mouse listener in a separate thread to avoid blocking the main program
        self.listener = mouse.Listener(on_click=self.on_click, on_move=self.on_move)
        self.thread = threading.Thread(target=self.listener.start)
        self.thread.start()

        self.auto_click_thread = None

    def auto_click_thread_loop(self):
        while self.auto_click:
            pyautogui.click()

    def toggle_auto_click(self):
        self.auto_click = not self.auto_click
        if self.auto_click_thread is None:
            self.auto_click_thread = threading.Thread(target=self.auto_click_thread_loop)
            self.auto_click_thread.start()
        else:
            self.auto_click_thread = None

    def get_position(self):
        return self.mouse.position

    def set_position(self, position):
        self.mouse.position = position

    def noise(self, width=600, height=150, step=25, duration=0.15):
        original_x, original_y = self.mouse.position
        x_factor = 1
        for y in range(int(max(original_y-height/2, 0)), int(min(original_y+height/2, 1080)), step):
            pyautogui.moveTo(original_x+((width*x_factor)/2), y, duration)
            x_factor *= -1
        pyautogui.moveTo(original_x, original_y, duration)

    def on_click(self, x, y, button, pressed):
        # Only record clicks if the controller has explicitly enabled it
        if pressed and self.controller.save_clicks:
            # Capture the click position as a Click object and store it via the controller
            self.recent_click = Click(x, y)
            self.drag_positions.clear()
            self.drag_positions.append((x, y))
            self.recent_click_time = time.perf_counter()

        elif (not pressed) and self.controller.save_clicks:
            if ((time.perf_counter() - self.recent_click_time) * 1000) > 100:
                drag = Drag(self.drag_positions)
                self.controller.saved_clicks.append(drag)
                print("Drag saved")
            else:
                self.controller.saved_clicks.append(self.recent_click)
                print(f"Click saved at ({x},{y})")

    def on_move(self, x, y):
        if self.dragging:
            self.drag_positions.append(x,y)