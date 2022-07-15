import random
from game_logic import find_status as fs
from gui import make_gui
import game_logic


gui = make_gui()



flag = True

while flag:
    user_input = input(f"Choose: R - P - S \n").lower()
    rock = "r"
    paper = "p"
    scissors = "s"

    gambits = [rock, paper, scissors]

    cpu_choice = random.choice(gambits)
    print(cpu_choice)

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

    curr_status = fs(user_input, cpu_choice)

    if curr_status == game_logic.win:
        print("You won!")
    elif curr_status == game_logic.lose:
        print("You lost. :(")
    elif curr_status == game_logic.draw:
        print("It's a draw. Try again!")

