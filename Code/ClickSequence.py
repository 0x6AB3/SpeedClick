import os
from Code.Click import Click

class ClickSequence:
    def __init__(self):
        self.clicks = []

    def __iter__(self):
        return iter(self.clicks)

    def execute(self):
        for click in self.clicks:
            click.execute()

    def append(self, click):
        self.clicks.append(click)

    def clear(self):
        self.clicks.clear()

    def save(self, profile_number):
        positions = [f"{x},{y}" for x, y in self.clicks]
        to_write = " ".join(positions)
        to_write += "\n"

        if to_write == "\n":
            return

        os.makedirs("Profiles", exist_ok=True)
        with open(f"Profiles/sequence_{profile_number}.txt", "a") as f:
            f.write(to_write)

    def load(self, profile_number):
        self.clear()
        data = None
        with open(f"Profiles/sequence_{profile_number}.txt", "r") as f:
            data = f.readline()

        for position in data.split(" "):
            x, y = position.split(",")
            self.append(Click(x, y))