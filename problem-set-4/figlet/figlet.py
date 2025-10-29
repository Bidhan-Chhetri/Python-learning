import sys
import random
from pyfiglet import Figlet


get_str = input("Input: ")
figlet = Figlet()
if len(sys.argv) == 3:
    if sys.argv[1] in ["-f", "--font"]:
        font = sys.argv[2]
        if font in figlet.getFonts():
            figlet.setFont(font=font)
            print(figlet.renderText(get_str))
        else:
            sys.exit()
else:
    font = random.choice(figlet.getFonts())
    figlet.setFont(font=font)
    print(figlet.renderText(get_str))

# import sys
# from pyfiglet import Figlet

# get_str = input("Input: ")
# figlet = Figlet()

# if len(sys.argv) == 3:
#     if sys.argv[1] in ["-f", "--font"]:
#         font = sys.argv[2]
#         if font in figlet.getFonts():
#             figlet.setFont(font=font)
#             print(figlet.renderText(get_str))
#         else:
#             sys.exit("Invalid font name.")
# else:
#     print(figlet.renderText(get_str))  # Use default font