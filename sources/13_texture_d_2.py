# The fundamental package for scientific computing with Python
import numpy as np
# Importação da biblioteca própria
import library

# R0_caso2.jpg

momento_angular = 0.0008
entropia = 12.1974
contraste = 209.8217
lbp = np.array([[193., 241., 241., 193., 193., 64.],
                [199., 255., 255., 231., 231., 100.],
                [199., 255., 255., 225., 225., 96.],
                [7., 15., 15., 135., 135., 4.],
                [7., 143., 15., 135., 135., 4.],
                [7., 15., 15., 15., 7., 4.]])
df_logxlog = 1.8536
df_iteracao_1 = 4.0
df_iteracao_2 = 12.0

vetor = np.array([momento_angular, entropia, contraste, df_logxlog, df_iteracao_1, df_iteracao_2])
vetor = np.concatenate((vetor, lbp.flatten()))

library.print_out(str(vetor))
