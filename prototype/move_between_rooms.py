"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}



# Theme: Gothic Vampire Horror

rooms = {
    'Grand Foyer': {
        'North': 'Torture Chamber',
        'South': 'Servants Quarters',
        'West': 'Forgotten Archive'
    },
    'Forgotten Archive': {
        'East': 'Grand Foyer',
        'South': 'Obsidian Spire'
    },
    'Obsidian Spire': {
        'North': 'Forgotten Archive'
    },
    'Torture Chamber': {
        'South': 'Grand Foyer',
        'East': 'Armory Vault'
    },
    'Armory Vault': {
        'West': 'Torture Chamber'
    },
    'Servants Quarters': {
        'North': 'Grand Foyer',
        'East': 'Gothic Kitchen'
    },
    'Gothic Kitchen': {
        'West': 'Servants Quarters',
        'North': 'The Crypt'
    },
    'The Crypt': {
        'South': 'Gothic Kitchen'
    }
}

# 1. Initialize starting room location
current_room = 'Grand Foyer'

print("--- Welcome to Escape from Castle Ravencrest ---")
print("Commands: North, South, East, West, or Exit\n")

# 2. Gameplay loop
while current_room != 'exit':
    # Output that displays the room the player is currently in
    print(f"You are currently standing in: {current_room}")
    
    # Prompt the player for their command input
    command = input("Enter your move command: ").strip().title()
    print("-" * 40)  # Visual divider for clean text flow
    
    # Handle the "exit" command requirement
    if command == 'Exit':
        current_room = 'exit'
        print("You fled Castle Ravencrest in terror!")
        
    # Check if the entered direction is valid for the current room
    elif command in rooms[current_room]:
        # Update current room using the dictionary map layout
        current_room = rooms[current_room][command]
        print(f"You move cautiously {command} into the darkness...")
        
    # Input validation: Output an error message for invalid commands
    else:
        print("A heavy iron gate bars that path! You cannot move in that direction.")
        print("Please check your available paths and try again.")
    print()  # Empty line for formatting

print("Thank you for playing! The gameplay loop has terminated safely.")

# TODO: Run and debug all milestone cases in prototype/README.md.
