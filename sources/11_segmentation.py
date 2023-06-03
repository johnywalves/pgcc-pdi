# Instalar pacote com `pip3 install pillow`
from PIL import Image
# The fundamental package for scientific computing with Python
import numpy as np
# Importação da biblioteca própria
import library

# Carrega a imagem de entrada
img = Image.open("./images_original/11/Img_seg.jpg").convert('RGB')

# Converte a imagem para um array numpy
img_array = np.array(img)

# Separa os canais de cor da imagem
blue_channel = img_array[:, :, 2]
red_channel = img_array[:, :, 0]

# Calcula a diferença entre os canais azul e vermelho
diff = blue_channel.astype(int) - red_channel.astype(int)

# Limiariza a imagem
thresh = np.where(diff > 20, 255, 0).astype(np.uint8)

# Realiza a operação de abertura para remover ruídos
kernel = np.ones((5, 5), np.uint8)
opening = np.zeros_like(thresh)

# Percorre a imagem com o elemento estruturante
for i in range(kernel.shape[0] // 2, opening.shape[0] - kernel.shape[0] // 2):
    for j in range(kernel.shape[1] // 2, opening.shape[1] - kernel.shape[1] // 2):
        if thresh[i, j] != 0:
            opening[i - kernel.shape[0] // 2:i + kernel.shape[0] // 2 + 1,
                    j - kernel.shape[1] // 2:j + kernel.shape[1] // 2 + 1] |= kernel

# Encontra os contornos na imagem limiarizada
contours = []
for i in range(opening.shape[0]):
    for j in range(opening.shape[1]):
        if opening[i, j] != 0:
            contour = [(j, i)]
            while True:
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if di == 0 and dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        if (
                            ni >= 0 
                            and nj >= 0 
                            and ni < opening.shape[0] 
                            and nj < opening.shape[1] 
                            and opening[ni, nj] != 0
                            ):
                            opening[ni, nj] = 0
                            contour.append((nj, ni))
                            i, j = ni, nj
                            break
                    else:
                        continue
                    break
                else:
                    break
            if len(contour) > 2:
                contours.append(np.array(contour))

# Desenha os contornos encontrados na imagem original
for contour in contours:
    for i in range(len(contour)):
        x0, y0 = contour[i - 1]
        x1, y1 = contour[i]
        img_array[y0, x0] = [0, 255, 0]
        img_array[y1, x1] = [0, 255, 0]

# Define as regiões de controle para cálculo das taxas
regions = [
    {'name': 'region1', 'center': (500, 500), 'radius': 50},
    {'name': 'region2', 'center': (700, 700), 'radius': 50},
    {'name': 'region3', 'center': (900, 900), 'radius': 50},
    {'name': 'region4', 'center': (1100, 1100), 'radius': 50}
]

# Inicializa as variáveis de contagem
tp = 0
fp = 0
tn = 0

# Define as regiões de controle para cálculo das taxas
regions_of_interest = [
    # (centro_x, centro_y, raio)
    (400, 550, 25),   # região 1
    (800, 500, 50),   # região 2
    (1150, 350, 75),  # região 3
    (1200, 650, 100)  # região 4
]

# Calcula as taxas de acerto e erro
true_positives = 0
false_positives = 0
true_negatives = 0
false_negatives = 0

for region in regions_of_interest:
    # Extrai as informações da região de controle
    center_x, center_y, radius = region
    
    # Verifica se há algum contorno dentro da região
    found = False
    for contour in contours:
        for point in contour:
            x, y = point
            distance = np.sqrt((x - center_x)**2 + (y - center_y)**2)
            if distance < radius:
                found = True
                break
        if found:
            break
    
    # Atualiza as taxas
    if found:
        true_positives += 1
    else:
        false_negatives += 1
    
    for contour in contours:
        for point in contour:
            x, y = point
            distance = np.sqrt((x - center_x)**2 + (y - center_y)**2)
            if distance < radius:
                false_positives += 1
                break
    
    true_negatives += thresh.shape[0] * thresh.shape[1] - true_positives - false_positives - false_negatives
    
accuracy = (true_positives + true_negatives) / (true_positives + true_negatives + false_positives + false_negatives)
if true_positives + false_positives == 0:
    precision = 0.0
else:
    precision = true_positives / (true_positives + false_positives)

recall = true_positives / (true_positives + false_negatives)

library.print_out("Taxas de acerto e erro:")
library.print_out(f"Acurácia: {accuracy:.2f}")
library.print_out(f"Precisão: {precision:.2f}")
library.print_out(f"Recall: {recall:.2f}")

# Desenha os contornos encontrados na imagem original
for contour in contours:
    for i in range(len(contour)):
        x0, y0 = contour[i - 1]
        x1, y1 = contour[i]
        if x0 >= 0 and x0 < img_array.shape[1] and y0 >= 0 and y0 < img_array.shape[0]:
            img_array[y0, x0] = [0, 255, 0]
        if x1 >= 0 and x1 < img_array.shape[1] and y1 >= 0 and y1 < img_array.shape[0]:
            img_array[y1, x1] = [0, 255, 0]

# Salva a imagem segmentada
Image.fromarray(img_array).save("./images_generate/11/Img_seg_segmentada.jpg")