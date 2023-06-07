# The fundamental package for scientific computing with Python
import numpy as np
# Importação da biblioteca própria
import library

# R3_caso2.jpg 

momento_angular = 0.0003
entropia = 13.8652
contraste = 916.0583
lbp = np.array([[193., 0., 241., 240., 240., 112.],
                [0., 127., 31., 240., 240., 112.],
                [7., 28., 255., 240., 240., 112.],
                [199., 231., 238., 60., 63., 28.],
                [195., 193., 224., 124., 255., 252.],
                [3., 1., 1., 28., 159., 0.]])
df_logxlog = 1.8536
df_iteracao_1 = 4.0
df_iteracao_2 = 12.0

vetor = np.array([momento_angular, entropia, contraste, df_logxlog, df_iteracao_1, df_iteracao_2])
vetor = np.concatenate((vetor, lbp.flatten()))

library.print_out(str(vetor))
