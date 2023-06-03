import cv2
import numpy as np

# Carregar a imagem
img = cv2.imread('img/Mandrill.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar um limiar para binarizar a imagem (opcional)
_, binary_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Definir um kernel para as operações morfológicas
kernel = np.ones((5, 5), np.uint8)

# Aplicar erosão para remover ruídos e melhorar a forma
eroded_img = cv2.erode(binary_img, kernel, iterations=1)

# Aplicar dilatação para recuperar a forma original
dilated_img = cv2.dilate(eroded_img, kernel, iterations=1)

# Encontrar contornos na imagem dilatada
contours, _ = cv2.findContours(dilated_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Desenhar os contornos na imagem original
contour_img = cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

# Exibir a imagem resultante
cv2.imshow('Imagem com contornos melhorados', contour_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
