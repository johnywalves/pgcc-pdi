# The fundamental package for scientific computing with Python
import numpy as np
# Importação da biblioteca própria
import library

def gerador_de_filtro_gaussiano(tamanho, sigma):
    # Calcula os coeficientes da expansão binomial de Newton
    coef = [1]
    for i in range(1, tamanho):
        coef.append(coef[-1] * (tamanho - i) // i)
    coef = np.array(coef)

    # Calcula a máscara gaussiana
    center = tamanho // 2
    filter = np.zeros((tamanho, tamanho))
    for i in range(tamanho):
        for j in range(tamanho):
            x, y = i - center, j - center
            filter[i, j] = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    filter = filter / np.sum(filter)

    # Aplica a expansão binomial para aproximar a máscara gaussiana
    for i in range(tamanho):
        filter[i, :] = filter[i, :] * coef[i]
        filter[:, i] = filter[:, i] * coef[i]
    filter = filter / np.sum(filter)

    # Calcula a variância (largura) da máscara gaussiana
    # Para se calcular a largura usa-se a expressão matemática 
    # largura = Σ((i - c) ^ 2 * Σ(m_i, j)), 
    # onde i, j são índices de linha e coluna da máscara, 
    # c é o índice central,
    # m é a matriz da máscara e 
    # Σ representa a soma.
    variance = np.sum(np.square(np.arange(tamanho) - center) * np.sum(filter, axis=1))

    return np.array2string(filter), str(variance)

# Gera as máscaras 3x3, 5x5 e 7x7 com sigma=1
filter_3x3, variance_3x3 = gerador_de_filtro_gaussiano(3, 1)
filter_5x5, variance_5x5 = gerador_de_filtro_gaussiano(5, 1)
filter_7x7, variance_7x7 = gerador_de_filtro_gaussiano(7, 1)

library.print_out("Máscara 3x3:")
library.print_out(filter_3x3)
library.print_out("Variância (largura): " + variance_3x3)
library.print_out("")
library.print_out("Máscara 5x5:")
library.print_out(filter_5x5)
library.print_out("Variância (largura): " + variance_5x5)
library.print_out("")
library.print_out("Máscara 7x7:")
library.print_out(filter_7x7)
library.print_out("Variância (largura): " + variance_7x7)
