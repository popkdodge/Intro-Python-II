from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
print('Welcome~!')

print("Welcome to exciting mansion treasure hunt game!")

name = input("What is your name? \n")
player1 = Player(name, room=room['outside'])
user_input = input("""
Press Enter to start!
""")

while user_input != 'q':
    print('==================================')
    print('Location:', player1.location.name)
    print('----------------------------------\n')
    print("Description:")
    print(player1.location.descripiton ,'\n')
    print("Make a Selection!", player1.name)
    try:
        user_input = input("""
        [1] Go North \n
        [2] Go South \n
        [3] Go East \n
        [4] Go West \n
        [q] Quit!
        """)
    except:
        print('Invalid input! Try agian!')
    if user_input == 1:
        new_location = player1.location.n_to
        if new_location == ' ':
            print('+++++++++++++++++++++++++++++++++++')
            print("Not a Valid!! Direction! TRY AGIAN!")
            print('+++++++++++++++++++++++++++++++++++')
        else: 
            player1.location = player1.location.n_to
    
    if user_input == 2:
        new_location = player1.location.s_to
        if new_location == ' ':
            print('+++++++++++++++++++++++++++++++++++')
            print("Not a Valid!! Direction! TRY AGIAN!")
            print('+++++++++++++++++++++++++++++++++++')
        else: 
            player1.location = player1.location.s_to

    if user_input == 3:
        new_location = player1.location.e_to
        if new_location == ' ':
            print('+++++++++++++++++++++++++++++++++++')
            print("Not a Valid!! Direction! TRY AGIAN!")
            print('+++++++++++++++++++++++++++++++++++')
        else: 
            player1.location = player1.location.e_to
    
    if user_input == 4:
        new_location = player1.location.w_to
        if new_location == ' ':
            print('+++++++++++++++++++++++++++++++++++')
            print("Not a Valid!! Direction! TRY AGIAN!")
            print('+++++++++++++++++++++++++++++++++++')
        else: 
            player1.location = player1.location.w_to

       
        
        


# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.