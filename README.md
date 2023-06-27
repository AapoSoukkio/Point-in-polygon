# Point in polygon

  

**Made by: Aapo Soukkio**

  

## Purpose of this project

  

This is a Python program that checks if a given point is inside or outside a polygon using the ray-casting algorithm. The main objective is to determine the point's position relative to the polygon.

  

## About this project

  

The primary focus of this project is to provide a solution to the common problem of determining whether a given point lies inside or outside a polygon. The ray-casting algorithm is employed to accomplish this task.

  

In addition to the core functionality the project employs the polygenerator module to generate random polygons and utilizes the matplotlib.pyplot module to visualize the polygons and interactively classify points.

  

## How to run

  

To run the program, please follow these steps:

### Prerequisites

-   Ensure that you have Python installed on your computer. You can download it from the official Python website ([https://www.python.org/downloads/](https://www.python.org/downloads/)).

### Run the Program

1.  Clone the repository to your local machine
    
2.  Install the required packages by running the following command:
    
```
pip install polygenerator matplotlib
```
This command will install the `polygenerator` and `matplotlib` packages.

3.  In the command prompt or terminal window, make sure you are still in the directory of the cloned repository.
4.  Run the Python script using the following command:
    
    `point_in_polygon.py` 

#### Output

A plot window will appear showing the random generated polygon. When you click inside the plot window, the program will check if the clicked point is inside or outside the polygon and print the corresponding message ("inside" or "outside") to the console. Green dot will be plotted if the point is inside the polygon, and a red dot if it's outside.