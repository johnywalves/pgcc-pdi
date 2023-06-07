# Importação da OpenCV2 (Computer Vision)
import cv2
# The fundamental package for scientific computing with Python
import numpy as np
# Matplotlib: Visualization with Python
from matplotlib import pyplot as plt

# Carregar a imagem de entrada
img = cv2.imread('./images_original/14/Mandrill.jpg', 0)  # Carrega a imagem em escala de cinza

# Aplicar a transformada de Fourier
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

# Definir o filtro (por exemplo, um filtro passa-baixa)
rows, cols = img.shape
center_row, center_col = rows // 2, cols // 2
radius = 30  # Defina o raio para o filtro passa-baixa
mask = np.zeros((rows, cols, 2), np.uint8)
mask[center_row - radius:center_row + radius, center_col - radius:center_col + radius] = 1

# Aplicar o filtro na frequência (multiplicação complexa)
filtered_shift = dft_shift * mask

# Aplicar a transformada inversa de Fourier
filtered_ishift = np.fft.ifftshift(filtered_shift)
filtered_img = cv2.idft(filtered_ishift)
filtered_img = cv2.magnitude(filtered_img[:, :, 0], filtered_img[:, :, 1])

# Exibir a imagem original e a imagem filtrada
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Imagem Original'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(filtered_img, cmap='gray')
plt.title('Imagem Filtrada'), plt.xticks([]), plt.yticks([])
plt.savefig('./images_generate/14/atividadefinal_g.png')
