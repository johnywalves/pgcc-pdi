# Instalar pacote com `pip3 install pillow`
from PIL import Image
# The fundamental package for scientific computing with Python
import numpy as np
# Importação da biblioteca própria
import library

def boxcount(Z, k):
    S = np.add.reduceat(
        np.add.reduceat(Z, np.arange(0, Z.shape[0], k), axis=0),
                            np.arange(0, Z.shape[1], k), axis=1)
    
    # Count number of boxes with non-empty pixels
    return len(np.where(S > 0)[0])

def fractal_dimension(Z, threshold=0.9):
    # Only for 2d image
    assert(len(Z.shape) == 2)

    def log_n(n):
        if n <= 1:
            return 0
        else:
            return 1 + log_n(n/2)

    # Define the scales
    min_shape = min(Z.shape)
    max_depth = log_n(min_shape) - 1
    sizes = 2**np.arange(max_depth, 1, -1)

    # Compute the fractal dimension
    Ns = np.zeros(sizes.shape)
    for i,size in enumerate(sizes):
        Ns[i] = boxcount(Z, size)

    # Fit the line (on log-log scale)
    coeffs = np.polyfit(np.log(sizes), np.log(Ns), 1)

    # Get the coefficients and the dimension
    df = -coeffs[0]
    df2 = np.nan
    if coeffs.shape[0] > 1:
        # Compute second order coefficient to check quality of fit
        df2 = np.polyfit(np.log(sizes), np.log(Ns), 2)[0]

    return df, df2, Ns[0], Ns[1]

# Load the image and convert to grayscale
image = Image.open("./images_original/13/R0_caso1.jpg").convert("L")

# Convert the image to a numpy array
Z = np.array(image)

# Compute the fractal dimension
df, df2, N1, N2 = fractal_dimension(Z)

# Imprimir resultados
library.print_out("Fractal Dimension (Box Counting): {:.4f}".format(df))
library.print_out("Second Order Coefficient: {:.4f}".format(df2))
library.print_out("N1: {:.4f}".format(N1))
library.print_out("N2: {:.4f}".format(N2))
