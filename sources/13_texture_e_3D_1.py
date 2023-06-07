# Matplotlib: Visualization with Python
from matplotlib import pyplot as plt

# Grafico 3D gerado a partir da imagem R0_caso1.jpg
momento_angular = 0.0004
entropia = 13.1171
contraste = 297.9365

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(momento_angular, entropia, contraste, c='r', marker='o')
ax.set_xlabel('Momento Angular')
ax.set_ylabel('Entropia')
ax.set_zlabel('Contraste')

plt.savefig('./images_generate/13/R0_caso1_grafico3d.png')
