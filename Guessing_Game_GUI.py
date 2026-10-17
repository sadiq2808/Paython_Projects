import tkinter as tk
from tkinter import messagebox
import random


class SadiqGuessingGame:
    def __init__(self,root):
        self.root=root
        self.root.title("Sadiq Guessing Game 🕹️")
        self.root.geometry("650x500")
        self.root.resizable(False,False)

        self.score=0

        self.root.configure(bg="#1FBC1F")
        
        title=tk.Label(
            root,
            text="SADIQ GUESSING GAME",
            font=("Arial",22,"bold"),
            bg="#000001",
            fg="gold"

       )
        title.pack(pady=15)

        self.info=tk.Label(
            root,
            text="Chooes the lucky Number!🤔",
            font=("Arial",15,"bold"),
            bg="#000001",
            fg="white"
        )

        self.info.pack()

        self.score_label=tk.Label(
            root,
            text="💯Score:0",
            font=("Arial",14,"bold"),
            bg="#1E3A5F",
            fg="yellow"
        )

        self.score_label.pack(pady=10)

        self.frame=tk.Frame(root,bg="#09E799")
        self.frame.pack(pady=40)

        self.message=tk.Label(
            root,
            text="Good Luck!",
            font=("Arial",16,"bold"),
            bg="#AC05A1",
            fg="#4CAF50"
        )

        self.message.pack()

        self.new_btn=tk.Button(
            root,
            font=("Arial",12,"bold"),
            bg="#FF9800",
            fg="white",
            width=15,
            command=self.new_game
        )
        self.new_btn.pack(pady=20)

        self.buttons=[]
        self.new_game()

    def new_game(self):

        
        self.numbers = random.sample(range(1, 150), 4)
        self.secret_number=random.choice(self.numbers)

        for btn in self.buttons:
            btn.destroy()
        self.buttons.clear()
        

        for i , number in enumerate(self.numbers):

            btn=tk.Button(
                self.frame,
                text=str(number),
                font=("Arial",18,"bold"),
                width=10,
                height=3,
                bg="#4FC3F7",
                fg="white",
                activebackground="#2196F3",
                cursor="hand2",
                command=lambda n=number:self.check_answer(n)
            )

            row=i//2
            col=i%2
            btn.grid(row=row, column=col, padx=15, pady=15)
            self.buttons.append(btn)
        self.message.config(text="Choose a Number!")


    def check_answer(self, number):
        win_messages=[
            "AMAZING!",
            "EXCELLENT!",
            "WELL DONE!",
             "GREAT JOB!",
             "CHAMPION"
        ]

        lose_message=[
             "Wrong Choose"
         
        ]

        if number==self.secret_number:
            self.score+=1
            self.score_label.config(
             text=f"Score:{self.score}"
         )

            msg=random.choice(win_messages)
            self.message.config(
             text=msg,
             fg="lime"
         )
            again=messagebox.askyesno(
                 "Winner",
                f"{msg}\n\n Correct Choice!\n\nPlay Again?"
            )   
            if again:
             self.new_game()
            else:
             self.root.destroy()
        else:
            msg=random.choice(lose_message)
            self.message.config(
                text=msg,
                fg="red"
            )
            messagebox.showerror(
                "Wrong Choice",
                msg
            )

root=tk.Tk()
game=SadiqGuessingGame(root)
root.mainloop()