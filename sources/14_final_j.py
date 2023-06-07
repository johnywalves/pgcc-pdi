# Importação da OpenCV2 (Computer Vision)
import cv2
# Matplotlib: Visualization with Python
from matplotlib import pyplot as plt
# Importação da biblioteca própria
import library

# Carregar a imagem de entrada
img_path = './images_original/14/Mandrill.jpg'
img = cv2.imread(img_path)

# Converter a imagem para escala de cinza
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Redimensionar a imagem para um tamanho fixo
resized_img = cv2.resize(gray_img, (100, 100))  # Ajuste o tamanho conforme necessário

# Calcular histograma de intensidade
histogram = cv2.calcHist([resized_img], [0], None, [256], [0, 256])

# Normalizar o histograma
normalized_histogram = histogram / (resized_img.shape[0] * resized_img.shape[1])

# Achatando o histograma em um vetor unidimensional
flattened_histogram = normalized_histogram.flatten()

# Exibir o histograma
plt.figure(figsize=(8, 4))
plt.plot(flattened_histogram)
plt.title('Histograma de Intensidade')
plt.xlabel('Intensidade')
plt.ylabel('Frequência')
plt.savefig('./images_generate/14/atividadefinal_j.png')

# Exibir a matriz de características
library.print_out('Matriz de Características:')
library.print_out(str(flattened_histogram))
