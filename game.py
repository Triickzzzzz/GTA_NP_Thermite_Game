import tkinter as tk
import tkinter.font as tkFont
import random

class Game(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="black")
        self.parent = parent
        self.pack(fill=tk.BOTH, expand=True)
        self.bind_all("<Key>", self.on_key_press)
        self.letters = ["Q","W","E","J","K","L"]
        self.failures, self.score, self.times_pressed = 0, 0, 0
        self.pressed_correctly = False

        self.setup_game_screen()
        self.place_letter()
        self.after(1500, self.update)

    def setup_game_screen(self):
        lbl_head = tk.Label(self, bg="black", text="Proof Your Skill", font=self.setup_font(12), fg="white")
        self.cnv_board = tk.Canvas(self, bg="black", highlightthickness=0)
        self.lbl_fails = tk.Label(self, bg="black", text="[ - ]  [ - ]  [ - ]", font=self.setup_font(20), fg="white")

        lbl_head.pack(fill=tk.X)
        self.cnv_board.pack(fill=tk.BOTH, expand=True)
        self.lbl_fails.pack(fill=tk.X)   
        self.draw_canvas_board()

    def draw_canvas_board(self):
        self.cnv_board.update()
        cnvs_height = self.cnv_board.winfo_height()
        cnvs_width = self.cnv_board.winfo_width()

        self.cnv_board.create_rectangle(0+5, 0, cnvs_width/3-5, cnvs_height, fill="red")
        self.cnv_board.create_rectangle(cnvs_width/3+5, 0, cnvs_width*2/3-5, cnvs_height, fill="green")
        self.cnv_board.create_rectangle(cnvs_width*2/3+5, 0, cnvs_width-5, cnvs_height, fill="blue")

        self.cnv_board.create_rectangle(0+7, 400, cnvs_width/3-7, 470, width=3, outline="white")
        self.cnv_board.create_rectangle(cnvs_width/3+7, 400, cnvs_width*2/3-7, 470, width=3, outline="white")
        self.cnv_board.create_rectangle(cnvs_width*2/3+7, 400, cnvs_width-7, 470, width=3, outline="white")

    def setup_font(self, size):
        return tkFont.Font(family="Helvetica",size=size,weight="bold")

    def place_letter(self):
        self.letter = self.get_random_letter()
        self.pos_x = self.get_random_position()
        self.pos_y = 25
        self.cnv_board.create_text(self.pos_x, self.pos_y, text=self.letter, font=self.setup_font(50), tag="letter")

    def move_letter(self):
        self.pos_y = self.pos_y + 25
        self.cnv_board.coords(self.cnv_board.find_withtag("letter"), (self.pos_x, self.pos_y))

    def get_random_letter(self):
        position = random.randrange(0, len(self.letters), 1)
        return self.letters[position]

    def get_random_position(self):
        position = random.randrange(0, 3, 1)
        if position == 0:
            return 60
        elif position == 1:
            return 200
        return 330

    def on_key_press(self, e):
        if self.times_pressed == 1:
            return
        elif self.pos_y > 380 and self.pos_y < 570:
            if e.keysym == self.letter.lower():
                self.pressed_correctly = True
                self.times_pressed = 1
                return
        self.pressed_correctly = False
        self.times_pressed = 1

    def update(self):
        if self.check_failures():
            if self.times_pressed == 1 and self.pressed_correctly == True:
                self.cnv_board.delete("letter")
                self.place_letter()
                self.times_pressed = 0
                self.score = self.score + 1
                self.pressed_correctly = False
            elif self.pos_y < 600:
                self.move_letter()
            elif self.pos_y >= 600:
                self.failures = self.failures + 1
                if not self.failures == 4:
                    self.cnv_board.delete("letter")
                    self.place_letter()
                    self.pressed_correctly = False
                    self.times_pressed = 0
        else:
            self.cnv_board.delete("letter")
            txt_end = f"Game Done\n  Score: {self.score}"
            self.cnv_board.create_text(200, 100, fill="white", text=txt_end, font=self.setup_font(40))
            return

        self.after(40, self.update)

    def check_failures(self):
        if self.failures >= 4:
            return False
        elif self.failures == 1:
            self.lbl_fails.config(text="[ X ]  [ - ]  [ - ]")
        elif self.failures == 2:
            self.lbl_fails.config(text="[ X ]  [ X ]  [ - ]")   
        elif self.failures == 3:
            self.lbl_fails.config(text="[ X ]  [ X ]  [ X ]")
        return True

