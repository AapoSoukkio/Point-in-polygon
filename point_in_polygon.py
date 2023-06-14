from polygenerator import random_polygon
import matplotlib.pyplot as plt


polygon = random_polygon(num_points=20)
polygon.append(polygon[0])
x_coordinates, y_coordinates = zip(*polygon)
plt.plot(x_coordinates, y_coordinates, color="black", linestyle="-", linewidth=0.8)
plt.show()

edge_pairs = list(zip(polygon, polygon[1:] + polygon[:1]))
