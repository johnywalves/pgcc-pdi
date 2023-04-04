import cv2
import numpy as np
import os

file_out = open(os.path.basename(__file__).split('.')[0] + '.txt', "w")

def print_out(text):
    file_out.write(text + '\n')
    print(text)

# Carrega a imagem existente com rudo gaussiano
img = cv2.imread("./images/e_noise_gaussian.bmp")

# Aplica a corre ́ao gama com diferentes valores de y
y_values = [0.04, 0.4, 2.5, 10]
for y in y_values:
    corrected_img = np.power(img / 255., y)
    corrected_img = np.uint8(corrected_img * 255)

    # Salva a imagem corrigida
    cv2.imwrite(f"./images/imagem_corrigida_y={y}.jpg", corrected_img)

# Aplicando duas métricas do exercicio 4 aula 4
# Carrega a imagem original degradada com rudo gaussiano
original_img = cv2.imread("./images/e_noise_gaussian.bmp")

# Carrega a imagem com tratamento gama
noisy_img = cv2.imread("./images/imagem_corrigida_y=0.4.jpg")

# Aplica a corre ́ao gama com um valor de y
y = 0.4
corrected_img = np.power(noisy_img / 255., y)
corrected_img = np.uint8(corrected_img * 255)

# Calcula o erro médio absoluto (MAE)
mae = np.mean(np.abs(corrected_img - original_img))

# Calcula o erro médio quadrático (MSE)
mse = np.mean((corrected_img - original_img)**2)

print_out(f"MAE: {mae}")
print_out(f"MSE: {mse}")
