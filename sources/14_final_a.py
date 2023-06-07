# Instalar pacote com `pip3 install pillow`
from PIL import Image
# The fundamental package for scientific computing with Python
import numpy as np
# Matplotlib: Visualization with Python
from matplotlib import pyplot as plt

# Carregar a imagem
original_image = Image.open('./images_original/14/Mandrill.jpg')

# Converter para escala de cinza
grayscale_image = original_image.convert('L')

# Converter a imagem para um array NumPy
grayscale_array = np.array(grayscale_image)

# Adicionar ruído gaussiano à imagem
mean = 0
stddev = 20
noisy_array = grayscale_array + np.random.normal(mean, stddev, grayscale_array.shape)

# Garantir que os valores estejam dentro do intervalo válido (0-255)
noisy_array = np.clip(noisy_array, 0, 255)

# Converter o array de volta para uma imagem PIL
noisy_image = Image.fromarray(noisy_array.astype(np.uint8))

# Exibir a imagem original e a imagem com ruído
fig, axes = plt.subplots(1, 2)
axes[0].imshow(original_image)
axes[0].set_title('Imagem Original')
axes[0].axis('off')
axes[1].imshow(noisy_image, cmap='gray')
axes[1].set_title('Imagem com Ruído Gaussiano')
axes[1].axis('off')

plt.savefig('./images_generate/14/atividadefinal_a.png')
