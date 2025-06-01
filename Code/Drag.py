import pyautogui

class Drag:
    def __init__(self, positions):
        self.positions = positions

    def execute(self):
        duration = 0.0
        pyautogui.moveTo(self.positions[0][0], self.positions[0][1], duration=duration)
        pyautogui.mouseDown()
        for x,y in self.positions:
            pyautogui.moveTo(x, y, duration=duration)
        pyautogui.mouseUp()