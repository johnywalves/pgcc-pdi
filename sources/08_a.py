# Importação da biblioteca de tratamento de imagens
from PIL import Image
# The fundamental package for scientific computing with Python
import numpy as np

def suavizacao_media(nome):
    # carrega a imagem de entrada
    img = Image.open('./images_original/' + nome + '.bmp')

    # converte a imagem para um array NumPy
    img_array = np.array(img)

    # cria um kernel de suavização média com janela 3x3
    kernel = np.ones((3, 3), np.float32) / 9

    # cria uma matriz de zeros para armazenar a imagem suavizada
    img_suave = np.zeros_like(img_array)

    # aplica o filtro de suavização média percorrendo todos os pixels da imagem
    for i in range(1, img_array.shape[0] - 1):
        for j in range(1, img_array.shape[1] - 1):
            img_suave[i, j] = np.sum(img_array[i-1:i+2, j-1:j+2] * kernel)

    # converte o array NumPy de volta para uma imagem
    img_suave = Image.fromarray(img_suave.astype(np.uint8))

    # Salvando a imagem ruidosa em uma pasta
    img_suave.convert('RGB').save('./images_generate/08/' + nome + '_Suavizacao_media.jpg')


def suavizacao_mediana(nome):
    # carrega a imagem de entrada
    img = Image.open('./images_original/' + nome + '.bmp')

    # converte a imagem para um array NumPy
    img_array = np.array(img)

    # cria uma matriz de zeros para armazenar a imagem suavizada
    img_suave = np.zeros_like(img_array)

    # aplica o filtro de suavização do tipo mediana percorrendo todos os pixels da imagem
    for i in range(1, img_array.shape[0] - 1):
        for j in range(1, img_array.shape[1] - 1):
            # cria um array com os valores dos pixels vizinhos (janela 3x3)
            window = img_array[i-1:i+2, j-1:j+2]
            # calcula a mediana dos valores na janela
            img_suave[i, j] = np.median(window)

    # converte o array NumPy de volta para uma imagem
    img_suave = Image.fromarray(img_suave.astype(np.uint8))

    # exibe a imagem de entrada e a imagem suavizada
    img_suave.convert('RGB').save('./images_generate/08/' + nome + '_Suavizacao_mediana.jpg')
    img_suave.save('./images_original/' + nome + '_Suavizacao_mediana.bmp')


def suavizacao_gausiano(nome):
    # carrega a imagem de entrada
    img = Image.open('./images_original/' + nome + '.bmp')

    # converte a imagem para um array NumPy
    img_array = np.array(img)

    # define o kernel do filtro de suavização gaussiano 3x3
    kernel = np.array([[1, 2, 1],
                    [2, 4, 2],
                    [1, 2, 1]]) / 16
    
    # aplica o filtro de suavização gaussiano usando convolução 2D no domínio da frequência
    # usando a Transformada Discreta de Fourier (DFT)
    img_fft = np.fft.fft2(img_array, axes=(0, 1))
    kernel_fft = np.fft.fft2(kernel, s=img_array.shape[:2], axes=(0, 1))
    img_suave_fft = img_fft * kernel_fft
    img_suave = np.fft.ifft2(img_suave_fft, axes=(0, 1)).real.astype(np.uint8)

    # converte o array NumPy de volta para uma imagem
    img_suave = Image.fromarray(img_suave)

    # exibe a imagem de entrada e a imagem suavizada
    img_suave.convert('RGB').save('./images_generate/08/' + nome + '_Suavizacao_gaussiano.jpg')


def suavizacao_moda (nome):
    # carrega a imagem de entrada
    img = Image.open('./images_original/' + nome + '.bmp')

    # converte a imagem para um array NumPy
    img_array = np.array(img)

    # define a janela de filtro como uma matriz 3x3
    kernel = np.ones((3, 3), dtype=int)

    # aplica o filtro de suavização do tipo moda com janela 3x3
    img_suave = np.zeros_like(img_array)
    for i in range(1, img_array.shape[0]-1):
        for j in range(1, img_array.shape[1]-1):
            patch = img_array[i-1:i+2, j-1:j+2]
            values, counts = np.unique(patch, return_counts=True)
            img_suave[i, j] = values[np.argmax(counts)]

    # converte o array NumPy de volta para uma imagem
    img_suave = Image.fromarray(img_suave)

    # exibe a imagem de entrada e a imagem suavizada
    img_suave.convert('RGB').save('./images_generate/08/' + nome + '_Suavizacao_moda.jpg')


suavizacao_media('e_ruido_salpimenta')
suavizacao_media('e_ruido_gaussiano')

suavizacao_mediana('e_ruido_salpimenta')
suavizacao_mediana('e_ruido_gaussiano')

suavizacao_gausiano('e_ruido_salpimenta')
suavizacao_gausiano('e_ruido_gaussiano')

suavizacao_moda('e_ruido_salpimenta')
suavizacao_moda('e_ruido_gaussiano')
