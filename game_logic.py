import gui as g

ROCK = "r"
PAPER = "p"
SCISSORS = "s"

# def user_choice(user_input):
#     if user_input == ROCK:

gambits = [ROCK, PAPER, SCISSORS]

DRAW = 0
WIN = 1
LOSE = -1


def find_status(user_gambit, cpu_gambit):
    status = -5
    if user_gambit == ROCK:
        if cpu_gambit == ROCK:
            status = DRAW
            g.background.configure(image=g.rock_draw)
        elif cpu_gambit == PAPER:
            status = LOSE
        else:
            status = WIN
    elif user_gambit == PAPER:
        if cpu_gambit == ROCK:
            status = WIN
        elif cpu_gambit == PAPER:
            status = DRAW
        else:
            status = LOSE
    elif user_gambit == SCISSORS:
        if cpu_gambit == ROCK:
            status = LOSE
        elif cpu_gambit == PAPER:
            status = WIN
        else:
            status = DRAW
    # else:
    #     print('really.....!!')
    return status
