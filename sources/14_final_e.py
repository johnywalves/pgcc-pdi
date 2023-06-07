# Importação da OpenCV2 (Computer Vision)
import cv2
# The fundamental package for scientific computing with Python
import numpy as np
# Matplotlib: Visualization with Python
from matplotlib import pyplot as plt

# Carregar a imagem segmentada
image_path = './images_original/14/Mandrill.jpg'
segmented_image = cv2.imread(image_path, 0)  # Lê a imagem em escala de cinza

# Aplicar a Transformada de Fourier
fft_result = np.fft.fft2(segmented_image)
shifted_fft = np.fft.fftshift(fft_result)
magnitude_spectrum = 20 * np.log(np.abs(shifted_fft))

# Exibir a imagem segmentada e o espectro de frequência
plt.subplot(121), plt.imshow(segmented_image, cmap='gray')
plt.title('Imagem segmentada'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Espectro de Frequência'), plt.xticks([]), plt.yticks([])
plt.savefig('./images_generate/14/atividadefinal_e.png')
