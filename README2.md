# COMP 163 — Project 1: Character Creator & Chronicles  
Jelani Campbell  
Introduction to Computer Programming (COMP 163)  
Fall 2025  

---

## Game Concept
**Character Creator & Chronicles** is a text-based RPG setup phase. When the player begins: they create a character by entering a name and selecting a class. The classes
`Warrior`, `Mage`, `Rogue`, and `Cleric` have different base stats and playstyles. Each character
has: name, class, level, strength, magic, health, and gold. These are stored inside a dictionary, which
acts like the player’s save file.

---

## Design Choices
- **Class Identity:**  
  - *Warrior:* high strength & health, low magic  
  - *Mage:* high magic, lower health, low strength  
  - *Rogue:* balanced strength/magic, moderate health  
  - *Cleric:* support-style, medium strength, high magic/health
- **Stat Formulas (scales with level):**  
  - `strength = base_strength + (level - 1) * 2`  
  - `magic    = base_magic    + (level - 1) * 2`  
  - `health   = base_health   + (level - 1) * 10`  
  These keep level 1 as the **base** (no bonus) and give linear, easy-to-explain growth that feels fair across classes.
- **Data Model:** One **dictionary** per character for simple access (`character["strength"]`, etc.).  
- **Function Boundaries:**  
  - `create_character()` builds the dict  
  - `calculate_stats()` returns a **tuple** `(strength, magic, health)` for clean unpacking  
  - `save_character()` / `load_character()` handle persistence  
  - `display_character()` prints a clean sheet  
  - `level_up()` increments level and reuses `calculate_stats()` (no duplicate logic)

## Bonus Creative Features
- **UTF-8 Save/Load Support:** Names with accents/emojis are saved correctly (opened files with `encoding="utf-8"`).  
- **Safer File Operations:** Checks for valid paths before saving; returns helpful values (`True`/`False` or `None`) instead of crashing.  
- **Readable Character Sheet:** Console output mirrors a classic RPG sheet for easy testing and presentation.

## AI Usage
I used AI to help **format** the `save_character()` function with the correct file methods (`open`, `write`, `close`) and UTF-8 encoding, with short explanations and examples. I also used AI to **debug early errors** while shaping the concept and to **professionally format this README**. All final code, logic choices, and testing were completed and verified by me, **Jelani Campbell**.

## How to Run
1. **Install/activate Python** (Windows PowerShell examples below).
2. **Run tests** (from the project root):
   ```bash
   py -m pytest