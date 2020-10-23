#game.py
from click_the_dots import *

def main():
    play=Clilck_the_dots()
    play.intro()
    time=play.gameplay()
    play.outro(time)
    pass


main()