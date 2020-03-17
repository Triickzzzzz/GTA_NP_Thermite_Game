import tkinter as tk
from game import Game

app = tk.Tk()
app.title("Thermite Game")
app.geometry("400x600")
app.resizable(False, False)

g_frame = Game(app)
app.mainloop()