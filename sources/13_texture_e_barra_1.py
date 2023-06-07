# The fundamental package for scientific computing with Python
import numpy as np
# Matplotlib: Visualization with Python
from matplotlib import pyplot as plt

# Gráfico barras gerado a partir da imagem R0_caso1.jpg
df_logxlog = 1.8536
df_iteracao_1 = 4.0
df_iteracao_2 = 12.0

valores_df = np.array([df_logxlog, df_iteracao_1, df_iteracao_2])
nomes_df = ['DF logxlog', 'DF Iteração 1', 'DF Iteração 2']
plt.bar(nomes_df, valores_df)
plt.xlabel('Descritores DF')
plt.ylabel('Valores')

plt.savefig('./images_generate/13/R0_caso1_grafico_barras.png')


