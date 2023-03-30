# Install package `pip3 install pillow`
from PIL import Image
# The fundamental package for scientific computing with Python
import numpy as np
# Matplotlib: Visualization with Python
import matplotlib.pyplot as plt

# Define Jaccard Similarity function
def jaccard(act, pred):  
    intersection = len(list(set(act).intersection(pred)))
    union = (len(act) + len(pred)) - intersection
    return float(intersection) / union


def max_error(act, pred):
    diff = pred - act
    return max(diff)


def root_mean_squared_error(act, pred):
    diff = pred - act
    differences_squared = diff ** 2
    mean_diff = differences_squared.mean()
    rmse_val = np.sqrt(mean_diff)
    return rmse_val


def mean_absolute_error(act, pred):
    diff = pred - act
    abs_diff = np.absolute(diff)
    mean_diff = abs_diff.mean()
    return mean_diff


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
    for i in range(original_img.size[0]):
        for j in range(original_img.size[1]):
            # Set the colour accordingly
            gaussian_pixels[i, j] = int(128 + gaussian[i][j])
            noised_pixels[i, j] = int(original_pixels[i, j] + gaussian[i][j])

    gaussian_img.save('./images/noise_gaussian.bmp')
    noised_img.save('./images/' + name + '_noise_gaussian.bmp')

    act = np.ndarray.flatten(np.asarray(original_img))
    gaus = np.ndarray.flatten(np.asarray(gaussian_img))
    pred = np.ndarray.flatten(np.asarray(noised_img))

    print("Erro máximo " + str(max_error(act, pred)))
    print("Erro médio absoluto " + str(mean_absolute_error(act, pred)))
    print("Erro médio quadrático " + str(root_mean_squared_error(act, pred)))
    print("Raiz do erro médio quadrático " + str(0)),
    print("Erro médio quadrático normalizado " + str(0))
    print("Coeficiente de Jaccard " + str(jaccard(act, pred)))

    # Histogram original image
    plt.hist(act, bins=255)
    plt.ylabel('Contagem')
    plt.xlabel('Profundidade')
    plt.title("Histograma imagem original")
    plt.savefig('./images/' + name + '_histogram.jpg')

    # Histogram gaussian noise
    plt.clf()
    plt.hist(gaus, bins=255)
    plt.ylabel('Contagem')
    plt.xlabel('Profundidade')
    plt.title("Histograma ruído gaussiano")
    plt.savefig('./images/noise_histogram.jpg')

    # Histogram noised image
    plt.clf()
    plt.hist(pred, bins=255)
    plt.ylabel('Contagem')
    plt.xlabel('Profundidade')
    plt.title("Histograma imagem ruidosa")
    plt.savefig('./images/e_noised_histogram.jpg')


add_gaussian_noise('e')
