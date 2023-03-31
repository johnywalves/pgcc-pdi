# Install package `pip3 install pillow`
from PIL import Image
# The fundamental package for scientific computing with Python
import numpy as np
# Matplotlib: Visualization with Python
import matplotlib.pyplot as plt


def jaccard(original, noised):  # Define Jaccard Similarity function
    intersection = len(list(set(original).intersection(noised)))
    union = (len(original) + len(noised)) - intersection
    return float(intersection) / union


def max_error(original, noised):
    diff = noised - original
    return max(diff)


def root_mean_squared_error(original, noised):
    diff = noised - original
    differences_squared = diff ** 2
    mean_diff = differences_squared.mean()
    rmse_val = np.sqrt(mean_diff)
    return rmse_val


def mean_absolute_error(original, noised):
    diff = noised - original
    abs_diff = np.absolute(diff)
    mean_diff = abs_diff.mean()
    return mean_diff


def create_figure(depths, label, file):
    plt.clf()
    plt.hist(depths, bins=255)
    plt.ylabel('Contagem')
    plt.xlabel('Profundidade')
    plt.title(label)
    plt.savefig('./images/' + file + '.jpg')


def add_gaussian_noise(name):
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
    # Standard Distribution
    # The range of 1-15 is considered low.
    # The range 15-30 is considered medium.
    # The range 30-50 (Even above) is considered high.
    sd = 30

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

    # Flatten the depths of gray
    original_depths = np.ndarray.flatten(np.asarray(original_img))
    gaussian_depths = np.ndarray.flatten(np.asarray(gaussian_img))
    noised_depths = np.ndarray.flatten(np.asarray(noised_img))

    # Display error indicators
    print("Erro máximo " + str(max_error(original_depths, noised_depths)))
    print("Erro médio absoluto " +
          str(mean_absolute_error(original_depths, noised_depths)))
    print("Erro médio quadrático " +
          str(root_mean_squared_error(original_depths, noised_depths)))
    print("Raiz do erro médio quadrático " + str(0)),
    print("Erro médio quadrático normalizado " + str(0))
    print("Coeficiente de Jaccard " +
          str(jaccard(original_depths, noised_depths)))

    # Histogram original image
    create_figure(original_depths, "Histograma imagem original",
                  name + "_histogram")
    # Histogram gaussian noise
    create_figure(gaussian_depths, "Histograma ruído gaussiano",
                  "noise_histogram")
    # Histogram noised image
    create_figure(noised_depths, "Histograma imagem ruidosa",
                  "e_noised_histogram")


add_gaussian_noise('e')
