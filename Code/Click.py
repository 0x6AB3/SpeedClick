import pyautogui
from random import randint

# GPT-generated comments
class Click:
    def __init__(self, x, y):
        # Store coordinates to make the click repeatable and location-specific
        self.x = x
        self.y = y

    def __iter__(self):
        yield self.x
        yield self.y

    def execute(self):
        # Randomized movement duration adds slight human-like variability
        #duration = float(randint(10, 100)) / 100
        duration = 0.01
        # Simulate human behavior by not instantly snapping to the location
        pyautogui.moveTo(self.x, self.y, duration=duration)

        # Final action: clicking after the cursor reaches the location
        pyautogui.click()

    def to_dict(self):
        return {"x": self.x, "y": self.y}

    @staticmethod
    def from_dict(data):
        return Click(data["x"], data["y"])