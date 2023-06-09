# Instalar pacote com `pip3 install pillow`
from PIL import Image
# The fundamental package for scientific computing with Python
import numpy as np

from sklearn.cluster import KMeans

# Carregar a imagem
imagem = Image.open('./images_original/14/Mandrill.jpg')

# Converter a imagem em uma matriz numpy
imagem_array = np.array(imagem)

# Redimensionar a matriz para 2D
largura, altura, _ = imagem_array.shape
dados = imagem_array.reshape(largura * altura, -1)

# Aplicar o algoritmo K-means
numero_clusters = 5  # Defina o número de clusters desejado
kmeans = KMeans(n_clusters=numero_clusters, random_state=0)
kmeans.fit(dados)

# Obter os rótulos dos clusters para cada pixel
rotulos = kmeans.labels_

# Redimensionar os rótulos para a forma da imagem
rotulos = rotulos.reshape(largura, altura)

# Mostrar a imagem original e a imagem com as regiões classificadas
#imagem.save('./images_generate/14/atividadefinal_k.png')

imagem_classificada = Image.fromarray(rotulos.astype(np.uint8) * int(255 / (numero_clusters - 1)))
imagem_classificada.convert('RGB').save('./images_generate/14/atividadefinal_k.png')
