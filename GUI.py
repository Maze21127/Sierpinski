import tkinter as tk
from Sierpinski import Sierpinski

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.sierpinski = None
        self.root = tk.Tk()
        self.root.title("Sierpinski Triangle")
        self.root.geometry("500x500")

        self.button = tk.Button(master=self.root, height=2, width=10, text="Plot")
        self.button.pack()

        self.figure = plt.Figure(figsize=(6, 5), dpi=100)
        self.x_plot = self.figure.add_subplot(111)
        self.y_plot = self.figure.add_subplot(111)

        self.init_triangle(accuracy=5000)

    def run(self):
        self.root.mainloop()

    def init_triangle(self, accuracy: int):
        self.sierpinski = Sierpinski(accuracy=accuracy)
        self.x_plot.plot(self.sierpinski.x_array)
        self.y_plot.plot(self.sierpinski.y_array)

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        #self.canvas.draw()
        self.canvas.get_tk_widget().pack()




app = App()
app.run()