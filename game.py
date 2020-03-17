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

        #=====Main objects=====#
        lbl_head = tk.Label(self, bg="white", text="Proof Your Skill", font=helv12)
        frame_board = tk.Frame(self, bg="white")
        lbl_fails = tk.Label(self, bg="white", text="[ - ]  [ - ]  [ - ]", font=helv20)

        lbl_head.pack(fill=tk.X)
        frame_board.pack(fill=tk.BOTH, expand=True)
        lbl_fails.pack(fill=tk.X)

        #=====Board objects=====#        
        lbl_blue = tk.Label(frame_board, bg="RoyalBlue1")
        lbl_red = tk.Label(frame_board, bg="tomato")
        lbl_green = tk.Label(frame_board, bg="medium sea green")

        lbl_blue.pack(fill=tk.BOTH, expand=True, side=tk.LEFT, padx=(10,5), pady=10)
        lbl_red.pack(fill=tk.BOTH, expand=True, side=tk.LEFT, padx=(5,5), pady=10)
        lbl_green.pack(fill=tk.BOTH, expand=True, side=tk.LEFT, padx=(5,10), pady=10)



