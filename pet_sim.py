import tkinter as tk
from tkinter import ttk

from pet import Pet


class VirtualPetGame:
    def __init__(self, window):
        self.pet = None
        self.game_running = False
        self.window = window
        self.window.title("My Virtual Pet Sim")
        self.window.geometry("500x700")
        self.window.resizable(False, False)
        self.window.configure(bg="#B8D9E0")
        self.show_start_screen()

    def show_start_screen(self):
        padding = 15

        tk.Label(self.window, font=("Arial", 25), bg="#B8D9E0", text="Welcome!!!").pack(
            pady=padding
        )
        tk.Label(
            self.window,
            font=("Arial", 20),
            bg="#B8D9E0",
            text="Let's adopt a new pet!!!\nEnter your pet's name:",
        ).pack(pady=padding)

        self.name_entry = tk.Entry(self.window, font=("Arial", 20), justify="center")
        self.name_entry.insert(0, "Kiki")
        self.name_entry.pack()

        tk.Label(
            self.window, font=("Arial", 20), bg="#B8D9E0", text="Choose your pet type:"
        ).pack(pady=padding)

        self.pet_type = ttk.Combobox(
            self.window,
            values=["Dog", "Cat", "Bird"],
            font=("Arial", 20),
            state="readonly",
            justify="center",
        )
        self.pet_type.current(0)
        self.pet_type.pack(pady=padding)

        tk.Button(
            self.window,
            text="Start Game",
            font=("Arial", 20, "bold"),
            width=20,
            height=2,
            command=self.start_game,
        ).pack(pady=padding)

    def start_game(self):
        self.pet = Pet(self.name_entry.get(), self.pet_type.get())
        self.game_running = True
        self.show_game_screen()
        self.schedule_timer()

    # ======
    # show_game_screen
    # ======

    def clear_screen(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def update_game_screen(self):
        pet_emoji = {"Dog": "🐶", "Cat": "🐱", "Bird": "🐦"}[self.pet.pet_type]
        mood, emoji = self.pet.get_mood()
        self.mood_label.config(text=f"{pet_emoji} {mood} {emoji}")
        self.mood_label.pack()

    def show_game_screen(self):

        self.clear_screen()

        # static
        tk.Label(
            self.window,
            text=f"Hello. {self.pet.name}!",
            font=("Arial", 20),
            bg="#B8D9E0",
        ).pack(pady=15)

        # dynamic
        self.mood_label = tk.Label(
            self.window, text="mood here", font=("Arial", 20), bg="#B8D9E0"
        )

        pet_emoji = {"Dog": "🐶", "Cat": "🐱", "Bird": "🐦"}[self.pet.pet_type]
        mood, emoji = self.pet.get_mood()
        self.mood_label.config(text=f"{pet_emoji} {mood} {emoji}")
        self.mood_label.pack()

        status_frame = tk.Frame(self.window).pack()

        self.bars = {}
        status_data = [
            ("Hunger", "hunger", "#E67E22"),
            ("Happiness", "happiness", "#E84393"),
            ("Energy", "energy", "#0984E3"),
        ]

        for title, key, clr in status_data:
            row = tk.Frame(status_frame)
            row.pack()

            tk.Label(row, text=title, font=("Arial", 15), bg="#B8D9E0").pack(
                side="left"
            )

            bar = ttk.Progressbar(
                row,
                length=200,
                maximum=100,
            )
            bar.pack(side="left")

            value_label = tk.Label(row, text="", font=("Arial", 10), bg="#E87345")
            value_label.pack(side="left")

            self.bars[key] = (bar, value_label)

    def game_tick(self):
        if not self.game_running:
            return

        print("game ticking!")
        self.timer_id = None
        self.pet.pass_time()  # 배고파지고, 기분 안좋아지고, 피곤해짐
        print(
            f"current pet status: hunger:{self.pet.hunger} energy:{self.pet.energy} happiness:{self.pet.happiness}"
        )

        self.update_game_screen()
        self.check_game_stauts()
        self.schedule_timer()

    def schedule_timer(self):
        if self.game_running:
            self.timer_id = self.window.after(5000, self.game_tick)
            print(self.timer_id)

    def check_game_stauts(self):
        if not self.pet.is_alive():
            self.game_running = False
            self.mood_label.config(text="💔 GAME OVER 💔", font=("Arial", 30, "bold"))


# ======
# run app
# ======

window = tk.Tk()
game = VirtualPetGame(window)
window.mainloop()
