ROCK = "r"
PAPER = "p"
SCISSORS = "s"


draw = 0
win = 1
lose = -1


def find_status(user_gambit, cpu_gambit):
    status = -5
    if user_gambit == ROCK:
        if cpu_gambit == ROCK:
            status = draw
        elif cpu_gambit == PAPER:
            status = lose
        else:
            status = win
    elif user_gambit == PAPER:
        if cpu_gambit == ROCK:
            status = win
        elif cpu_gambit == PAPER:
            status = draw
        else:
            status = lose
    elif user_gambit == SCISSORS:
        if cpu_gambit == ROCK:
            status = lose
        elif cpu_gambit == PAPER:
            status = win
        else:
            status = draw
    else:
        print('really.....!!')
    return status
