import matplotlib.pyplot as plt


from Sierpinski import Sierpinski

sierpinski = Sierpinski(accuracy=5000)
x_array = sierpinski.x_array
y_array = sierpinski.y_array


plt.plot(x_array, y_array, "b+", markersize=0.1)
plt.show()
