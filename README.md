# SpeedClick

A lightweight, Python-based utility tool designed for automating mouse clicks and keyboard actions with ease. Whether you're looking to streamline repetitive tasks or simulate input for testing, SpeedClick provides a simple keyboard-driven interface to automate your workflow.

---

## Features

- **Click & drag recording**
- **Execution of saved sequences**
- **Profile save/load system**
- **Mouse noise/random movement mode**
- **Live popup previews of click sequences**
- **Instant quit command for safety**

---

## How It Works

1. **Run** `SpeedClick(main).py` inside the `Code` directory using **Python 3.13**.  
   ➤ [Download Python 3.13.3 here](https://www.python.org/ftp/python/3.13.3/python-3.13.3-amd64.exe)

2. Let the script run in the background in a terminal or your IDE.  
   By default, it starts in **command mode** — be careful with your keyboard inputs.

---

## Keybinds & Modes

| Key | Action |
|-----|--------|
| `S` | **Selection Mode Toggle** – Start/stop recording mouse clicks and drags. Adds to the current sequence. |
| `E` | **Execute Mode** – Run the saved selection sequence. |
| `D` | **Delete Sequence** – Clears the currently saved sequence. |
| `V` | **View Sequence** – Shows the current sequence in a popup. |
| `0–9` | **Profile Save/Load** – Save or load the current sequence to/from one of 10 profiles. |
| `N` | **Noise Mode** – Automatically move the mouse around within a predefined area. |
| `Q` | **Quit** – Exit the program immediately and safely. |

---

## Notes

- Works best on the **main monitor** — clicks on other monitors may be misaligned.
- Selection mode **does not overwrite** — all clicks are added until cleared.
- Runs safely in the background, providing real-time input detection.
- GUI popups help you preview your sequences visually.

---
