# Importação da OpenCV2 (Computer Vision)
import cv2

def limiarizacao (entrada, saida):
    img = cv2.imread("./images_original/12/" + entrada + ".bmp", cv2.IMREAD_GRAYSCALE)

    # Aplicação do limiar T=220 para obter uma imagem binarizada
    ret, th = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY)

    # Inverte as cores das imagens resultantes
    th = cv2.bitwise_not(th)

    # Salvar as imagens
    cv2.imwrite("./images_generate/12/" + saida + ".bmp", th)
    cv2.imwrite("./images_generate/12/" + saida + ".jpg", th)

def operacao_morfologica (entrada, saida):
    img = cv2.imread("./images_generate/12/" + entrada + ".bmp", cv2.IMREAD_GRAYSCALE)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    eroded = cv2.erode(img, kernel, iterations=4)
    cv2.imwrite("./images_generate/12/" + saida + ".jpg", eroded)

limiarizacao ('Img4', 'imgB')
operacao_morfologica('imgB','eroded_imgB')