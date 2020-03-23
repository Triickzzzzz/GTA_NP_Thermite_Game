import tkinter as tk
from game import Game

def main(app):
    app.title("Thermite Game")
    app.geometry("400x600")
    app.resizable(False, False)
    Game(app)
    app.mainloop()

if __name__ == "__main__":
    app = tk.Tk()
    main(app)