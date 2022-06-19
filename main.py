import tkinter as tk
from Sierpinski import Sierpinski
import enum

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class Color(enum.Enum):
    blue = "b+"
    red = "r+"
    green = "g+"
    cyan = "c+"
    magenta = "m+"
    yellow = "y+"
    black = "k+"


class App:
    def __init__(self):
        self.sierpinski = None
        self.root = tk.Tk()
        self.root.title("Sierpinski Triangle")
        self.root.geometry("500x500")
        self.bg_color = "#FFF"
        self.root['bg'] = self.bg_color

        tk.Label(self.root, text="Accuracy", bg=self.bg_color).pack()

        self.canvas = None
        self.figure = None
        self.axes = None

        self.triangle_color = Color.black.value

        self.accuracy = 60000
        self.sierpinski = Sierpinski(self.accuracy)
        self.sierpinski.create_arrays()

        self.accuracy_var = tk.IntVar()

        self.accuracy_scale = tk.Scale(self.root, from_=0, to=self.accuracy, resolution=1000, orient=tk.HORIZONTAL,
                                       length=200, variable=self.accuracy_var, command=lambda _: self._draw_triangle(),
                                       bg=self.bg_color, bd=0)
        self.accuracy_scale.pack(pady=5)

        self.settings = tk.Frame(self.root, borderwidth=3, bg=self.bg_color)
        self.settings.pack()

        self.triangle_color_name = tk.StringVar()
        self._init_buttons()

        self.x_array = self.sierpinski.x_array
        self.y_array = self.sierpinski.y_array

        self._draw_triangle()

        self.root.mainloop()

    def _init_buttons(self):
        color_buttons = []
        for color in Color:
            radiobutton = tk.Radiobutton(self.settings,
                                         text=color.name,
                                         value=color.value,
                                         bg=self.bg_color,
                                         variable=self.triangle_color_name, command=lambda: self._change_color())
            radiobutton.pack(side=tk.LEFT)
            radiobutton.deselect()
            color_buttons.append(radiobutton)
        color_buttons[0].select()

    def _change_color(self):
        self.triangle_color = self.triangle_color_name.get()
        self._draw_triangle()

    def _init_triangle(self):
        self.x_array = self.sierpinski.x_array
        self.y_array = self.sierpinski.y_array
        self._draw_triangle()

    def _delete_triangle(self):
        self.canvas.get_tk_widget().pack_forget()
        plt.cla()
        plt.close(self.figure)

    def _configure_axes(self):
        self.figure.set_figheight(20)
        self.figure.set_figwidth(20)
        plt.axis('off')

    def _init_plt_items(self):
        if self.canvas is not None:
            self._delete_triangle()
        self.figure, self.axes = plt.subplots()
        self._configure_axes()

    def _draw_triangle(self):
        self._init_plt_items()
        accuracy = self.accuracy_var.get()
        self.axes.plot(self.x_array[0:accuracy], self.y_array[0:accuracy], self.triangle_color, markersize=0.1)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack()


app = App()
