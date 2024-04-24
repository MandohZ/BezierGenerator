import numpy as np
import matplotlib.pyplot as plt

# Define control points scaled and translated to fit desired plot range
P0 = np.array([5, 2])   
P1 = np.array([10, 5])   
P2 = np.array([5, 8])   

# Define the Bezier curve function
def bezier_curve(t, P0, P1, P2):
    return (1 - t)**2 * P0 + 2 * t * (1 - t) * P1 + t**2 * P2

# Evaluate the curve on [0, 1] sliced in 50 points
# Smoothness of the curve can be controlled by adjusting the slice value
t_values = np.linspace(0, 1, 50)
points = np.array([bezier_curve(t, P0, P1, P2) for t in t_values])

# Get x and y coordinates of points separately
x = points[:, 0]
y = points[:, 1]

# Plotting on a custom range [1, 10] for both x and y axes
plt.figure(figsize=(8, 8))  # Set the figure size (optional)
plt.xlim(1, 10)  # Set x-axis range
plt.ylim(1, 10)  # Set y-axis range

# Plot the Bezier curve
plt.plot(x, y, 'k-', label='Bezier Curve')

# Plot the control points
plt.plot(P0[0], P0[1], 'ro', label='P0')
plt.plot(P1[0], P1[1], 'go', label='P1')
plt.plot(P2[0], P2[1], 'bo', label='P2')

# Annotate control points with their coordinates
plt.text(P0[0], P0[1], f'({P0[0]}, {P0[1]})', verticalalignment='bottom', horizontalalignment='right')
plt.text(P1[0], P1[1], f'({P1[0]}, {P1[1]})', verticalalignment='bottom', horizontalalignment='right')
plt.text(P2[0], P2[1], f'({P2[0]}, {P2[1]})', verticalalignment='bottom', horizontalalignment='left')

# Add labels and legend
plt.xlabel('X')
plt.ylabel('Y', rotation = 0)
plt.title('Quadratic Bezier Curve')
plt.legend()
plt.axis('on')
#plt.savefig('C:\\Users\Mando\ForStimuliGenImages/spyder_bezier.png', dpi=300, transparent = True)  # Specify file name and DPI (optional)


# Show the plot
plt.grid(True)  # Add grid for better visualization (optional)
plt.show()
