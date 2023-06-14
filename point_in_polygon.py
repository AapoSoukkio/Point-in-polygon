from polygenerator import random_polygon
import matplotlib.pyplot as plt

def onclick(event):
    xp, yp = event.xdata, event.ydata
    plt.plot(xp, yp, "go", markersize=5)
    plt.gcf().canvas.draw()


polygon = random_polygon(num_points=20)
polygon.append(polygon[0])
edge_pairs = list(zip(polygon, polygon[1:] + polygon[:1]))
plt.figure(figsize=(10, 10))
plt.gca().set_aspect("equal")
x_coordinates, y_coordinates = zip(*polygon)
plt.gcf().canvas.mpl_connect('button_press_event', onclick)
plt.plot(x_coordinates, y_coordinates, color="black", linestyle="-", linewidth=0.8)
plt.show()



