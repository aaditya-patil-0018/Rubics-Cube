from matplotlib.patches import Polygon
import matplotlib.pyplot as plt


class face:

    def __init__(self, v1, v2, v3, v4, color):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4
        self.color = color
        self.figure = plt.gca()
        self.figure.add_patch(Polygon([v1, v2, v3, v4],
                                      closed=True, facecolor=color, fill=True, edgecolor=None))

    def update_color(self, color):
        self.color = color
        self.figure.add_patch(Polygon([self.v1, self.v2, self.v3, self.v4],
                                      closed=True, facecolor=color, fill=True, edgecolor=None))
