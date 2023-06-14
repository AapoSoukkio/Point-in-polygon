from polygenerator import random_polygon
import matplotlib.pyplot as plt


def is_inside(edge_pairs, xp, yp):
    cnt = 0
    for edge in edge_pairs:
        (x1, y1), (x2, y2) = edge
        if (yp < y1) != (yp < y2) and xp < x1 + ((yp-y1)/(y2-y1))*(x2-x1):
            cnt += 1
    return cnt%2 == 1


def onclick(event):
    xp, yp = event.xdata, event.ydata
    if is_inside(edge_pairs, xp, yp):
        print("inside")
        plt.plot(xp, yp, "go", markersize=5)
    else:
        print("outside")
        plt.plot(xp, yp, "ro", markersize=5)
    plt.draw()


polygon = random_polygon(num_points=20)
polygon.append(polygon[0])
edge_pairs = list(zip(polygon, polygon[1:] + polygon[:1]))
plt.figure(figsize=(10, 10))
plt.gca().set_aspect("equal")
x_coordinates, y_coordinates = zip(*polygon)
plt.gcf().canvas.mpl_connect('button_press_event', onclick)
plt.plot(x_coordinates, y_coordinates, color="black", linestyle="-", linewidth=0.8)
plt.show()



