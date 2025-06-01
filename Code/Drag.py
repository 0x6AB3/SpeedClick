import pyautogui

class Drag:
    def __init__(self, positions):
        self.positions = positions

    def __iter__(self):
        yield self.positions[0]

    def execute(self):
        duration = 0.05
        pyautogui.moveTo(self.positions[0][0], self.positions[0][1], duration=duration)
        pyautogui.mouseDown()
        for x,y in self.positions:
            pyautogui.moveTo(x, y, duration=duration)
        pyautogui.mouseUp()