# The fundamental package for scientific computing with Python
import numpy as np
# Importação da OpenCV2 (Computer Vision)
import cv2

# Carregar a imagem
imagem = cv2.imread('./images_original/14/Mandrill.jpg')

# Aplicar o filtro de média
filtro_media = cv2.blur(imagem, (5, 5))  # Pode ajustar o tamanho da janela (kernel) para alterar a intensidade do filtro

# Aplicar o filtro de aguçamento
mascara = cv2.subtract(imagem, filtro_media)
imagem_realcada = cv2.add(imagem, mascara)

# Exibir a imagem original, o filtro de média e o resultado final lado a lado
resultado = np.concatenate((imagem, filtro_media, imagem_realcada), axis=1)
cv2.imwrite('./images_generate/14/atividadefinal_b.png', resultado)

