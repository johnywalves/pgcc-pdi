import numpy as np
import scipy.signal
import matplotlib.pyplot as plt
from PIL import Image

# Carregar a imagem de entrada
input_image = Image.open("img/Mandrill.jpg")

# Converter a imagem em um array numpy
image_array = np.array(input_image)

# Converter a imagem para escala de cinza (se necessário)
if len(image_array.shape) > 2:
    image_array = np.mean(image_array, axis=2).astype(np.uint8)

# Aplicar a transformada de Fourier 2D
fft_image = np.fft.fft2(image_array)

# Centralizar a transformada
fft_shifted = np.fft.fftshift(fft_image)

# Criar um filtro passa-baixa Butterworth
cutoff_frequency = 30  # Defina a frequência de corte desejada
order = 2  # Defina a ordem do filtro
rows, cols = image_array.shape
crow, ccol = rows // 2, cols // 2
mask = np.zeros((rows, cols))
mask[int(crow - cutoff_frequency):int(crow + cutoff_frequency),
     int(ccol - cutoff_frequency):int(ccol + cutoff_frequency)] = 1
mask = scipy.signal.fftconvolve(mask, np.ones((order, order)), mode='same')
mask = 1 / (1 + np.power(mask, 2))  # Aplicar a função de transferência do filtro de Butterworth

# Aplicar o filtro na imagem na frequência
filtered_shifted = fft_shifted * mask

# Reverter o deslocamento
filtered_image = np.fft.ifftshift(filtered_shifted)

# Aplicar a transformada inversa de Fourier
filtered_image = np.fft.ifft2(filtered_image)

# Extrair a parte real da imagem filtrada
filtered_image = np.abs(filtered_image).astype(np.uint8)

# Plotar a imagem original e a imagem filtrada
plt.subplot(1, 2, 1)
plt.imshow(image_array, cmap='gray')
plt.title('Imagem Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(filtered_image, cmap='gray')
plt.title('Imagem Filtrada')
plt.axis('off')

plt.show()
