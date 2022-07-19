import tkinter as tk
import game_logic as gl
import random
# from PIL import Image, ImageTK


def make_gui():
    window = tk.Tk()
    window.title('Rock, Paper, Scissors!')

    window.geometry('580x400')
    window.config(bg='#0935ce', pady=10, padx=10) #082eaf
    window.resizable(False, False)

    banner = tk.Canvas(width=400, height=50)
    banner.grid(row=1, column=2, pady=10)

    banner_text = tk.Label(text="Jan! Ken! Pon!", fg='black')
    banner_text.grid(row=1, column=2, pady=1)

    card_background_photo = tk.PhotoImage(file=r'sprites\Waiting_Question.png')  # change this to list w idx
    card_background_photo = card_background_photo.subsample(3, 3)

    background = tk.Label(image=card_background_photo, bg='#0935ce') #082eaf
    background.grid(row=2, column=2, pady=10)

# # # All photos, to be used for label changes (see https://replit.com/@CadetJ/Week12?v=1#gui.py) # # #
#     def resize_sprites(list):     # DOES NOT WORK! Instead, add indexed list of files to the card_backround variable
#         for _ in list:
#             _ = _.subsample(3, 3)
#             return list

    ## Waiting for cpu choice ##
    loading_both = tk.PhotoImage(file=r'sprites\Waiting_Question.png')
    rock_loading = tk.PhotoImage(file=r'sprites\Rock_Question.png')
    paper_loading = tk.PhotoImage(file=r'sprites\Paper_Question.png')
    scissors_loading = tk.PhotoImage(file=r'sprites\Scissors_Question.png')

    # loading_sprites = [loading_both, rock_loading, paper_loading, scissors_loading]
    # resize_sprites(loading_sprites)  # DOES NOT WORK!
    
    ## Results ##
    rock_win = tk.PhotoImage(file=r'sprites\Rock_Win_Result.png')
    rock_lose = tk.PhotoImage(file=r'sprites\Rock_Lose_Result.png')
    rock_draw = tk.PhotoImage(file=r'sprites\Rock_Draw_Result.png')

    # rock_results = [rock_win, rock_lose, rock_draw]
    # resize_sprites(rock_results)  # DOES NOT WORK!

    paper_win = tk.PhotoImage(file=r'sprites\Paper_Win_Result.png')
    paper_lose = tk.PhotoImage(file=r'sprites\Paper_Lose_Result.png')
    paper_draw = tk.PhotoImage(file=r'sprites\Paper_Draw__Result.png')

    # paper_results = [paper_win, paper_lose, paper_draw]
    # resize_sprites(paper_results)  # DOES NOT WORK!
    
    scissors_win = tk.PhotoImage(file=r'sprites\Scissors_Win_Result.png')
    scissors_lose = tk.PhotoImage(file=r'sprites\Scissors_Lose_Result.png')
    scissors_draw = tk.PhotoImage(file=r'sprites\Scissors_Draw_Result.png')

    # scissors_results = [scissors_win, scissors_lose, scissors_draw]
    # resize_sprites(scissors_results)  # DOES NOT WORK!
    
    you_win_banner = tk.PhotoImage(file=r'sprites\Victory text.png')
    you_lose_banner = tk.PhotoImage(file=r'sprites\Defeat text.png')

# # # Need to add functions to buttons, and timer (with loading animation) # # #
    click = True

    # gambits = [ROCK, PAPER, SCISSORS]

    def cpu_choice():
        choice = random.choice(gl.gambits)
        return choice

    def user_choice(choice):
        global click

        cpu_current = cpu_choice()


    rock_photo = tk.PhotoImage(file= r'sprites\rock_button.png')
    rock_photo = rock_photo.subsample(6, 6)
    choose_rock_button = tk.Button(text='Rock', image=rock_photo, command=lambda: user_choice('r'), width=72, height=55)
    choose_rock_button.grid(row=3, column=1, pady=1)

    paper_photo = tk.PhotoImage(file=r'sprites\paper_button.png')
    paper_photo = paper_photo.subsample(6, 6)
    choose_paper_button = tk.Button(text='Paper', image=paper_photo, command=lambda: user_choice('p'), width=72, height=55)
    choose_paper_button.grid(row=3, column=2, pady=1)

    scissors_photo = tk.PhotoImage(file=r'sprites\scissors_button.png')
    scissors_photo = scissors_photo.subsample(8, 8)
    choose_scissors_button = tk.Button(text='Scissors', image=scissors_photo, command=lambda: user_choice('s'), width=72, height=55)
    choose_scissors_button.grid(row=3, column=3, pady=1)

    quit_game = tk.Button(text='Quit', command=window.destroy)
    quit_game.grid(row=4, column=2, pady=1)


    window.mainloop()