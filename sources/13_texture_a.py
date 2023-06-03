import numpy as np
from PIL import Image
import os

file_out = open(os.path.basename(__file__).split('.')[0] + '.txt', "w")

def print_out(text):
    file_out.write(text + '\n')
    print(text)

def calculate_glcm(image_array, distance, angle):
    # cria uma matriz de zeros para a matriz de co-ocorrência
    glcm = np.zeros((256, 256), dtype=np.uint32)

    # itera sobre a imagem e incrementa os valores da matriz de co-ocorrência
    for row in range(image_array.shape[0] - distance):
        for col in range(image_array.shape[1] - distance):
            # pega o valor do pixel atual e do pixel adjacente
            p1 = image_array[row, col]
            p2 = image_array[row + distance, col + angle]

            # incrementa a entrada correspondente na matriz de co-ocorrência
            glcm[p1, p2] += 1

    # normaliza a matriz de co-ocorrência para que as entradas somem 1
    glcm = glcm / np.sum(glcm)

    return glcm

def calculate_haralick(image_array, distance=1, angle=0):
    # calcula a matriz de co-ocorrência para o ângulo e distância especificados
    glcm = calculate_glcm(image_array, distance, angle)

    # calcula as medidas de Haralick
    asm = np.sum(glcm ** 2)
    entropy = -np.sum(glcm * np.log2(glcm + (glcm == 0)))
    contrast = np.sum(glcm * np.square(np.subtract(*np.meshgrid(range(256), range(256), indexing='ij'))))

    return asm, entropy, contrast

# carrega a imagem em tons de cinza
img = Image.open('images/R0_caso1.JPG').convert('L')

# converte para matriz NumPy
img_array = np.array(img)

# calcula as medidas de Haralick
asm, entropy, contrast = calculate_haralick(img_array, distance=1, angle=0)

# exibe os resultados
print_out(f'Second Moment Angular: {asm:.4f}')
print_out(f'Entropia: {entropy:.4f}')
print_out(f'Contraste: {contrast:.4f}')
