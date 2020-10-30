#Clear screen
print(u"\u001B[2J", u"\u001B[0;0H")

#setup for cursor
ANSI_RED  = u"\u001B[31m"
ANSI_GREEN  = u"\u001B[32m"
ANSI_YELLOW  = u"\u001B[33m"
ANSI_BLUE = u"\u001B[34m"

#Clear screen
print(u"\u001B[2J", u"\u001B[0;0H")
#print colors
print(ANSI_RED,   "Red")
print(ANSI_GREEN, "Green")
print(ANSI_YELLOW, "Yellow")
print(ANSI_BLUE, "Blue")

#setup for cursor
BUILDER_ESCAPE        = "\033["
SAVE_CURSOR           = "\033[s"
RESTORE_CURSOR        = "\033[u"

#print message at coordinates
print(SAVE_CURSOR)
row = str(4)
col = str(15)
message_move = "r"+row+";"+"c"+col
cursor_move = BUILDER_ESCAPE + row + ";" + col + "H"
print(cursor_move, message_move)
print(RESTORE_CURSOR)