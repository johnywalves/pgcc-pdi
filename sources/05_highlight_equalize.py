# Importação da biblioteca de tratamento de imagens
from PIL import Image
# The fundamental package for scientific computing with Python
import numpy as np
# Importação da biblioteca própria
import library

def equalizacao_histograma(nome_imagem):
    # Carregar a imagem
    original_img = Image.open("./images_original/05/" + nome_imagem + ".jpg")
    original_depths = np.asarray(original_img)

    # Flatten image array and calculate histogram via binning
    histogram = np.bincount(original_depths.flatten(), minlength=256)
    # Normalize
    histogram = histogram / np.sum(histogram)
    # Normalized cumulative histogram
    count_histogram = np.cumsum(histogram)
    # Pixel mapping lookup table
    transform_map = np.floor(255 * count_histogram).astype(np.uint8)
    # Flatten image array
    image_list = list(original_depths.flatten())
    # Transform pixel values to equalize
    eq_img_list = [transform_map[p] for p in image_list]
    # Reshape and write back into img_array
    eq_img_array = np.reshape(np.asarray(eq_img_list), original_depths.shape)

    # Geração da imagem de Equalizada
    largura = eq_img_array.shape[1]
    altura = eq_img_array.shape[0]

    equalized_img = Image.new('P', (largura, altura))
    equalized_pixels = equalized_img.load()
    for i in range(largura):
        for j in range(altura):
            equalized_pixels[i, j] = int(eq_img_array[j][i][0])

    # Plotar a comparação original e equalizada com os histogramas
    library.plotar_comparacao_histograma(
            original_img, 
            equalized_img,
            [
                "Imagem original",
                "Imagem equalizada",
                "Histograma da imagem original",
                "Histograma da imagem equalizada"
            ],
            "./images_generate/05/equalize_" + nome_imagem + ".jpg"
        )

equalizacao_histograma("frutas")
equalizacao_histograma("mammogram")
equalizacao_histograma("Moon")
equalizacao_histograma("polem")
