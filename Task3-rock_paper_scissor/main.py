from tkinter import *
import random

choices = ["Rock", "Paper", "Scissor"]

def button_click(user_choice):
    comp_choice = random.choice(choices)
    if user_choice == comp_choice:
        choice_label.config(text=comp_choice, font=('Time new Roman', 12, 'bold'))
        win_loose.config(text="Match Draw!", font=('Time new Roman', 15, 'bold'))
    elif user_choice == "Paper" and comp_choice == "Rock" or user_choice == "Rock" and comp_choice == "Scissor" or user_choice == "Scissor" and comp_choice == "Paper":
        choice_label.config(text=comp_choice, font=('Time new Roman', 12, 'bold'))
        win_loose.config(text="You Win!", font=('Time new Roman', 15, 'bold'))
    else:
        choice_label.config(text=comp_choice, font=('Time new Roman', 12, 'bold'))
        win_loose.config(text="You loose!", font=('Time new Roman', 15, 'bold'))
    

window = Tk()
window.title("Rock Paper scissor")
window.geometry("500x300")

label = Label(window, text="Rock paper scissor", font=('Time new Roman', 15, 'bold'))
label.pack()

paper_btn_image = PhotoImage(file="paper.png")
rock_btn_image = PhotoImage(file="rock.png")
scissor_btn_image = PhotoImage(file="scissor.png")

paper_btn = Button(image=paper_btn_image, highlightthickness=0, bd=0, command=lambda: button_click("Paper"))
paper_btn.place(x=70, y=50)

rock_btn = Button(image=rock_btn_image, highlightthickness=0, bd=0,  command=lambda: button_click("Rock"))
rock_btn.place(x=240, y=50)

scissor_btn = Button(image=scissor_btn_image, highlightthickness=0, bd=0,  command=lambda: button_click("Scissor"))
scissor_btn.place(x=400, y=50)



computer_choice_label = Label(window, text="Computer Choice: ", font=('Time new Roman', 12, 'bold'))
computer_choice_label.place(x=150, y=150)

choice_label = Label(window, text="", font=('Time new Roman', 12, 'bold'))
choice_label.place(x=300, y=150)

win_loose = Label(window, text="", font=('Time new Roman', 15, 'bold'))
win_loose.place(x=210, y=200)

window.mainloop()
