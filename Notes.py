'''https://www.geeksforgeeks.org/looping-through-buttons-in-tkinter/

https://www.youtube.com/watch?v=EPwszp6Ecgs
https://www.geeksforgeeks.org/python-lambda/

https://foodscienceinstitute.com/2020/12/18/rock-paper-scissors-in-python-part-ii-building-a-gui/
'''
# -----------------------------------------------------------------------------------------------------------------------------------------------------------

import random
from tkinter import *
from tkinter import ttk
from api_calls import api_convert
window = Tk()
window.title("Currency Conversion Tool")
tabControl = ttk.Notebook(window)
convert_tab = Frame(tabControl)
rate_tab = Frame(tabControl)
tabControl.add(convert_tab, text='Convert')
tabControl.add(rate_tab, text='Exchange Rates')
tabControl.grid(row=0, column=0)
class Gui:
    def __init__(self):
        # Gui Labels ---------------------------------------------------------------------------------------------------
        self.amount_label = Label(convert_tab, text="Amount:", bg='white', font=('comic sans', 15))
        self.amount_label.grid(row=1, column=0, padx=8, pady=10)
        self.convert_from_label = Label(convert_tab, text="From:", bg='white', font=('comic sans', 15))
        self.convert_from_label.grid(row=1, column=1, padx=10, pady=10)
        self.convert_to_label = Label(convert_tab, text="To:", bg='white', font=('comic sans', 15))
        self.convert_to_label.grid(row=1, column=2, padx=10, pady=10)
        # User Input ---------------------------------------------------------------------------------------------------
        # Amount Entry
        self.amount_entry = Entry(convert_tab, width=12)
        self.amount_entry.grid(row=2, column=0, pady=10)
        # Drop Down Menu Options
        self.options = ["USD", "EUR", "GBP", "INR", "AUD", "CAD", "JPY"]
        # Convert From Drop Down Button
        self.from_selected = StringVar()
        self.from_selected.set("USD")
        self.convert_from_choice = OptionMenu(convert_tab, self.from_selected, *self.options )
        self.convert_from_choice.grid(row=2, column=1)
        # Convert To Drop Down Button
        self.to_selected = StringVar()
        self.to_selected.set("USD")
        self.convert_to_choice = OptionMenu(convert_tab, self.to_selected, *self.options )
        self.convert_to_choice.grid(row=2, column=2)
        # Convert Button
        self.convert = Button(convert_tab, text='Convert', width=25,  command=self.run_convert)
        self.convert.grid(row=3, column=0, pady=10)
        # Conversion Result
        #self.result_display = f"{self.converted_amount} {self.to_selected}"
        self.result_label = Label(convert_tab, text="Click Convert to view converted currency", bg='white', font=('comic sans', 15))
        self.result_label.grid(row=4, column=0, pady=10, columnspan=3)
    def run_convert(self):
        #print(api_convert(self.to_selected.get(), self.from_selected.get(), self.amount_entry.get()))
        self.result_label.config(text=api_convert(self.to_selected.get(), self.from_selected.get(), self.amount_entry.get()))

window.mainloop()

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

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

import tkinter as tk


    # from PIL import Image, ImageTK

    def make_gui():
        window = tk.Tk()
        window.title('Rock, Paper, Scissors!')

        window.geometry('550x400')
        window.config(bg='blue', pady=10, padx=10)  # E9FFDB
        window.resizable(False, False)

        prompt = tk.Canvas(width=400, height=50)
        prompt.grid(row=1, column=2, pady=10)

        prompt_text = tk.Label(text="Jan! Ken! Pon!", fg='black')
        prompt_text.grid(row=1, column=2, pady=1)

        # card_background = tk.Canvas(width=300, height=200)
        # card_background.grid(row=2, column=2, pady=10)

        card_background_photo = tk.PhotoImage(file=r'sprites\Waiting_Question.png')
        card_background_photo = card_background_photo.subsample(3, 3)
        # card_background_photo = tk.resizeImage(card_background_photo,80,80)
        # card_background.create_image(280,80, image=card_background_photo, anchor="center")

        background = tk.Label(image=card_background_photo, bg='blue')
        background.grid(row=2, column=2, pady=10)

        # left_slot = tk.Frame(bg='orange', width=63, height=60)
        # left_slot.grid(row=2, column=1, pady=10)
        #
        # right_slot = tk.Frame(bg='orange', width=63, height=60)
        # right_slot.grid(row=2, column=3, pady=10)

        # Need to solve this
        rock_photo = tk.PhotoImage(file=r'sprites\rock_button.png')
        choose_rock = tk.Button(text='Rock', image=rock_photo, width=50, height=50)
        choose_rock.grid(row=3, column=1, padx=2, pady=1)

        choose_paper = tk.Button(text='Paper')
        choose_paper.grid(row=3, column=2, padx=2, pady=1)

        choose_scissors = tk.Button(text='Scissors')
        choose_scissors.grid(row=3, column=3, pady=1)

        clear_choice = tk.Button(text='Clear')
        clear_choice.grid(row=4, column=2, pady=1)

        window.mainloop()


# import tkinter as tk
#
#
#     # from PIL import Image, ImageTK
#
#     def make_gui():
#         window = tk.Tk()
#         window.title('Rock, Paper, Scissors!')
#
#         window.geometry('550x400')
#         window.config(bg='blue', pady=10, padx=10)  # E9FFDB
#         window.resizable(False, False)
#
#         prompt = tk.Canvas(width=400, height=50)
#         prompt.grid(row=1, column=2, pady=10)
#
#         prompt_text = tk.Label(text="Jan! Ken! Pon!", fg='black')
#         prompt_text.grid(row=1, column=2, pady=1)
#
#         # card_background = tk.Canvas(width=300, height=200)
#         # card_background.grid(row=2, column=2, pady=10)
#
#         card_background_photo = tk.PhotoImage(file=r'sprites\Waiting_Question.png')
#         card_background_photo = card_background_photo.subsample(3, 3)
#         # card_background_photo = tk.resizeImage(card_background_photo,80,80)
#         # card_background.create_image(280,80, image=card_background_photo, anchor="center")
#
#         background = tk.Label(image=card_background_photo, bg='blue')
#         background.grid(row=2, column=2, pady=10)
#
#         # left_slot = tk.Frame(bg='orange', width=63, height=60)
#         # left_slot.grid(row=2, column=1, pady=10)
#         #
#         # right_slot = tk.Frame(bg='orange', width=63, height=60)
#         # right_slot.grid(row=2, column=3, pady=10)
#
#         # Need to solve this
#         rock_photo = tk.PhotoImage(file=r'sprites\rock_button.png')
#         choose_rock = tk.Button(text='Rock', image=rock_photo, width=50, height=50)
#         choose_rock.grid(row=3, column=1, padx=2, pady=1)
#
#         choose_paper = tk.Button(text='Paper')
#         choose_paper.grid(row=3, column=2, padx=2, pady=1)
#
#         choose_scissors = tk.Button(text='Scissors')
#         choose_scissors.grid(row=3, column=3, pady=1)
#
#         clear_choice = tk.Button(text='Clear')
#         clear_choice.grid(row=4, column=2, pady=1)
#
#         window.mainloop()