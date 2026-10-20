"""Project Two starter for the student's text-based adventure game."""

# TODO: # Name: [Jesseca Montanez]
# Course: IT-140 Introduction to Scripting
# Assignment: Project Two (Escape from Castle Ravencrest)


def show_instructions():
    """Display the game objective and available commands."""
    # TODO:   # just basic welcoming messages and rules for how to type choices
    print("Welcome to Escape from Castle Ravencrest!")
    print("Collect all 6 relics before finding Count Dracula.")
    print("To move use: go North, go South, go East, go West")
    print("To grab an item use: get 'item name'")
    print("Type 'exit' if you want to quit the game.")
    print() # blank line for spacing
    pass


def show_status(current_room, inventory, rooms):
    """Display the player's current game status."""
       # simple layout showing current info to the player each loop
    print("----------------------------")
    print("You are in the:", current_room)
    print("Your current inventory:", inventory)
    
    # if an item is still left in this room dictionary, tell the user
    if 'item' in rooms[current_room]:
        print("You see a relic:", rooms[current_room]['item'])
    print("----------------------------")
    pass


def main():
    """Run the main gameplay loop."""
      # my 8-room game map dictionary with connections and items from my storyboard
    rooms = {
        'Grand Foyer': {
            'North': 'Gothic Kitchen',
            'South': 'Forgotten Archive',
            'East': 'Armory Vault',
            'West': 'Servants Quarters'
        },
        'Gothic Kitchen': {
            'South': 'Grand Foyer',
            'East': 'Torture Chamber',
            'item': 'Garlic Necklace'
        },
        'Torture Chamber': {
            'West': 'Gothic Kitchen',
            'item': 'Vampire Stake'
        },
        'Forgotten Archive': {
            'North': 'Grand Foyer',
            'East': 'Obsidian Spire',
            'item': 'Ancient Tome'
        },
        'Obsidian Spire': {
            'West': 'Forgotten Archive',
            'item': 'Silver Crucifix'
        },
        'Armory Vault': {
            'West': 'Grand Foyer',
            'North': 'The Crypt',
            'item': 'Sword of Light'
        },
        'Servants Quarters': {
            'East': 'Grand Foyer',
            'item': 'Holy Water'
        },
        'The Crypt': {
            'South': 'Armory Vault',
            'villain': 'Count Dracula'
        }
    }

    # standard tracking variables to start the game loop
    current_room = 'Grand Foyer'
    inventory = []
    
    # print rules at the beginning
    show_instructions()

    # the game loop runs until they win or lose
    while True:
        show_status(current_room, inventory, rooms)

        # losing condition if you step into the crypt
        if 'villain' in rooms[current_room]:
            print("\nNOM NOM... GAME OVER!")
            print("Count Dracula caught you before you got all the items.")
            print("Thanks for playing the game. Hope you had fun!")
            break

        # winning condition once you have all six items
        if len(inventory) == 6:
            print("\nCongratulations! You have collected all 6 items!")
            print("You defeated Count Dracula and escaped the castle!")
            print("Thanks for playing the game. Hope you had fun!")
            break

        # ask player for input and strip spaces
        user_input = input("Enter your move:\n> ").strip()
        
        # simple check to quit out of the script early
        if user_input.lower() == 'exit':
            print("\nThanks for playing! Goodbye.")
            break

        # split it up so we get the action and the item/direction separate
        input_split = user_input.split(' ', 1)
        
        # error checking for short or weird strings
        if len(input_split) > 0:
            command = input_split[0].lower()
        else:
            command = ""
            
        if len(input_split) > 1:
            argument = input_split[1].title()
        else:
            argument = ""

        # code blocks handling directions
        if command == 'go':
            if argument in rooms[current_room]:
                current_room = rooms[current_room][argument]
                print("\nYou moved to the", current_room)
            else:
                print("\nYou can't go that way!")

        # code blocks handling item pickups
        elif command == 'get':
            if 'item' in rooms[current_room] and argument == rooms[current_room]['item']:
                inventory.append(argument)
                print("\nYou picked up the", argument)
                # clear the item from the room dictionary setup so they can't grab it twice
                del rooms[current_room]['item']
            else:
                print("\nThat item is not here!")

        # error catch for typing something entirely wrong
        else:
            print("\nInvalid command!")

# actual setup script pattern to run main
if __name__ == '__main__':
    main()
