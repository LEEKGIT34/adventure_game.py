# This program is a text-based adventure game where the player makes choices to find treasure.

print("Adventure Game setup successful!")

def start_game():
    print("Welcome to the Adventure Game!")
    name = input("What is your name, adventurer? ")
    print(f"Hello, {name}! Your quest for treasure begins now.")
    choice = input("Would you like to explore the forest or enter the cave? ").lower()

    if choice == "forest":
        forest_path()
    elif choice == "cave":
        cave_path()

def forest_path():
    print("You enter a dark forest with glowing plant life.")
    forest_choice = input("Do you want to follow the river or climb a tree? ").lower()
    if forest_choice == "river":
        print("You follow the river and find a hidden waterfall with sparkling gems!")        
    else:
        print("You climb the tree and find a nest with golden eggs!")
def cave_path():
    print("You enter a dimly lit cave with shiny crystals on the walls.")
    cave_choice = input("Do you want to light a torch or proceed in the dark? ").lower()
    if cave_choice == "torch":
        print("You light a torch and see a path leading to a treasure room!")
    else:
        print("You proceed and lose your way in the tunnel")

while True:
    start_game()
    play_again = input("Do you want to play again? (yes/no) ")
    if play_again.lower() != "yes":
        print("Thank you for playing! Goodbye!")
        break