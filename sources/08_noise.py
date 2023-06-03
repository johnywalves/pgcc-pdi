# Instalar pacote com `pip3 install pillow`
from PIL import Image
# The fundamental package for scientific computing with Python
import numpy as np

import random

def ruido_sal_pimenta (nome):
    # Carregando a imagem de entrada
    img = Image.open('./images_original/' + nome + '.bmp').convert('L')

    # Definindo a probabilidade de ocorrência do ruído
    prob = 0.05

    # Gerando o ruído sal e pimenta
    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r = random.random()
            if r < prob/2:
                pixels[i,j] = 0
            elif r > 1 - prob/2:
                pixels[i,j] = 255

    # Salvando a imagem ruidosa em uma pasta
    img.save('./images_original/' + nome + '_ruido_salpimenta.bmp')

def ruido_gaussiano(nome):
    # carregar imagem de entrada
    img = Image.open('./images_original/' + nome + '.bmp')
    img_array = np.array(img)

    # gerar ruído gaussiano
    mean = 0
    stddev = 50
    noise = np.random.normal(mean, stddev, img_array.shape)

    # adicionar ruído à imagem original
    noisy_img = np.uint8(np.clip(img_array + noise, 0, 255))

    # salvar imagem com ruído
    Image.fromarray(noisy_img).save('./images_original/' + nome + '_ruido_gaussiano.bmp')

ruido_sal_pimenta('e')
ruido_gaussiano('e')