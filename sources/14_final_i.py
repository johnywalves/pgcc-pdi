import numpy as np
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
print('Contrast:', contrast)
print('Dissimilarity:', dissimilarity)
print('Homogeneity:', homogeneity)
print('Energy:', energy)
print('Correlation:', correlation)
