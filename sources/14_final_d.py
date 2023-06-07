# Importação da OpenCV2 (Computer Vision)
import cv2

# Carregar a imagem
imagem = cv2.imread("./images_original/14/Mandrill.jpg")

# Converter a imagem para escala de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Aplicar um limiar para segmentação
limiar, imagem_segmentada = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_BINARY)

# Encontrar contornos na imagem segmentada
contornos, _ = cv2.findContours(imagem_segmentada, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Encontrar o maior contorno
maior_contorno = max(contornos, key=cv2.contourArea)

# Calcular o retângulo delimitador da região de interesse
x, y, largura, altura = cv2.boundingRect(maior_contorno)

# Extrair a região de interesse da imagem original
regiao_interesse = imagem[y:y+altura, x:x+largura]

# Mostrar a região de interesse
cv2.imwrite('./images_generate/14/atividadefinal_d.png', regiao_interesse)
