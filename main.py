import enum
import tkinter as tk
import sys

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from Sierpinski import Sierpinski


class Color(enum.Enum):
    blue = "b+"
    red = "r+"
    green = "g+"
    cyan = "c+"
    magenta = "m+"
    yellow = "y+"
    black = "k+"


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


class App:
    def __init__(self):
        self.sierpinski = None
        self.root = tk.Tk()
        self.root.title("Sierpinski Triangle")
        self.root.geometry("500x500")
        self.bg_color = "#FFF"
        self.root['bg'] = self.bg_color

        self.root.protocol("WM_DELETE_WINDOW", lambda: self.__close())

        self.canvas = None
        self.figure = None
        self.axes = None

        self.settings = Settings(self.root)
        self.settings.init_widgets()
        self.add_commands()

        self.sierpinski = Sierpinski(self.settings.accuracy)
        self.sierpinski.create_arrays()

        self.draw_triangle()

        self.root.mainloop()

    def add_commands(self):
        self.settings.accuracy_scale.configure(command=lambda _: self.draw_triangle())
        for button in self.settings.color_buttons:
            button.configure(command=lambda: self.change_color())

    def change_color(self):
        self.settings.change_color()
        self.draw_triangle()

    def delete_triangle(self):
        self.canvas.get_tk_widget().pack_forget()
        plt.cla()
        plt.close(self.figure)

    def configure_axes(self):
        self.figure.set_figheight(20)
        self.figure.set_figwidth(20)
        plt.axis('off')

    def init_plt_items(self):
        if self.canvas is not None:
            self.delete_triangle()
        self.figure, self.axes = plt.subplots()
        self.configure_axes()

    def draw_triangle(self):
        self.init_plt_items()
        accuracy = self.settings.accuracy_var.get()
        self.axes.plot(self.sierpinski.x_array[0:accuracy], self.sierpinski.y_array[0:accuracy],
                       self.settings.triangle_color, markersize=0.1)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack()

    def __close(self):
        self.delete_triangle()
        sys.exit(0)


app = App()
