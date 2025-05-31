import os

class ClickSequence:
    def __init__(self):
        self.clicks = []

    def __iter__(self):
        return iter(self.clicks)

    def execute(self):
        for click in self.clicks:
            click.execute()

    def append(self, target):
        self.clicks.append(target)

    def clear(self):
        self.clicks = []

    def save(self, profile_number):
        positions = [f"{x},{y}" for x, y in self.clicks]
        to_write = " ".join(positions)
        to_write += "\n"

        if to_write == "\n":
            return

        os.makedirs("Profiles", exist_ok=True)
        with open(f"Profiles/sequence_{profile_number}.txt", "a") as f:
            f.write(to_write)

    def load(self):
        pass