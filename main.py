import random

'''Placeholder for GUI choice'''

flag = True

while flag:
    user = input(f"Choose: R - P - S \n").lower()
    rock = "r"
    paper = "p"
    scissors = "s"

    gambits = [rock,paper,scissors]

    cpu_choice = random.choice(gambits)

    print(cpu_choice)

    draw = 0
    win = 1
    lose = -1

    # Choices #
    if input == rock:
        if cpu_choice == rock:
            status = draw
        elif cpu_choice == paper:
            status = lose
        elif cpu_choice == scissors:
            status = win
    elif input == paper:
        if cpu_choice == rock:
            status = win
        elif cpu_choice == paper:
            status = draw
        elif cpu_choice == scissors:
            status = lose
    elif input == scissors:
        if cpu_choice == rock:
            status = lose
        elif cpu_choice == paper:
            status = win
        elif cpu_choice == scissors:
            status = draw

    if status == win:
        print("You won!")
    elif status == lose:
        print("You lost. :(")
    elif status == draw:
        print("It's a draw. Try again!")