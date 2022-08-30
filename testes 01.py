# Plotting example

import ti_plotlib as plt

# Set up the graph window

plt.window(-10, 10, -10, 10)

plt.axes("on")

plt.grid(1, 1, "dashed")

# Add leading spaces to position the title

plt.title("                TITLE")

# Set the pen style and the graph color

plt.pen("medium", "solid")

plt.color(28, 242, 221)

plt.line(-5, 5, 5, -5, "arrow")

plt.pen("thin", "dashed")

plt.color(224, 54, 243)

plt.line(-5, -5, 5, 5, "")

# Scatter plot from 2 lists

plt.color(0, 0, 0)

xlist = [1, 2, 3, 4, 5]

ylist = [5, 4, 3, 2, 1]

plt.scatter(xlist, ylist, "x")


