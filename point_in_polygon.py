from polygenerator import random_polygon
import matplotlib.pyplot as plt
import tkinter as tk
import tkinter.font as tkfont
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def is_inside(edge_pairs, xp, yp):
    cnt = 0
    for edge in edge_pairs:
        (x1, y1), (x2, y2) = edge
        if (yp < y1) != (yp < y2) and xp < x1 + ((yp - y1) / (y2 - y1)) * (x2 - x1):
            cnt += 1
    return cnt % 2 == 1

def onclick(event):
    xp, yp = event.xdata, event.ydata
    if is_inside(edge_pairs, xp, yp):
        print("inside")
        output_text.insert(tk.END, "inside\n")
        plot_figure.gca().plot(xp, yp, "go", markersize=5)
    else:
        print("outside")
        output_text.insert(tk.END, "outside\n")
        plot_figure.gca().plot(xp, yp, "ro", markersize=5)
    plot_canvas.draw()

def refresh_polygon():
    global polygon, edge_pairs

    output_text.delete(1.0, tk.END)

    polygon = random_polygon(num_points=20)
    polygon.append(polygon[0])
    edge_pairs = list(zip(polygon, polygon[1:] + polygon[:1]))

    plot_figure.clf()
    plot_figure.gca().set_aspect("equal")
    x_coordinates, y_coordinates = zip(*polygon)
    plot_figure.gca().plot(x_coordinates,
             y_coordinates,
             color="black",
             linestyle="-",
             linewidth=0.8)
    plot_canvas.draw()

polygon = random_polygon(num_points=20)
polygon.append(polygon[0])
edge_pairs = list(zip(polygon, polygon[1:] + polygon[:1]))

root = tk.Tk()
root.title("Polygon App")

frame = tk.Frame(root)
frame.pack(pady=10)

output_text = tk.Text(frame, height=10, width=30)
output_text.pack(side=tk.LEFT, padx=10)

refresh_button = tk.Button(frame, text="Refresh", command=refresh_polygon, bg="blue", fg="white", width=10, height=2)
refresh_button.pack(side=tk.LEFT)

plot_figure = plt.figure(figsize=(7, 6))
plot_canvas = FigureCanvasTkAgg(plot_figure, master=root)
plot_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

plot_figure.gca().set_aspect("equal")
x_coordinates, y_coordinates = zip(*polygon)
plot_figure.gca().plot(x_coordinates,
         y_coordinates,
         color="black",
         linestyle="-",
         linewidth=0.8)
plot_canvas.draw()

plot_canvas.mpl_connect('button_press_event', onclick)

root.mainloop()
