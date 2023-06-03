# Importação da biblioteca de tratamento de imagens
from PIL import Image
# The fundamental package for scientific computing with Python
import numpy as np
# Importação da biblioteca própria
import library

# Criando a imagem A com nveis de cinza aleatórios
A = np.random.randint(0, 256, size=(5, 5))
library.print_out("Imagem A:")
library.print_out(str(A))

# Ruído Gaussiano
# Definindo parâmetros iniciais para gerar o ruído de Gaussiano
mean = 0
variance = 100

# Gerando ruído de Gaussiano em uma imagem B
B_gauss = np.random.normal(mean, np.sqrt(variance), size=(5, 5)).astype(int)
library.print_out("Imagem B (Gaussiano):")
library.print_out(str(B_gauss))

# Geração da imagem de Poisson
img_poison = Image.new('P', (5, 5))
pixels = img_poison.load()
for i in range(img_poison.size[0]):
    for j in range(img_poison.size[1]):
        pixels[i, j] = (int(128 + B_gauss[i][j]))
img_poison.convert('RGB').save('./images_generate/04/pz_gauss.jpg')

# Degradando a imagem A com o ruído de Gaussiano
A_gauss = np.clip(A + B_gauss, 0, 255).astype(int)
library.print_out("Imagem A degradada (Gaussiano):")
library.print_out(str(A_gauss))

# Plotando o histograma de B para mostrar a caracterstica do ruído de Gaussiano
library.plotar_histograma_ruido(
        B_gauss.flatten(),
        "Função p(z) do ruído de Gaussiano", 
        "./images_generate/04/pz_gauss_noise.jpg"
    )

# Plotando a função p(z) para Gaussiano
library.plotar_histograma_cinzas(
        A_gauss.flatten(),
        "Histograma do ruído de Gaussiano", 
        "./images_generate/04/pz_gauss_degraded.jpg"
    )

# Ruído Poisson
# Definindo parmetros iniciais para gerar o ruído de Poisson
lam = 10.

# Gerando rudo de Poisson em uma imagem B
B_poisson = np.random.poisson(lam=lam, size=(5, 5)).astype(int)
library.print_out("Imagem B (Poisson):")
library.print_out(str(B_poisson))

# Geração da imagem de Poisson
img_poison = Image.new('P', (5, 5))
pixels = img_poison.load()
for i in range(img_poison.size[0]):
    for j in range(img_poison.size[1]):
        pixels[i, j] = (int(128 + B_poisson[i][j]))
img_poison.save('./images_generate/04/pz_poisson.bmp')

# Degradando a imagem A com o ruído de Poisson
A_poisson = np.clip(A + B_poisson, 0, 255).astype(int)
library.print_out("Imagem A degradada (Poisson):")
library.print_out(str(A_poisson))

# Plotando o histograma de B para mostrar a caracterstica do ruído de Poisson
library.plotar_histograma_ruido(
        B_poisson.flatten(),
        "Função p(z) do ruído de Poisson", 
        "./images_generate/04/pz_poisson_noise.jpg"
    )

# Plotando a função p(z) para Poisson
library.plotar_histograma_cinzas(
        A_poisson.flatten(),
        "Histograma do ruído de Poisson", 
        "./images_generate/04/pz_poisson_degraded.jpg"
    )
