import tkinter as tk
from tkinter import PhotoImage
from login import LoginPage
import random

class WelcomeScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome to Task Scheduler")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")
        self.root.resizable(True, True)
        self.canvas = tk.Canvas(self.root, width=screen_width, height=screen_height, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.root.bind("<Configure>", self.on_resize)

        # 🌒 Darker background
        self.canvas.create_rectangle(0, 0, screen_width, screen_height, fill="#b0cadc", outline="")

        # 🌈 Darker gradient tones for bubbles
        self.gradient_colors = [
            "#749fd9",  # darker blue
            "#87c2dd",  # deeper teal
            "#a1cc84",  # deeper mint
            "#6da78a",  # darker sage
            "#a788d6"   # deeper lavender
        ]

        self.bubbles = []
        self.create_bubbles(60)
        self.animate_bubbles()

        try:
            self.logo = PhotoImage(file="welcome.jpg")
            self.logo_id = self.canvas.create_image(screen_width // 2, screen_height // 5, image=self.logo)
        except:
            self.logo_id = self.canvas.create_text(
                screen_width // 2, screen_height // 5,
                text="Task Scheduler",
                font=("Segoe UI", 44, "bold"),
                fill="#2e2d42"  # darker text
            )

        self.welcome_text = self.canvas.create_text(
            screen_width // 2, screen_height // 2 - 40,
            text="Welcome!",
            font=("Segoe UI", 36, "bold"),
            fill="#2e2d42"  # darker text
        )
        self.tagline_text = self.canvas.create_text(
            screen_width // 2, screen_height // 2 + 10,
            text="Plan your tasks. Prioritize your life.",
            font=("Segoe UI", 20, "italic"),
            fill="#494a68"  # deeper gray-blue
        )

        self.start_button = tk.Button(self.root, text="Start / Enter",
                                      font=("Segoe UI", 16, "bold"),
                                      bg="#3a5b99", fg="white",
                                      activebackground="#142647",
                                      width=20, relief="flat",
                                      command=self.open_login)
        self.start_button.bind("<Enter>", self.on_hover_enter)
        self.start_button.bind("<Leave>", self.on_hover_leave)
        self.button_window = self.canvas.create_window(screen_width // 2, screen_height // 2 + 80, window=self.start_button)

    def create_bubbles(self, count):
        self.root.update_idletasks()
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        for _ in range(count):
            x = random.randint(0, width)
            y = random.randint(height // 3, height)
            size = random.randint(15, 35)
            color = random.choice(self.gradient_colors)
            bubble = self.canvas.create_oval(x, y, x+size, y+size, fill=color, outline="")
            self.bubbles.append((bubble, size, random.randint(1, 3)))

    def animate_bubbles(self):
        if self.root.winfo_exists():
            for bubble, size, speed in self.bubbles:
                self.canvas.move(bubble, 0, -speed)
                x1, y1, x2, y2 = self.canvas.coords(bubble)
                if y2 < 0:
                    new_x = random.randint(0, self.canvas.winfo_width())
                    new_size = random.randint(15, 35)
                    color = random.choice(self.gradient_colors)
                    self.canvas.coords(bubble, new_x, self.canvas.winfo_height(),
                                       new_x + new_size, self.canvas.winfo_height() + new_size)
                    self.canvas.itemconfig(bubble, fill=color)
            self.root.after(20, self.animate_bubbles)

    def on_resize(self, event):
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        if hasattr(self, 'logo_id'):
            self.canvas.coords(self.logo_id, w//2, h//5)
        self.canvas.coords(self.welcome_text, w//2, h//2 - 40)
        self.canvas.coords(self.tagline_text, w//2, h//2 + 10)
        self.canvas.coords(self.button_window, w//2, h//2 + 80)

    def open_login(self):
        self.root.destroy()
        login_root = tk.Tk()
        login = LoginPage(login_root)
        login_root.mainloop()

    def on_hover_enter(self, event):
        event.widget.config(bg="#2d4a7a")

    def on_hover_leave(self, event):
        event.widget.config(bg="#3a5b99")

if __name__ == "__main__":
    root = tk.Tk()
    app = WelcomeScreen(root)
    root.mainloop()
