import sys
import tkinter as tk

from Settings import Settings
from Drawer import Drawer


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sierpinski Triangle")
        self.root.geometry("500x500")
        self.bg_color = "#FFF"
        self.root['bg'] = self.bg_color

        self.root.protocol("WM_DELETE_WINDOW", lambda: self.__close())

        self.drawer = Drawer(self.root)

        self.settings = Settings(self.root)
        self.settings.init_widgets()
        self.add_commands()

        self.draw_triangle()

        self.root.mainloop()

    def add_commands(self):
        self.settings.accuracy_scale.configure(command=lambda _: self.draw_triangle())
        for button in self.settings.color_buttons:
            button.configure(command=lambda: self.change_color())

    def change_color(self):
        self.settings.change_color()
        self.draw_triangle()

    def draw_triangle(self):
        self.drawer.draw_triangle(self.settings)

    def __close(self):
        self.drawer.delete_triangle()
        sys.exit(0)


app = App()
