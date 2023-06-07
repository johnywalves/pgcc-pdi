# The fundamental package for scientific computing with Python
import numpy as np
# Importação da biblioteca própria
import library

import mahotas as mh
from skimage.io import imread

# Carregando a imagem segmentada
image_path = './images_generate/14/atividadefinal_h.png'
segmented_image = imread(image_path, as_gray=True)

# Calculando a matriz de coocorrência
glcm = mh.features.haralick(segmented_image.astype(np.uint8))

# Extraindo as características de textura
contrast = glcm.mean(axis=0)[2]
dissimilarity = glcm.mean(axis=0)[4]
homogeneity = glcm.mean(axis=0)[8]
energy = glcm.mean(axis=0)[1]
correlation = glcm.mean(axis=0)[5]

# Exibindo as características calculadas
library.print_out('Contrast: ' + str(contrast))
library.print_out('Dissimilarity: ' + str(dissimilarity))
library.print_out('Homogeneity: ' + str(homogeneity))
library.print_out('Energy: ' + str(energy))
library.print_out('Correlation: ' + str(correlation))
