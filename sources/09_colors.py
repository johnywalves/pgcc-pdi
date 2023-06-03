# Instalar pacote com `pip3 install pillow`
from PIL import Image
# Matplotlib: Visualization with Python
import matplotlib.pyplot as plt
# The fundamental package for scientific computing with Python
import numpy as np

import math
import colorsys

# incio nós estamos transformando a imagem original para o formato HSI
def rgb_to_hsi(rgb):
    # Converte valores de 0-255 para 0-1
    r, g, b = rgb[0]/255.0, rgb[1]/255.0, rgb[2]/255.0

    # Calcula Intensidade
    I = (r + g + b) / 3.0

    # Calcula Saturação
    if r + g + b == 0:
        S = 0
    else:
        S = 1 - 3 * min(r, g, b) / (r + g + b)

    # Calcula Matiz
    H = 0
    if S != 0:
        num = 0.5 * ((r - g) + (r - b))
        den = ((r - g)**2 + (r - b) * (g - b))**0.5
        theta = math.acos(num / den)
        if b > g:
            H = 360 - theta
        else:
            H = theta
    return (H, S, I)


def bmp_to_hsi(input_file, output_file):
    # Carrega a imagem BMP
    with Image.open(input_file) as img:
        # Cria nova imagem com mesmo tamanho
        new_img = Image.new('RGB', img.size)

        # Converte cada pixel para HSI
        for y in range(img.height):
            for x in range(img.width):
                pixel_rgb = img.getpixel((x, y))
                pixel_hsi = rgb_to_hsi(pixel_rgb)
                new_img.putpixel((x, y), tuple(
                    map(lambda x: int(x * 255), colorsys.hsv_to_rgb(*pixel_hsi))))

        # Salva a nova imagem HSI em um arquivo BMP
        new_img.save(output_file)

# agora pegamos a imagem original que está no formato RGB e aplicamos a equalização
# Carrega a imagem de entrada
def equalize_image(nome):
    img = np.array(Image.open('./images/'+nome+'.bmp'))
    # Separa os canais R, G e B da imagem
    r_channel = img[:, :, 0]
    g_channel = img[:, :, 1]
    b_channel = img[:, :, 2]

    # Aplica a equalização de histograma em cada canal
    r_equalized = np.interp(r_channel.flatten(), np.arange(256), np.histogram(r_channel, bins=256, range=(0, 255))[0].cumsum()*255/(r_channel.shape[0]*r_channel.shape[1])).reshape(r_channel.shape)
    g_equalized = np.interp(g_channel.flatten(), np.arange(256), np.histogram(g_channel, bins=256, range=(0, 255))[0].cumsum()*255/(g_channel.shape[0]*g_channel.shape[1])).reshape(g_channel.shape)
    b_equalized = np.interp(b_channel.flatten(), np.arange(256), np.histogram(b_channel, bins=256, range=(0, 255))[0].cumsum()*255/(b_channel.shape[0]*b_channel.shape[1])).reshape(b_channel.shape)
    
    # Junta os canais R, G e B equalizados em uma única imagem
    img_equalized = np.stack(
        (r_equalized, g_equalized, b_equalized), axis=2).astype(np.uint8)
    
    # Salva a imagem equalizada
    Image.fromarray(img_equalized).save('./images/' + nome + '_equalizada.jpg')

def gera_histograma(nome):
    # agora carregamos a imagem equalizada e mostramos seu histograma
    # Carrega a imagem de entrada
    img = np.array(Image.open('./images/' + nome + '_equalizada.jpg'))

    # Separa os canais R, G e B da imagem
    r_channel = img[:, :, 0]
    g_channel = img[:, :, 1]
    b_channel = img[:, :, 2]

    # Aplica a equalização de histograma em cada canal
    r_equalized = np.interp(r_channel.flatten(), np.arange(256), np.histogram(r_channel, bins=256, range=(0, 255))[0].cumsum()*255/(r_channel.shape[0]*r_channel.shape[1])).reshape(r_channel.shape)
    g_equalized = np.interp(g_channel.flatten(), np.arange(256), np.histogram(g_channel, bins=256, range=(0, 255))[0].cumsum()*255/(g_channel.shape[0]*g_channel.shape[1])).reshape(g_channel.shape)
    b_equalized = np.interp(b_channel.flatten(), np.arange(256), np.histogram(b_channel, bins=256, range=(0, 255))[0].cumsum()*255/(b_channel.shape[0]*b_channel.shape[1])).reshape(b_channel.shape)
    
    # Junta os canais R, G e B equalizados em uma única imagem
    img_equalized = np.stack((r_equalized, g_equalized, b_equalized), axis=2).astype(np.uint8)
    
    # Calcula o histograma equalizado da imagem equalizada
    hist_equalized = np.histogram(img_equalized.flatten(), bins=256, range=(0, 255))[0]
   
    # Plotar o histograma equalizado
    plt.clf()
    plt.plot(hist_equalized)
    plt.title('Histograma Equalizado')
    plt.xlabel('Intensidade')
    plt.ylabel('Frequência')

    # Salva a figura do histograma em um arquivo
    plt.savefig('./images/' + nome + '_histograma_equalizado.jpg')

# função que executa o exercicio completo para a imgem especificada
def executa_exercicio(nome):
    # Conversão da imagem original para o formato HSI
    bmp_to_hsi('./images/' + nome + '.bmp', './images/' + nome + '_HSI.bmp')

    # Equalização da imagem original no formato RGB
    equalize_image(nome)

    # Geração do histograma da imagem equalizada
    gera_histograma(nome)

executa_exercicio('Img1')
executa_exercicio('Img2')
executa_exercicio('Img3')
