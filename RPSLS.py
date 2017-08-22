import random

#List of Helper Functions
choice_list = [
    "Rock",
    "Spock",
    "Paper",
    "Lizard",
    "Scissors"
]

choice_map = {}

# Adds an enumerate object to iterate in the list
for num, choice in enumerate(choice_list):
    choice_map[choice] = num
    print(choice_map)

def name_to_number(name):
    return choice_map[name]

def number_to_name(number):
    return choice_list[number]

def rpsls(player_choice):

    # Used to print a blank line inorder to separate two games
    print()

    #Prints the message from Player's choice on the command line
    print('Player chooses', player_choice)

    #Converts the Player's choice to Number using the function number_to_name()
    player_number = name_to_number(player_choice)

    # Computer just guesses for a random integer
    comp_number = random.randrange(5)

    # Converts computer's number to a name with the help of the function name_to_number()
    comp_choice = number_to_name(comp_number)

    #Print the Computer's choice
    print('Computer chooses', comp_choice)

    # Computes the difference
    dif = (player_number - comp_number) % 5

    # Used if else loop to decide the winner of the game
    if dif == 0:
        print("Player and Computer tie!!")
    elif dif < 3:
        print("Player wins!!")
    else:
        print("Computer Wins!!")

rpsls("Rock")
rpsls("Spock")
rpsls("Paper")
rpsls("Lizard")
rpsls("Scissors")