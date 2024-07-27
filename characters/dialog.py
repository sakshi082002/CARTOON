import tkinter as tk
from tkinter import simpledialog
import os
import subprocess

# Function to execute the selected Python code
def execute_code(character):
    characters = {
        "1": "doreamon.py",
        "2": "shinchan.py",
        "3": "captain_america.py",
        "4": "ironman.py",
        "5": "pikachu.py",
        "6": "black_panther.py",
        "7": "tom_and_jerry.py",
    }
    if character in characters:
        character_script = characters[character]
        try:
            script_path = os.path.join(os.path.dirname(__file__), character_script)
            subprocess.run(["python", script_path])
        except FileNotFoundError:
            print(f"Failed to run {character_script}")
    else:
        print("Invalid choice")

# List of available cartoon characters
character_list = {
    "1": "Doraemon",
    "2": "Shinchan",
    "3": "Captain America Shield",
    "4": "Ironman",
    "5": "Pikachu",
    "6": "Black Panther",
    "7": "Tom and Jerry",
}

# Create a Tkinter window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Create a dialog box to get user input
character_choice = simpledialog.askstring("Character Selection", "Select a cartoon character:\n" + "\n".join(f"{key}: {value}" for key, value in character_list.items()))

# Execute the selected character's Python code
execute_code(character_choice)
