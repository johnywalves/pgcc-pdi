# Install package `pip3 install pillow`
from PIL import Image
# The fundamental package for scientific computing with Python
import numpy as np
# Matplotlib: Visualization with Python
import matplotlib.pyplot as plt
# Importação de métricas sobre predição
from sklearn.metrics import max_error, jaccard_score,  mean_absolute_error, mean_squared_error


def normalized_root_mean_square_error(original, noised):
    squared_sums = sum((original - noised) ^ 2)
    mse = squared_sums / len(original)
    rmse = np.sqrt(mse)
    nrmse = rmse / np.std(original)
    nrmse = round(nrmse, 3)

    return (nrmse)


def create_figure(depths, label, file):
    plt.clf()
    plt.hist(depths, bins=255)
    plt.ylabel('Contagem')
    plt.xlabel('Profundidade')
    plt.title(label)
    plt.savefig('./images/' + file + '.jpg')


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
    print("Desvio padrão " + str(sd))

    # Flatten the depths of gray
    original_depths = np.ndarray.flatten(np.asarray(original_img))
    gaussian_depths = np.ndarray.flatten(np.asarray(gaussian_img))
    noised_depths = np.ndarray.flatten(np.asarray(noised_img))

    # Display error indicators
    print("Erro máximo " + str(max_error(original_depths, noised_depths)))
    print("Erro médio absoluto " +
          str(mean_absolute_error(original_depths, noised_depths)))
    print("Erro médio quadrático " +
          str(mean_squared_error(original_depths, noised_depths)))
    print("Raiz do erro médio quadrático " +
          str(mean_squared_error(original_depths, noised_depths, squared=False))),
    print("Erro médio quadrático normalizado " +
          str(normalized_root_mean_square_error(original_depths, noised_depths)))
    print("Coeficiente de Jaccard " +
          str(jaccard_score(original_depths, noised_depths, average="micro")))

    # Histogram original image
    create_figure(original_depths, "Histograma imagem original",
                  name + "_histogram")
    # Histogram gaussian noise
    create_figure(gaussian_depths, "Histograma ruído gaussiano",
                  "noise_histogram")
    # Histogram noised image
    create_figure(noised_depths, "Histograma imagem ruidosa",
                  "e_noised_histogram")


# Standard Distribution
# The range of 1-15 is considered low.
# The range 15-30 is considered medium.
# The range 30-50 (Even above) is considered high.

add_gaussian_noise('e', 0)
print('')
add_gaussian_noise('e', 5)
print('')
add_gaussian_noise('e', 10)
print('')
add_gaussian_noise('e', 20)
print('')
add_gaussian_noise('e', 30)
