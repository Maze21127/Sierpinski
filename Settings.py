import tkinter as tk

from Color import Color
from Sierpinski import Sierpinski


class Settings:
    def __init__(self, root):
        self.root = root
        self.bg_color = "#FFF"

        self.accuracy_scale = None
        self.accuracy_var = None
        self.settings_frame = None
        self.triangle_color_name = None
        self.accuracy_var = None

        self.accuracy = 60000
        self.sierpinski = Sierpinski(self.accuracy)
        self.sierpinski.create_arrays()

        self.triangle_color = Color.blue.value
        self.color_buttons = []

    def init_widgets(self):
        self.accuracy_var = tk.IntVar()
        self.accuracy_scale = tk.Scale(self.root, from_=0, to=self.accuracy, resolution=1000, orient=tk.HORIZONTAL,
                                       length=200, variable=self.accuracy_var, bg=self.bg_color, bd=0)

        self.settings_frame = tk.Frame(self.root, borderwidth=3, bg=self.bg_color)

        self.triangle_color_name = tk.StringVar()
        tk.Label(self.root, text="Accuracy", bg=self.bg_color).pack()
        self.accuracy_scale.pack(pady=5)
        self.settings_frame.pack()

        self.init_buttons()

    def init_buttons(self):
        for color in Color:
            radiobutton = tk.Radiobutton(self.settings_frame,
                                         text=color.name,
                                         value=color.value,
                                         bg=self.bg_color,
                                         variable=self.triangle_color_name)
            radiobutton.pack(side=tk.LEFT)
            radiobutton.deselect()
            self.color_buttons.append(radiobutton)
        self.color_buttons[0].select()

    def change_color(self):
        self.triangle_color = self.triangle_color_name.get()