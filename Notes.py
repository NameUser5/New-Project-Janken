import random

'''Placeholder for GUI'''

flag = True

user = input(f"Choose: R - P - S \n").lower()
rock = "r"
paper = "p"
scissors = "s"

gambits = [rock, paper, scissors]

# cpu_choice = random.choice(gambits)

while flag:

    cpu_choice = random.choice(gambits)

    score = 0

    draw = 0
    win = 1
    lose = -1

    # Choices #
    status = -5
    if input == rock:
        cpu_choice = random.choice(gambits)
        print(cpu_choice)
        if cpu_choice == rock:
            status = draw
            print("It's a draw. Try again!")
        elif cpu_choice == paper:
            status = lose
            print("You lost. :(")
        else:
            status = win
            print("You won!")
    elif input == paper:
        if cpu_choice == rock:
            status = win
            print("You won!")
        elif cpu_choice == paper:
            status = draw
            print("It's a draw. Try again!")
        else:
            status = lose
            print("You lost. :(")
    elif input == scissors:
        if cpu_choice == rock:
            status = lose
            print("You lost. :(")
        elif cpu_choice == paper:
            status = win
            print("You won!")
        else:
            status = draw
            print("It's a draw. Try again!")

    # else:
    #   print("R-P-S only")
    # if status == win:
    #     print("You won!")
    #   #increment tally here, to your score variable
    # elif status == lose:
    #     print("You lost. :(")
    # else:
    #     print("It's a draw. Try again!")