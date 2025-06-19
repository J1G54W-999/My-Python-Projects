''' 
Weclome to the Spooky Manor game
Room classes are already provided in the spookymanor library.
You just need to import it to use it in your game.
'''
from spookymanor.spookymanor import *

# This block of code defines a room in the manor.
front_porch = Room("Front Porch", "You are standing outside of the manor on the front porch. There's a lock on the door and you notice something under the welcome mat.\n")
hallway = Room("Hallway", "The hallway is dark except for light shining in from underneath the bedroom door.")
kitchen = Room("Kitchen", "The kitchen is full of dirty dishes and is really smelly. You hear something moving around near the oven.")
garage = Room("Garage", "The garage is full of old junk. There's a car in here, but it's covered in a tarp, but it's been moved.")
closet = Room("Closet", "The closet is stuffed full of files and boxes all the way to the ceiling. You can barely fit inside - or can you?")
office = Room("Office", "The office is full of open books and has papers all over the floor. There's a computer on the desk, but it's password protected.")
library = Room("Library", "The library is dark, dusty and very cold - you can see your breath. There are many bookshelves with only one book in the room.")
bedroom = Room("Bedroom", "The bedroom is brightly lit and decorated with stuffed animals and posters for various boy bands.")

# This block of code connects all of the rooms together
hallway.north - closet
hallway.south = front_porch
hallway.east = kitchen
hallway.west = office
kitchen.east = garage
office.north = library
office.west = bedroom

# This block of code defines where keys are located and what room they unlock.
front_porch.add_key_for(hallway)
garage.add_key_for(office)
hallway.add_key_for(closet)
office.add_key_for(bedroom)

# This block of code defines where the player's friends will be hiding.
kitchen.add_friend("Spike")
garage.add_friend("Jet")
closet.add_friend("Faye")

# This line of code defines where a player will start in the game.
set_current_room(front_porch)

# This line of code provides the player with the story and kicks off the game.
enter_the_manor()

# This block of code is the main game loop. It will run forever until the player either wins or loses.
while True:
    print_slow(underline_text("What will you do now?\n"))
    print_slow("You need to find " + str(remaining_friends()) + " more of your friends before you can escape!\n\n")
    action = show_options("Look around for clues", "Move to another room", "Remind me where I am", "I give up. Get me out of here!")
    
    # This block of code checks the player's CHOSEN action and executes the CORRESPONDING actions.
    if action == "Look around for clues":
        get_current_room().look_around()
        if get_current_room() == library:
            print_slow(bold_text("What's that noise?!?\n"))
            found_a_ghost()
            print_slow("Oh no! You ran into the owners of the Manor - ghosts! You run out of the building as fast as you can. \n\nWhen you return back in the morning, you find that the manor has disappeared! \nIn it's place is a pile of rubble and a sign that says 'Coming Soon: Apartments!'\n\nBetter luck next time!")
            quit()
    elif action == "Move to another room":
        get_current_room().show_move_options()
    elif action == "Remind me where I am":
        get_current_room().where_am_i()
    elif action == "I give up. Get me out of here!":
        found_a_ghost()
        print_slow("Oh no! You ran home.\n\nWhen you return back in the morning, you find that the manor has disappeared! \nIn it's place is a pile of rubble and a sign that says 'Coming Soon: Apartments!'\n\nBetter luck next time!")
        quit()

    # If the player is in the bedroom and **still has friends to find**, a message about an open window is displayed, but the player receives a message that they have friends to locate.
    if get_current_room() == bedroom and remaining_friends() > 0:
        print_slow("You see an open window on the bedroom wall.")
        print_slow("Oh no! You can't escape without all of your friends!")
    # If the player is in the bedroom and has found all their friends, a message about escaping through the window is shown, and the game ends.
    elif get_current_room() == bedroom and remaining_friends() == 0:
        print_slow("You see an open window on the bedroom wall.")
        print_slow("You and your friends climb out the window and escape. 🎉🎉 Congratulations - you escaped with your friends and won the game!! 🎉🎉")
        quit()
    # If the player is on the front porch, a message about rain prompts them to enter the Manor.
    if get_current_room() == front_porch:
        print_slow(blue_text("It's starting to rain. "))
        print_slow("Hurry back inside before you get SOAKED!\n\n")
