import numpy as np
import matplotlib.pyplot as plt

# Criando a imagem A com nveis de cinza aleatórios
A = np.random.randint(0, 256, size=(5, 5))
print("Imagem A:")
print(A)

# Definindo parâmetros iniciais para gerar o ruído de Gaussiano
mean = 0
variance = 100

# Gerando ruído de Gaussiano em uma imagem B
B_gauss = np.random.normal(mean, np.sqrt(variance), size=(5, 5)).astype(int)
print("Imagem B (Gaussiano):")
print(B_gauss)

# Calculando a função p(z) para o rudo de Gaussiano
z = np.arange(-255, 256)
p_gauss = np.exp(-(z - mean) ** 2 / (2 * variance)) / \
    np.sqrt(2 * np.pi * variance)

# Plotando a fun ́ao p(z)
plt.clf()
plt.plot(z, p_gauss)
plt.title(" Função p(z) do ruído de Gaussiano")
plt.xlabel("Intensidade de pixel")
plt.ylabel("Probabilidade")
plt.savefig('./images/pz_gaussian.jpg')

# Plotando o histograma de B para mostrar a caracterstica do rudo de Gaussiano
plt.clf()
plt.hist(B_gauss.flatten(), bins=256, range=(-255, 255), density=True)
plt.title("Histograma do ruído de Gaussiano")
plt.xlabel("Intensidade de pixel")
plt.ylabel("Frequência")
plt.savefig('./images/pz_gaussian_histogram.jpg')

# Definindo parmetros iniciais para gerar o rudo de Poisson
lam = 10

# Gerando rudo de Poisson em uma imagem B
B_poisson = np.random.poisson(lam=lam, size=(5, 5)).astype(int)
print("Imagem B (Poisson):")
print(B_poisson)

# Calculando a funcao p(z) para o ruido de Poisson
z = np.arange(0, 256)
p_poisson = (lam ** z * np.exp(-lam)) / np.math.factorial(z)

# Plotando a funcao p(z)
plt.clf()
plt.plot(z, p_poisson)
plt.title("Função p(z) do ruído de Poisson")
plt.xlabel("Intensidade de pixel")
plt.ylabel("Probabilidade")
plt.savefig('./images/pz_poisson.jpg')

# Plotando o histograma de B para mostrar a caracterstica do ruido de Poisson
plt.clf()
plt.hist(B_poisson.flatten(), bins=256, range=(0, 255), density=True)
plt.title("Histograma do rudo de Poisson")
plt.xlabel("Intensidade de pixel")
plt.ylabel("Frequncia")
plt.savefig('./images/pz_poisson_histogram.jpg')

# Degradando a imagem A com o ruido de Gaussiano e Poisson
A_gauss = np.clip(A + B_gauss, 0, 255).astype(int)
print("Imagem A degradada (Gaussiano):")
print(A_gauss)

A_poisson = np.clip(A + B_poisson, 0, 255).astype(int)
print("Imagem A degradada (Poisson):")
print(A_poisson)
