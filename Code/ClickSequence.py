import json
import pyautogui
from Code.Click import Click

class ClickSequence:
    def __init__(self):
        self.clicks = []
        self.initial_clicks = 0

    def __iter__(self):
        return iter(self.clicks)

    def execute(self):
        if self.initial_clicks < 0:
            self.initial_clicks = 0

        for i in range(self.initial_clicks):
            pyautogui.click()

        for click in self.clicks:
            click.execute()

    def append(self, click):
        self.clicks.append(click)

    def clear(self):
        self.clicks.clear()

    def to_json(self, profile_number):
        with open(f"Profiles/{profile_number}.json", "w") as f:
            f.write(json.dumps([click.to_dict() for click in self.clicks], indent=4))
        print(f"Saved current sequence to profile: {profile_number}")

    def from_json(self, profile_number):
        json_string = None
        try:
            with open("Profiles/{profile_number}.json", "r") as f:
                json_string = f.read()
        except FileNotFoundError:
            print("Profile {profile_number} does not exist yet, saving...")
            self.to_json(profile_number)
            return

        self.clear()
        data = json.loads(json_string)
        for item in data:
            self.append(Click.from_dict(item))

