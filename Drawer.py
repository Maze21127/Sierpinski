import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from Settings import Settings


class Drawer:
    def __init__(self, root):
        self.root = root

        self.canvas = None
        self.figure = None
        self.axes = None

    def init_grid(self):
        if self.canvas is not None:
            self.delete_triangle()
        self.figure, self.axes = plt.subplots()
        self.configure_axes()

    def configure_axes(self):
        self.figure.set_figheight(20)
        self.figure.set_figwidth(20)
        plt.axis('off')

    def delete_triangle(self):
        self.canvas.get_tk_widget().pack_forget()
        plt.cla()
        plt.close(self.figure)

    def draw_triangle(self, settings: Settings):
        self.init_grid()
        accuracy = settings.accuracy_var.get()
        self.axes.plot(settings.sierpinski.x_array[0:accuracy], settings.sierpinski.y_array[0:accuracy],
                       settings.triangle_color, markersize=0.1)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack()