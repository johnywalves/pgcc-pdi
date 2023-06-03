import cv2
import os

def limiarizacao (entrada, saida):
    # Verifica se a imagem de entrada existe e se está no formato correto
    img_path = "images/"+entrada
    if not os.path.isfile(img_path):
        print("Erro: arquivo de imagem não encontrado.")
        exit()
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Erro: o arquivo de imagem está corrompido ou não é suportado.")
        exit()
    # Aplicação do limiar T=220 para obter uma imagem binarizada
    ret, th = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY)
    # Inverte as cores das imagens resultantes
    th = cv2.bitwise_not(th)
    opening = cv2.bitwise_not(ret)
    # Salvar as imagens na pasta "images"
    os.makedirs("images", exist_ok=True)
    cv2.imwrite("images/"+saida, th)


def operacao_morfologica (entrada, saida):
    img = cv2.imread("images/"+entrada, cv2.IMREAD_GRAYSCALE)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    #dilated = cv2.dilate(img, kernel, iterations=1)
    #eroded = cv2.erode(dilated, kernel, iterations=7)
    eroded = cv2.erode(img, kernel, iterations=4)
    cv2.imwrite("images/"+saida, eroded)


limiarizacao ('img4.bmp', 'imgB.bmp')
operacao_morfologica('imgB.bmp','eroded_imgB.bmp')