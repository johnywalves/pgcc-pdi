# Importação da OpenCV2 (Computer Vision)
import cv2
# The fundamental package for scientific computing with Python
import numpy as np
# Importação da biblioteca própria
import library

# Carrega a imagem existente com rudo gaussiano
img = cv2.imread("./images_original/e_noise_gaussian.bmp")

# Aplica a correção gama com diferentes valores de y
y_values = [0.04, 0.4, 2.5, 10]
for y in y_values:
    corrected_img = np.power(img / 255., y)
    corrected_img = np.uint8(corrected_img * 255)

    # Salva a imagem corrigida
    cv2.imwrite(f"./images_generate/06/imagem_corrigida_y={y}.jpg", corrected_img)

# Aplicando duas métricas do exercicio 4 aula 4
# Carrega a imagem original degradada com rudo gaussiano
original_img = cv2.imread("./images_original/e_noise_gaussian.bmp")

# Carrega a imagem com tratamento gama
noisy_img = cv2.imread("./images_generate/06/imagem_corrigida_y=0.4.jpg")

# Aplica a correção gama com um valor de y
y = 0.4
corrected_img = np.power(noisy_img / 255., y)
corrected_img = np.uint8(corrected_img * 255)

# Calcula o erro médio absoluto (MAE)
mae = np.mean(np.abs(corrected_img - original_img))

# Calcula o erro médio quadrático (MSE)
mse = np.mean((corrected_img - original_img)**2)

library.print_out(f"MAE: {mae}")
library.print_out(f"MSE: {mse}")
