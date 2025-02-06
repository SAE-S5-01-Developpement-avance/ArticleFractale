from itertools import product
import matplotlib.pyplot as plt
import numpy as np


def create_menger_sponge(order):
    """
    Generate a Menger sponge of given order.
    Returns a 3D numpy array where True represents solid cubes and False represents empty space.
    """
    size = 3 ** order  # The sponge has dimensions (3^order) x (3^order) x (3^order)
    sponge = np.ones((size, size, size), dtype=bool)  # Initialize a 3D array with all cubes present

    def should_remove(x, y, z):
        """
        Determines if a cube at position (x, y, z) should be removed.
        A cube should be removed if it is in the center of a 3x3x3 block.
        """
        while x > 0 or y > 0 or z > 0:
            # Check if the cube is in the middle of any face
            if (x % 3 == 1 and y % 3 == 1) or \
                    (y % 3 == 1 and z % 3 == 1) or \
                    (z % 3 == 1 and x % 3 == 1):
                return True  # The cube should be removed
            x //= 3  # Move to the next larger cube level
            y //= 3
            z //= 3
        return False  # The cube remains

    # Iterate through each position in the 3D grid
    for x in range(size):
        for y in range(size):
            for z in range(size):
                if should_remove(x, y, z):
                    sponge[x, y, z] = False  # Mark the cube as removed

    return sponge


def plot_menger_sponge_3d(sponge):
    """
    Create a 3D visualization of the Menger sponge using Matplotlib.

    Args:
        sponge (numpy.ndarray): 3D array representing the Menger sponge
    """
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')  # Create a 3D plot

    # Get coordinates of filled (solid) cubes
    x, y, z = np.where(sponge)

    # Use ax.voxels to visualize the 3D Menger sponge
    ax.voxels(sponge, facecolors='blue', edgecolors='k', alpha=0.8)

    # Set equal aspect ratio for proper visualization
    ax.set_box_aspect([1, 1, 1])

    # Label axes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Set plot title with the order of the sponge
    plt.title(f'Menger Sponge (Order {int(np.log(len(sponge)) / np.log(3))})')

    return fig, ax


if __name__ == "__main__":
    # Generate and visualize Menger sponges for orders 0, 1, and 2
    for order in range(3):
        print(f"Creating Menger Sponge of Order {order}...")
        sponge = create_menger_sponge(order)  # Generate the sponge
        fig, ax = plot_menger_sponge_3d(sponge)  # Plot the sponge
        plt.show()  # Display the 3D plot
