# Install package `pip3 install pillow`
from PIL import Image
# The fundamental package for scientific computing with Python
import numpy as np
# Matplotlib: Visualization with Python
import matplotlib.pyplot as plt
# Importação de métricas sobre predição
from sklearn.metrics import max_error, jaccard_score,  mean_absolute_error, mean_squared_error
# Importação da biblioteca própria
import library
import os

file_out = open(os.path.basename(__file__).split('.')[0] + '.txt', "w")


def print_out(text):
    file_out.write(text + '\n')
    print(text)


def normalized_root_mean_square_error(original, noised):
    squared_sums = sum((original - noised) ^ 2)
    mse = squared_sums / len(original)
    rmse = np.sqrt(mse)
    nrmse = rmse / np.std(original)
    nrmse = round(nrmse, 3)

    return (nrmse)


def add_gaussian_noise(name, sd):
    # Load original image
    original_img = Image.open("./images/e.bmp")
    # Image original shape
    width, height = original_img.size

    # Create noise gaussian to reference
    gaussian_img = Image.new('P', (width, height))
    # Create noise gaussian to original image
    noised_img = Image.new('P', (width, height))

    # Mean of distribution
    mean = 0

    # Calculate normal distribution
    gaussian = np.random.normal(
        loc=mean, scale=sd, size=(width, height, 1)).astype(int)

    # Create the pixel map to original image
    original_pixels = original_img.load()
    # Create the pixel map to gaussian noise
    gaussian_pixels = gaussian_img.load()
    # Create the pixel map to noised image
    noised_pixels = noised_img.load()

    # For every pixel:
    for i in range(width):
        for j in range(height):
            # Set the colour accordingly
            gaussian_pixels[i, j] = int(128 + gaussian[i][j])
            noised_pixels[i, j] = int(original_pixels[i, j] + gaussian[i][j])

    gaussian_img.save('./images/noise_gaussian.bmp')
    noised_img.save('./images/' + name + '_noise_gaussian.bmp')

    # Display Standard Distribution
    print_out("Desvio padrão " + str(sd))

    # Flatten the depths of gray
    original_depths = np.ndarray.flatten(np.asarray(original_img))
    gaussian_depths = np.ndarray.flatten(np.asarray(gaussian_img))
    noised_depths = np.ndarray.flatten(np.asarray(noised_img))

    # Display error indicators
    print_out("Erro máximo " + str(max_error(original_depths, noised_depths)))
    print_out("Erro médio absoluto " +
          str(mean_absolute_error(original_depths, noised_depths)))
    print_out("Erro médio quadrático " +
          str(mean_squared_error(original_depths, noised_depths)))
    print_out("Raiz do erro médio quadrático " +
          str(mean_squared_error(original_depths, noised_depths, squared=False))),
    print_out("Erro médio quadrático normalizado " +
          str(normalized_root_mean_square_error(original_depths, noised_depths)))
    print_out("Coeficiente de Jaccard " +
          str(jaccard_score(original_depths, noised_depths, average="micro")))

    # Histogram original image
    library.plotar_histograma_cinzas(original_depths, "Histograma imagem original",
                                     './images/e_histogram.jpg')
    # Histogram gaussian noise
    library.plotar_histograma_cinzas(gaussian_depths, "Histograma ruído gaussiano",
                                     './images/noise_histogram.jpg')
    # Histogram noised image
    library.plotar_histograma_cinzas(noised_depths, "Histograma imagem ruidosa",
                                     './images/e_noised_histogram.jpg')


# Standard Distribution
# The range of 1-15 is considered low.
# The range 15-30 is considered medium.
# The range 30-50 (Even above) is considered high.
add_gaussian_noise('e', 0)
print_out('')
add_gaussian_noise('e', 5)
print_out('')
add_gaussian_noise('e', 10)
print_out('')
add_gaussian_noise('e', 20)
print_out('')
add_gaussian_noise('e', 30)
