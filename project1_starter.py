"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Jelani Campbell
Date: 10/25/25

AI Usage: I used AI to help **format** the `save_character()` function with the correct file methods (`open`, `write`, `close`) and UTF-8 encoding, with short explanations and examples
Example: AI helped with file I/O error handling logic in save_character function
"""

import os

VALID_CLASSES = ["Warrior", "Mage", "Rogue", "Cleric"]

def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    # make sure name is a string and not empty 
    if type(name) != str or name.strip() == "":
        return None
    # check if player picked a valid class
    if character_class not in VALID_CLASSES:
        return None
    
    level = 1 # all characters start at level 1

    # get base stats for chosen class
    result = calculate_stats(character_class, level)
    if result is None:
        return None
    strength, magic, health = result

    # store all info in one dictionary
    character = {
        "name": name.strip(),
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": 100 # starting gold for all players
    }
    return character

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
    # each class has different starting stats
    if character_class == "Warrior":
        strength, magic, health = 15, 3, 120
    elif character_class == "Mage":
        strength, magic, health = 5, 15, 80
    elif character_class == "Rogue":
        strength, magic, health = 10, 8, 90
    elif character_class == "Cleric":
        strength, magic, health = 8, 12, 110
    else:
        return None # invalid class
    
    # increase stats slightly based on level
    strength = strength + (level - 1) * 2
    magic = magic + (level - 1) * 2
    health = health + (level - 1) * 10

    return (strength, magic, health)

def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    # savess all character info to a file (like a save slot)
    folder = os.path.dirname(filename)
    if folder != "" and not os.path.exists(folder):
        return False # stop if folder doesn't exist
    
    # open file to write text
    file = open(filename, "w", encoding="utf-8")

    # write every piece of info on its own line
    file.write("Character Name: " + character["name"] + "\n")
    file.write("Class: " + character["class"] + "\n")
    file.write("Level: " + str(character["level"]) + "\n")
    file.write("Strength: " + str(character["strength"]) + "\n")
    file.write("Magic: " + str(character["magic"]) + "\n")
    file.write("Health: " + str(character["health"]) + "\n")
    file.write("Gold: " + str(character["gold"]) + "\n")
    
    file.close() # always close after writing
    
    return True

def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    # check if the file exists first
    if not os.path.exists(filename):
        return None

    file = open(filename, "r", encoding="utf-8")
    lines = file.readlines()
    file.close()

    # store data inside a dictionary
    character = {}
    character["name"] = lines[0].replace("Character Name: ", "").strip()
    character["class"] = lines[1].replace("Class: ", "").strip()
    character["level"] = int(lines[2].replace("Level: ", "").strip())
    character["strength"] = int(lines[3].replace("Strength: ", "").strip())
    character["magic"] = int(lines[4].replace("Magic: ", "").strip())
    character["health"] = int(lines[5].replace("Health: ", "").strip())
    character["gold"] = int(lines[6].replace("Gold: ", "").strip())

    return character

def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    print("=== CHARACTER SHEET ===")
    print("Name:", character["name"])
    print("Class:", character["class"])
    print("Level:", character["level"])
    print("Strength:", character["strength"])
    print("Magic:", character["magic"]) 
    print("Health:", character["health"]) 
    print("Gold:", character["gold"]) 


def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # add 1 to the current level
    character["level"] = character["level"] + 1

    # recalculate new stats using calculate_stats
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health

    # display confirmation message
    print("Level up! " + character["name"] + " is not level " + str(character["level"]) + "!")

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
