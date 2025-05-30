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
        pass

    def load(self):
        pass