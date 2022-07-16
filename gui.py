import tkinter as tk
# from PIL import Image, ImageTK


def make_gui():
    window = tk.Tk()
    window.title('Rock, Paper, Scissors!')

    window.geometry('580x400')
    window.config(bg='blue', pady=10, padx=10) #E9FFDB
    window.resizable(False, False)

    prompt = tk.Canvas(width=400, height=50)
    prompt.grid(row=1, column=2, pady=10)

    prompt_text = tk.Label(text="Jan! Ken! Pon!", fg='black')
    prompt_text.grid(row=1, column=2, pady=1)

    card_background_photo = tk.PhotoImage(file= r'sprites\Waiting_Question.png')
    card_background_photo = card_background_photo.subsample(3,3)

    background = tk.Label(image=card_background_photo, bg='blue')
    background.grid(row=2, column=2, pady=10)

# Need to add functions to buttons
    rock_photo = tk.PhotoImage(file= r'sprites\rock_button.png')
    rock_photo = rock_photo.subsample(6, 6)
    choose_rock_button = tk.Button(text='Rock', image=rock_photo, width=72, height=55)
    choose_rock_button.grid(row=3, column=1, pady=1)

    paper_photo = tk.PhotoImage(file=r'sprites\paper_button.png')
    paper_photo = paper_photo.subsample(6, 6)
    choose_paper_button = tk.Button(text='Paper', image=paper_photo, width=72, height=55)
    choose_paper_button.grid(row=3, column=2, pady=1)

    scissors_photo = tk.PhotoImage(file=r'sprites\scissors_button.png')
    scissors_photo = scissors_photo.subsample(8, 8)
    choose_scissors_button = tk.Button(text='Scissors', image=scissors_photo, width=72, height=55)
    choose_scissors_button.grid(row=3, column=3, pady=1)

    clear_choice = tk.Button(text='Clear')
    clear_choice.grid(row=4, column=2, pady=1)


    window.mainloop()