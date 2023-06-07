# The fundamental package for scientific computing with Python
import numpy as np
# Importação da biblioteca própria
import library

momento_angular = 0.0004
entropia = 13.1171
contraste = 297.9365
lbp = np.array([[1, 1, 1, 193, 193, 64],
                [199, 255, 239, 231, 195, 96],
                [192, 241, 227, 131, 1, 0],
                [192, 240, 240, 30, 30, 28],
                [0, 16, 16, 30, 30, 28],
                [6, 30, 31, 30, 30, 28]])
df = 1.8536
df_iteracao1 = 4.0000
df_iteracao2 = 12.0000

vetor = np.array([momento_angular, entropia, contraste, lbp, df, df_iteracao1, df_iteracao2])

library.print_out(str(vetor))
