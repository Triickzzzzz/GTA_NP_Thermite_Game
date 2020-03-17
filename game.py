import tkinter as tk
import tkinter.font as tkFont

class Game(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="black")
        self.parent = parent
        self.pack(fill=tk.BOTH, expand=True)
        self.setup_game_screen()

    def setup_game_screen(self):
        helv12 = tkFont.Font(family="Helvetica",size=12,weight="bold")
        helv20 = tkFont.Font(family="Helvetica",size=20,weight="bold")

        lbl_head = tk.Label(self, bg="white", text="Proof Your Skill", font=helv12)
        frame_board = tk.Frame(self, bg="black")
        lbl_fails = tk.Label(self, bg="white", text="[ - ]  [ - ]  [ - ]", font=helv20)

        lbl_head.pack(fill=tk.X)
        frame_board.pack(fill=tk.BOTH, expand=True)
        lbl_fails.pack(fill=tk.X)
        

