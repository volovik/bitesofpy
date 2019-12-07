VALID_COLORS = ['blue', 'yellow', 'red']
def print_colors():
    """In the while loop ask the user to enter a color,
       lowercase it and store it in a variable. Next check:
       - if 'quit' was entered for color, print 'bye' and break.
       - if the color is not in VALID_COLORS, print 'Not a valid color' and continue.
       - otherwise print the color in lower case."""
    while True:
        USER_COLOR = input("Type your color pls...")
        USER_COLOR = USER_COLOR.lower()
        done_str = str("quit")
        if USER_COLOR in VALID_COLORS:
            print(USER_COLOR)

        elif USER_COLOR == done_str :
            print("bye")
            exit()
        else :
            print('Not a valid color')
    return
# print_colors()