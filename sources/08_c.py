# Importação da biblioteca de tratamento de imagens
from PIL import Image
# The fundamental package for scientific computing with Python
import numpy as np
# Importação da biblioteca própria
import library

from scipy.signal import medfilt2d

# carrega a imagem de entrada
img_in = Image.open('./images_original/e.bmp').convert('L')

# converte a imagem para matriz NumPy
img_in_arr = np.array(img_in)

# aplica o filtro de mediana
img_out_arr = medfilt2d(img_in_arr, kernel_size=3)

# converte a imagem de saída para matriz NumPy
img_out = Image.open('./images_original/e_ruido_salpimenta_Suavizacao_mediana.bmp').convert('L')
img_out_arr = np.array(img_out)

# calcula a diferença absoluta entre as duas imagens
diff_arr = np.abs(img_in_arr - img_out_arr)

# calcula a média da diferença absoluta
mae = np.mean(diff_arr)
library.print_out('A diferença média absoluta entre as imagens é: ' + str(mae))
