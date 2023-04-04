from PIL import Image
import numpy as np

import os
import library

file_out = open(os.path.basename(__file__).split('.')[0] + '.txt', "w")


def print_out(text):
    file_out.write(text + '\n')
    print(text)

# Criando a imagem A com nveis de cinza aleatórios
A = np.random.randint(0, 256, size=(5, 5))
print_out("Imagem A:")
print_out(str(A))

# Ruído Gaussiano
# Definindo parâmetros iniciais para gerar o ruído de Gaussiano
mean = 0
variance = 100

# Gerando ruído de Gaussiano em uma imagem B
B_gauss = np.random.normal(mean, np.sqrt(variance), size=(5, 5)).astype(int)
print_out("Imagem B (Gaussiano):")
print_out(str(B_gauss))

# Geração da imagem de Poisson
img_poison = Image.new('P', (5, 5))
pixels = img_poison.load()
for i in range(img_poison.size[0]):
    for j in range(img_poison.size[1]):
        pixels[i, j] = (int(128 + B_gauss[i][j]))
img_poison.save('./images/pz_gauss.bmp')

# Degradando a imagem A com o ruído de Gaussiano
A_gauss = np.clip(A + B_gauss, 0, 255).astype(int)
print_out("Imagem A degradada (Gaussiano):")
print_out(str(A_gauss))

# Plotando o histograma de B para mostrar a caracterstica do ruído de Gaussiano
library.plotar_histograma_ruido(B_gauss.flatten(),
                                 "Função p(z) do ruído de Gaussiano", "./images/pz_gauss_noise.jpg")

# Plotando a função p(z) para Gaussiano
library.plotar_histograma_cinzas(A_gauss.flatten(),
                                "Histograma do ruído de Gaussiano", "./images/pz_gauss_degraded.jpg")

# Ruído Poisson
# Definindo parmetros iniciais para gerar o ruído de Poisson
lam = 10.

# Gerando rudo de Poisson em uma imagem B
B_poisson = np.random.poisson(lam=lam, size=(5, 5)).astype(int)
print_out("Imagem B (Poisson):")
print_out(str(B_poisson))

# Geração da imagem de Poisson
img_poison = Image.new('P', (5, 5))
pixels = img_poison.load()
for i in range(img_poison.size[0]):
    for j in range(img_poison.size[1]):
        pixels[i, j] = (int(128 + B_poisson[i][j]))
img_poison.save('./images/pz_poisson.bmp')

# Degradando a imagem A com o ruído de Poisson
A_poisson = np.clip(A + B_poisson, 0, 255).astype(int)
print_out("Imagem A degradada (Poisson):")
print_out(str(A_poisson))

# Plotando o histograma de B para mostrar a caracterstica do ruído de Poisson
library.plotar_histograma_ruido(B_poisson.flatten(),
                                 "Função p(z) do ruído de Poisson", "./images/pz_poisson_noise.jpg")

# Plotando a função p(z) para Poisson
library.plotar_histograma_cinzas(A_poisson.flatten(),
                                "Histograma do ruído de Poisson", "./images/pz_poisson_degraded.jpg")
