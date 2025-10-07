import random
import os

def prompt_list(prompt_text):
    """Prompt user for multiple items separated by commas."""
    items = input(prompt_text + " (separate multiple items with commas): ")
    return [item.strip() for item in items.split(",") if item.strip()]

def create_god_profile():
    print("\n=== Chaos Magick God Creator ===\n")
    
    # Basic info
    god_name = input("Enter a name for your new God: ").strip()
    god_focus = input("What is the main focus or domain of this God? ").strip()
    
    # Associations
    planets = prompt_list("Which planets is this God associated with?")
    plants = prompt_list("Which plants are associated with this God?")
    animals = prompt_list("Which animals are sacred to this God?")
    symbols = prompt_list("Which symbols represent this God?")
    abode = input("Where does this God reside (abode)? ").strip()
    
    # Ritual materials (randomly enhanced)
    basic_materials = ["candles", "incense", "salt", "water", "stones"]
    ritual_materials = random.sample(basic_materials, k=random.randint(2, len(basic_materials)))
    
    # Ritual instructions (basic template + chaos magic flavor)
    ritual_steps = [
        "Find a quiet space free from distractions.",
        f"Set up a ritual space with: {', '.join(ritual_materials)}.",
        f"Focus your mind on invoking {god_name}, the deity of {god_focus}.",
        "Visualize their power and domain vividly in your mind.",
        f"Optionally, chant or meditate using the symbols: {', '.join(symbols)}.",
        "Once your intent is clear, conclude the ritual and record any visions or feelings."
    ]
    
    # Compose profile
    profile = f"""
==============================
God Name: {god_name}
Focus / Domain: {god_focus}
Abode: {abode}

Associations:
- Planets: {', '.join(planets) if planets else 'None'}
- Plants: {', '.join(plants) if plants else 'None'}
- Animals: {', '.join(animals) if animals else 'None'}
- Symbols: {', '.join(symbols) if symbols else 'None'}

Ritual Instructions:
"""
    for i, step in enumerate(ritual_steps, 1):
        profile += f"{i}. {step}\n"

    profile += "\n==============================\n"
    
    # Display profile
    print(profile)
    
    # Save to file
    file_name = god_name.replace(" ", "_") + "_profile.txt"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(profile)
    print(f"Profile saved to {file_name}\n")

# Run the program
if __name__ == "__main__":
    create_god_profile()

