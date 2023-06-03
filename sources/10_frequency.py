import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from skimage import io, img_as_float, img_as_ubyte, color, util 

def conversao_cinza(nome):
    # Carregar a imagem de entrada
    img = Image.open('./images_original/10/' + nome + '.png')
    # Converter a imagem para escala de cinza
    img_gray = img.convert('L')
    # Converter a imagem para 8 bits de quantização
    img_gray_8bits = img_gray.quantize(colors=256)
    # Salvar a imagem resultante
    img_gray_8bits.save('./images_generate/10/' + nome + '_cinza_8bits.png')


def ruido_gaussiano(nome):
    # Carregue a imagem
    img = Image.open('./images_generate/10/' + nome + '_cinza_8bits.png')
    # Converta a imagem para um array NumPy
    img_array = np.array(img)
    # Defina a média e o desvio padrão do ruído gaussiano
    mean = 0
    stddev = 50
    # Crie uma matriz de números aleatórios de distribuição normal
    noise = np.random.normal(mean, stddev, img_array.shape)
    # Adicione o ruído à imagem
    noisy_img = img_array + noise
    # Converta o array NumPy de volta para uma imagem
    noisy_img = Image.fromarray(noisy_img.astype('uint8'))
    # Salve a imagem com ruído
    noisy_img.save('./images_generate/10/' + nome + '_gaussiano.png')


def img_DFT(nome):
    # Carregar a imagem de entrada
    img = plt.imread('./images_generate/10/' + nome + '_gaussiano.png')
    # Aplicar a DFT
    dft = np.fft.fft2(img)
    dft_shift = np.fft.fftshift(dft)
    # Calcular o espectro de frequência
    magnitude_spectrum = 40 * np.log(np.abs(dft_shift))
    # Salvar a imagem resultante
    plt.imsave('./images_generate/10/' + nome + '_dft.png', magnitude_spectrum, cmap='gray')


def deslocamento_frequencias(nome):
    # Carregando a imagem 
    img = io.imread('./images_generate/10/' + nome + '_dft.png', as_gray=True) 
    # Aplicando a transformada discreta de Fourier 
    dft = np.fft.fft2(img) 
    # Centralizando o espectro 
    dft_shifted = np.fft.fftshift(dft) 
    # Obtendo o módulo do espectro 
    magnitude_spectrum = np.abs(dft_shifted) 
    # Plotando a imagem original e o espectro 
    fig, ax = plt.subplots(1, 2, figsize=(10, 5)) 
    ax[0].imshow(img, cmap='gray') 
    ax[0].set_title('Imagem Original') 
    ax[1].imshow(np.log(1 + magnitude_spectrum), cmap='gray') 
    ax[1].set_title('Espectro de Fourier com Deslocamento') 
    # Salvando o resultado 
    plt.savefig('./images_generate/10/' + nome + '_desloamento_frequencia.png', dpi=300, bbox_inches='tight') 



def filtros_dominio_frequencia_2(nome):
    # carrega a imagem em tons de cinza com ruído gaussiano
    img = Image.open('./images_generate/10/' + nome + '_gaussiano.png').convert('L')
    img = np.array(img)
    # calcula o espectro de Fourier da imagem original
    img_fft = np.fft.fft2(img)
    img_fft_shift = np.fft.fftshift(img_fft)
    img_fft_mag = np.abs(img_fft_shift)
    # aplica o filtro média
    n = 3
    img_suave = np.zeros_like(img)
    for i in range(n//2, img.shape[0]-n//2):
        for j in range(n//2, img.shape[1]-n//2):
            img_suave[i,j] = np.mean(img[i-n//2:i+n//2+1,j-n//2:j+n//2+1])
    # calcula o espectro de Fourier da imagem suavizada
    img_suave_fft = np.fft.fft2(img_suave)
    img_suave_fft_shift = np.fft.fftshift(img_suave_fft)
    img_suave_fft_mag = np.abs(img_suave_fft_shift)
    # aplica o filtro gaussiano
    sigma = 5.5
    h, w = img.shape
    x, y = np.meshgrid(np.arange(w), np.arange(h))
    center_x, center_y = w // 2, h // 2
    gaussian_mask = np.exp(-((x - center_x) ** 2 + (y - center_y) ** 2) / (2 * sigma ** 2))
    img_gauss = np.fft.ifft2(np.fft.fft2(img) * gaussian_mask).real
    # calcula o espectro de Fourier da imagem com filtro gaussiano
    img_gauss_fft = np.fft.fft2(img_gauss)
    img_gauss_fft_shift = np.fft.fftshift(img_gauss_fft)
    img_gauss_fft_mag = np.abs(img_gauss_fft_shift)
    # mostra as imagens e os espectros de Fourier
    fig, axs = plt.subplots(2, 3, figsize=(12, 8))
    axs[0, 0].imshow(img, cmap='gray')
    axs[0, 0].set_title('Imagem Original')
    axs[0, 1].imshow(img_suave, cmap='gray')
    axs[0, 1].set_title('Img c/ Filtro média')
    axs[0, 2].imshow(img_gauss, cmap='gray')
    axs[0, 2].set_title('Img c/ Filtro Gaussiano')
    axs[1, 0].imshow(np.log(1 + img_fft_mag), cmap='gray')
    axs[1, 0].set_title('Espectro Fourier Img_Original')
    axs[1, 1].imshow(np.log(1 + img_suave_fft_mag), cmap='gray')
    axs[1, 1].set_title('Espectro Fourier Img_c/ Filtro Media')
    axs[1, 2].imshow(np.log(1 + img_gauss_fft_mag), cmap='gray')
    axs[1, 2].set_title('Espectro Fourier Img c/ Filtro Gaussiano')
    for ax in axs.flat:
        ax.label_outer()
    plt.savefig("./images_generate/10/" + nome + "_final.png")

conversao_cinza('img_exercicio2')
ruido_gaussiano('img_exercicio2')
img_DFT('img_exercicio2')
deslocamento_frequencias('img_exercicio2')
filtros_dominio_frequencia_2('img_exercicio2')