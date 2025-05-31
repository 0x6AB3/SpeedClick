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

    def save(self):
        positions = [f"{x},{y}" for x, y in self.clicks]
        to_write = " ".join(positions)
        to_write += "\n"

        with open("SavedSequences.txt", "a") as f:
            f.write(to_write)

    def load(self):
        pass