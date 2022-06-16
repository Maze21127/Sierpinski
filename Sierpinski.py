import random
import math


class Sierpinski:
    def __init__(self, accuracy: int):
        self.accuracy = accuracy
        self._x_array = [0.0]
        self._y_array = [0.0]
        self._create_arrays()

    def _add_next_point(self, x: float, y: float, number: int):
        match number:
            case 0:
                self._x_array.append(x / 2.0)
                self._y_array.append(y / 2.0)
            case 1:
                self._x_array.append((x + 1) / 2.0)
                self._y_array.append(y / 2.0)
            case _:
                self._x_array.append((x + 0.5) / 2)
                self._y_array.append((y + math.sqrt(3)) / 2.0)

    def _create_arrays(self):
        for i in range(self.accuracy):
            self._add_next_point(self._x_array[-1], self._y_array[-1], random.randint(0, 2))

    @property
    def x_array(self):
        return self._x_array

    @property
    def y_array(self):
        return self._y_array



