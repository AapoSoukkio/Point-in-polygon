from polygenerator import random_polygon
import matplotlib.pyplot as plt


polygon = random_polygon(num_points=20)
polygon.append(polygon[0])
xs, ys = zip(*polygon)
plt.plot(xs, ys, "b-", linewidth=0.8)
plt.show()

