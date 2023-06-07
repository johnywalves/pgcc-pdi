import numpy as np
from PIL import Image
from skimage.feature import local_binary_pattern

# Carrega a imagem em tons de cinza
img = Image.open('./images_original/13/R0_caso1.jpg').convert('L')

# Converte para matriz NumPy
img_array = np.array(img)

# Define os parâmetros para o cálculo do LBP
radius = 1
n_points = 8

# Calcula o LBP da imagem
lbp = local_binary_pattern(img_array, n_points, radius)

# Exibe a imagem resultante
generated = Image.fromarray(lbp)
generated = generated.convert('RGB')
generated.save('./images_generate/13/atividade_8_exercicio_2.jpg')
