import random
from game_logic import find_status as fs
from gui import *
import game_logic


gui = make_gui()



flag = True
score = 0

while flag:
    # user_input = input(f"Choose: R - P - S \n").lower()
    ROCK = "r"
    PAPER = "p"
    SCISSORS = "s"
    #
    gambits = [ROCK, PAPER, SCISSORS]
    #
    # cpu_choice = random.choice(gambits)
    # print(cpu_choice)

# # # I am unsure as to where to place these two functions: in the main, logic file, or GUI??? # # #
    def cpu_choice():
        choice = random.choice(gambits)
        return choice

    def user_choice(choice):
        global click

        cpu_current = cpu_choice()

    # Choices #
    # if user_input == rock:
    #     if cpu_choice == rock:
    #         status = draw
    #     elif cpu_choice == paper:
    #         status = lose
    #     else:
    #         status = win
    # elif user_input == paper:
    #     if cpu_choice == rock:
    #         status = win
    #     elif cpu_choice == paper:
    #         status = draw
    #     else:
    #         status = lose
    # elif user_input == scissors:
    #     if cpu_choice == rock:
    #         status = lose
    #     elif cpu_choice == paper:
    #         status = win
    #     else:
    #         status = draw
    # else:
    #     print('really.....!!')

    curr_status = fs(user_choice, cpu_choice)

    if curr_status == game_logic.WIN:
        # print("You won!")
        gui.banner_text.configure(image=gui.you_win_banner)
        score +=1
    elif curr_status == game_logic.LOSE:
        # print("You lost. :(")
        gui.banner_text.configure(image=gui.you_lose_banner)
        score -=1
    elif curr_status == game_logic.DRAW:
        # print("It's a draw. Try again!")
        gui.banner_text.configure(text="It's a draw. Try again!", image='')
        score +=0
