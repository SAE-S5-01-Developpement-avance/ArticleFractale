import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def sierpinski_tetrahedron(vertices, order):
    """
    Recursively generate the vertices of a Sierpiński tetrahedron.

    Args:
        vertices (list): List of four 3D points defining a tetrahedron.
        order (int): The recursion depth.

    Returns:
        list: List of tetrahedra vertices.
    """
    if order == 0:
        return [vertices]

    midpoints = [(vertices[i] + vertices[j]) / 2 for i in range(4) for j in range(i + 1, 4)]

    return (sierpinski_tetrahedron([vertices[0], midpoints[0], midpoints[1], midpoints[2]], order - 1) +
            sierpinski_tetrahedron([vertices[1], midpoints[0], midpoints[3], midpoints[4]], order - 1) +
            sierpinski_tetrahedron([vertices[2], midpoints[1], midpoints[3], midpoints[5]], order - 1) +
            sierpinski_tetrahedron([vertices[3], midpoints[2], midpoints[4], midpoints[5]], order - 1))


def plot_sierpinski_tetrahedron(order):
    """
    Plot a 3D Sierpiński tetrahedron using Matplotlib.

    Args:
        order (int): The recursion depth.
    """
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d', elev=0, azim=90)


    # Define initial tetrahedron vertices
    v0 = np.array([0, 0, 0])
    v1 = np.array([1, 0, 0])
    v2 = np.array([0.5, np.sqrt(3) / 2, 0])
    v3 = np.array([0.5, np.sqrt(3) / 6, np.sqrt(2 / 3)])

    tetrahedra = sierpinski_tetrahedron([v0, v1, v2, v3], order)

    for tetra in tetrahedra:
        faces = [
            [tetra[0], tetra[1], tetra[2]],
            [tetra[0], tetra[1], tetra[3]],
            [tetra[0], tetra[2], tetra[3]],
            [tetra[1], tetra[2], tetra[3]]
        ]
        ax.add_collection3d(Poly3DCollection(faces, alpha=1, edgecolor='k'))

    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.set_zlim([0, 1])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.title(f'Sierpiński Tetrahedron (Order {order})')
    plt.show()


if __name__ == "__main__":
    for order in range(3):  # Generate orders 0 to 2
        print(f"Creating Sierpiński Tetrahedron of Order {order}...")
        plot_sierpinski_tetrahedron(order)
