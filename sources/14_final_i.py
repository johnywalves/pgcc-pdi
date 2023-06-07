# The fundamental package for scientific computing with Python
import numpy as np
# Importação da biblioteca própria
import library

import mahotas as mh
from skimage.io import imread

# Carregando a imagem segmentada
image_path = 'img/segmentada.png'
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
library.print_out('Contrast:', contrast)
library.print_out('Dissimilarity:', dissimilarity)
library.print_out('Homogeneity:', homogeneity)
library.print_out('Energy:', energy)
library.print_out('Correlation:', correlation)
