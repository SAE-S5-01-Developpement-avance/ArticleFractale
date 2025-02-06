import matplotlib
matplotlib.use('TkAgg')  # Set the backend to TkAgg
import matplotlib.pyplot as plt
import numpy as np

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z ** 2 + c
        n += 1
    return n

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    mandelbrot_image = np.empty((width, height))

    for i in range(width):
        for j in range(height):
            c = r1[i] + 1j * r2[j]
            mandelbrot_image[i, j] = mandelbrot(c, max_iter)
    return mandelbrot_image.T

# Paramètres
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
width, height = 1000, 1000
max_iter = 100

# Génération de l'ensemble de Mandelbrot
mandelbrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)

# Affichage
plt.figure(figsize=(10, 10))
plt.imshow(mandelbrot_image, extent=[xmin, xmax, ymin, ymax], cmap='hot')
plt.colorbar(label='Nombre d\'itérations')
plt.title("Ensemble de Mandelbrot")
plt.xlabel("Re(z)")
plt.ylabel("Im(z)")
plt.show()