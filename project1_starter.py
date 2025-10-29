"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Jelani Campbell
Date: 10/25/25

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""

VALID_CLASSES = ["Warrior", "Mage", "Rogue", "Cleric"]

def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    # TODO: 
    if type(name) != str or name.strip() == "":
        return None

    if character_class not in VALID_CLASSES:
        return None
    
    level = 1

    stats = calculate_stats(character_class, level)

    character = {
        "name": name.strip(),
        "class": character_class,
        "level": level,
        "strength": stats["strength"],
        "magic": stats["magic"],
        "health": stats["magic"],
        "gold": stats["gold"]
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
    # TODO: Implement this function
    if character_class == "Warrior":
        strength = 15
        magic = 3
        health = 120
    elif character_class == "Mage":
        strength = 5
        magic = 15
        health = 80
    elif character_class == "Rogue":
        strength = 10
        magic = 8
        health = 90
    elif character_class == "Cleric":
        strength = 8
        magic = 12
        health = 120 
    else:
        return None
    
    strength = strength + (level - 1) * 2
    magic = magic + (level - 1) * 2
    health = health + (level - 1) * 10

    gold = 100

    stats = {
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }

    return stats

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
    file = open(filename, "w")

    file.write("Character Name: " + character["name"] + "\n")
    file.write("Class: " + character["class"] + "\n")
    file.write("Level: " + str(character["level"]) + "\n")
    file.write("Strength: " + str(character["strength"]) + "\n")
    file.write("Magic: " + str(character["magic"]) + "\n")
    file.write("Health: " + str(character["health"]) + "\n")
    file.write("Gold: " + str(character["gld"]) + "\n")
    
    file.close()
    
    return True

def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
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
    character["level"] = character["level"] + 1

    new_stats = calculate_stats(character["class"], character["level"])

    character["strength"] = new_stats["strength"]
    character["magic"] = new_stats["magic"]
    character["health"] = new_stats["health"]
    character["gold"] = new_stats["gold"]

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
