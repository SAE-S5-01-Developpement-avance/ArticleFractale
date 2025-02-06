import numpy as np
import matplotlib.pyplot as plt

def floconVonKoch(order, start, end):
    if order == 0:
        return [start, end]
    else:
        points = []
        start = np.array(start)
        end = np.array(end)

        segment = (end - start) / 3
        p1 = start + segment
        p3 = start + 2 * segment
        
        # Compute the peak of the equilateral triangle
        angle = np.pi / 3  # 60 degrees
        rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
        p2 = p1 + np.dot(rotation_matrix, segment)
        
        # Recursively compute smaller segments
        points += floconVonKoch(order - 1, start, p1)[:-1]
        points += floconVonKoch(order - 1, p1, p2)[:-1]
        points += floconVonKoch(order - 1, p2, p3)[:-1]
        points += floconVonKoch(order - 1, p3, end)
        
        return points

# Pour un triangle
def plot_koch(order):
    p1 = np.array([0, 0])
    p2 = np.array([0.5, np.sqrt(3)/2])
    p3 = np.array([1, 0])
    
    points =  floconVonKoch(order, p1, p2)
    points += floconVonKoch(order, p2, p3)[1:]
    points += floconVonKoch(order, p3, p1)[1:]
    
    points = np.array(points)
    
    plt.figure(figsize=(8, 8))
    plt.plot(points[:, 0], points[:, 1], 'b')
    plt.axis('equal')
    plt.xticks([])
    plt.yticks([])
    plt.gca().set_frame_on(False)
    plt.title(f"Flocon de von Koch - Itération {order}")
    plt.show()

# Afficher les différentes étapes
iterations = 8
for i in range(iterations + 1):
    plot_koch(i)
