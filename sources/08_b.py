# Importação da biblioteca de tratamento de imagens
from PIL import Image
# The fundamental package for scientific computing with Python
import numpy as np

from scipy.signal import convolve2d

def filtro_passa_alta_com_mascara(nome):
    # carrega a imagem de entrada
    img = Image.open('./images_original/' + nome + '.bmp').convert('L')

    # converte a imagem para matriz NumPy
    img_arr = np.array(img)

    # aplica a máscara H1
    mask_h1 = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
    img_h1 = np.abs(convolve2d(img_arr, mask_h1, mode='same')).astype(np.uint8)

    # aplica a máscara H2
    mask_h2 = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    img_h2 = np.abs(convolve2d(img_arr, mask_h2, mode='same')).astype(np.uint8)

    # converte as matrizes de volta para a imagem
    img_h1 = Image.fromarray(img_h1)
    img_h2 = Image.fromarray(img_h2)

    # Salva a imagem de entrada e as imagens filtradas
    img_h1.convert('RGB').save('./images_generate/08/' + nome + '_Suavizacao_passa_alta_h1.jpg')
    img_h2.convert('RGB').save('./images_generate/08/' + nome + '_Suavizacao_passa_alta_h2.jpg')

filtro_passa_alta_com_mascara('e_ruido_salpimenta')
filtro_passa_alta_com_mascara('e_ruido_gaussiano')
