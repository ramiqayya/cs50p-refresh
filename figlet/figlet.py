from pyfiglet import Figlet
from random import choice
import sys

figlet = Figlet()

# print(len(sys.argv))
accepted = ["-f", "--font"]

if len(sys.argv) == 1:
    input = input("Input: ")
    font1 = choice(figlet.getFonts())
    figlet.setFont(font=font1)

elif len(sys.argv) == 3:
    if sys.argv[1] not in accepted:
        sys.exit("Invalid Usage")
    if sys.argv[2] in figlet.getFonts():
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Invalid Input")
    input = input("Input: ")
else:
    sys.exit("Invalid Input")


print(f"Output: {figlet.renderText(input)}")
