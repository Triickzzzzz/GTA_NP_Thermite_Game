import tkinter as tk

class Game(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="black")
        self.parent = parent
        self.pack(fill=tk.BOTH, expand=True)
        self.setup_game_screen()

    def setup_game_screen(self):
        pass


