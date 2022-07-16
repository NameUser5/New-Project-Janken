import tkinter as tk


def make_gui():
    window = tk.Tk()
    window.title('Rock, Paper, Scissors!')

    window.geometry('550x400')
    window.config(bg='blue', pady=10, padx=10) #E9FFDB
    window.resizable(False, False)

    prompt = tk.Canvas(width=400, height=50)
    prompt.grid(row=1, column=2, pady=10)

    prompt_text = tk.Label(text="Jan! Ken! Pon!", fg='black')
    prompt_text.grid(row=1, column=2, pady=1)

    card_background = tk.Canvas(width=300, height=70)
    card_background.grid(row=2, column=2, pady=10)

    left_slot = tk.Frame(bg='orange', width=63, height=60)
    left_slot.grid(row=2, column=1, pady=10)

    right_slot = tk.Frame(bg='orange', width=63, height=60)
    right_slot.grid(row=2, column=3, pady=10)

    choose_rock = tk.Button(text='Rock')
    choose_rock.grid(row=3, column=1, padx=2, pady=1)

    choose_paper = tk.Button(text='Paper')
    choose_paper.grid(row=3, column=2, padx=2, pady=1)

    choose_scissors = tk.Button(text='Scissors')
    choose_scissors.grid(row=3, column=3, pady=1)

    clear_choice = tk.Button(text='Clear')
    clear_choice.grid(row=4, column=2, pady=1)



    window.mainloop()