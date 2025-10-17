"""
Filename: text-based_adventure_game.py
Author: <Dylan Mayemba>
Created: <DATE>
Instructor: Holtslander
Description:
    <DESCRIPTION OF THE PROGRAM>
Dependencies: parser
"""

# Import statements
from parser import Parser

# This is a dictionary
# It is a place to store variables you want to use in your story Instead of having to create and manage many different
# variables, we can just store and quickly access them here.
# Inserting a new entry: player_vars["key"] = "value"
# If you want to store a user generated value: player_vars["player"] = input("Please type your name")
# "key" is your variable name and "value" is what you are storing. (It can also be an integer. Just remove the quotes.)
#
# Accessing an entry: player_vars["key"]
# e.g.
# print(player_vars["key"])
#
# You can also overwrite an entry by just assigning a new value e.g.: player_vars["key"] = "value2"
player_vars = {
    "player" : "Henry"
}

# This is the entry point for the program. It the program should start and stop here.
# For now, all your code should be in the main function
def main():
    """
    The entry point and driver of the narrative game program.
    :return: None
    """

    # This creates a new parser object. You can use it to print your text files
    # parser.dprint("example.txt", player_vars, pause=0.1)
    # The dict and pause arguments can be omitted if you do not want a delay and do not want to format the output.
    parser = Parser()

    # Your code goes under this line.
    parser.dprint("the start")
    q1 = input()
    if q1 == "1": #Lawyer

        parser.dprint("lawyer.txt")
        q1 == input()
        if q1 == "1":

            parser.dprint("doctor.txt")
        q1 = input()
    elif q1 == "2": #Doctor

            parser.dprint("")
            q1 == input()
    else:
            parser.dprint("you stay quiet.txt")
            q1 == input()
    else:
        parser.dprint("computer scientist.txt")
        q1 = input()





    # Clean up code. Do not write any code past this line.
    parser.destroy()
    parser = None

# This tells the program to start with the main function.
if __name__ == "__main__":
    main()
