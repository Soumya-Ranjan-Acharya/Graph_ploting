import matplotlib.pyplot as plt

# Get number of data points
n = int(input("Enter number of data points: "))

# Get X and Y data   Ploting_Graph
x = []
y = []
print("Enter X and Y values:")

for i in range(n):
    xi = float(input(f"X[{i+1}]: "))
    yi = float(input(f"Y[{i+1}]: "))
    x.append(xi)
    y.append(yi)

# Plot the graph
plt.plot(x, y, marker='o', color='b', label='Data Line')
plt.title("User Input Data Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)

# Show the graph
plt.show()
