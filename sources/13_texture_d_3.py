# The fundamental package for scientific computing with Python
import numpy as np
# Importação da biblioteca própria
import library

# R3_caso1.jpg

momento_angular = 0.0002
entropia = 13.6887
contraste = 714.1787
lbp = np.array([[64., 112., 112., 48., 48., 48.],
                [64., 120., 124., 124., 124., 124.],
                [64., 120., 248., 120., 248., 120.],
                [0., 18., 31., 15., 15., 12.],
                [6., 30., 31., 15., 15., 12.],
                [6., 30., 30., 14., 30., 28.]])
df_logxlog = 1.8536
df_iteracao_1 = 4.0
df_iteracao_2 = 12.0

vetor = np.array([momento_angular, entropia, contraste, df_logxlog, df_iteracao_1, df_iteracao_2])
vetor = np.concatenate((vetor, lbp.flatten()))

library.print_out(str(vetor))
