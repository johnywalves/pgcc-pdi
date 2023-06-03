# Instalar pacote com `pip3 install pillow`
from PIL import Image
# Importação da biblioteca própria
import library

import random
import math

n_columns = 256
n_rows = 256
cluster_colors = [
    (214, 39, 40),
    (31, 119, 180),
    (255, 127, 14),
    (44, 160, 44),
    (148, 103, 189),
    (140, 86, 75),
    (227, 119, 194),
    (188, 189, 34),
    (23, 190, 207),
    (214, 39, 40),
    (31, 119, 180),
    (255, 127, 14),
    (44, 160, 44),
    (148, 103, 189),
    (140, 86, 75),
    (227, 119, 194),
    (188, 189, 34),
    (23, 190, 207),
]

def distance_euclidean(first, second):
    (x1, y1) = first
    (x2, y2) = second
    return str(math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2)))

def distance_four(first, second):
    (x1, y1) = first
    (x2, y2) = second
    return str(abs(x1 - x2) + abs(y1 - y2))

def distance_eight(first, second):
    (x1, y1) = first
    (x2, y2) = second
    return str(max(abs(x1 - x2), abs(y1 - y2)))

def find(labels, x):
    y = x

    while (labels[y] != y):
        y = labels[y]

    while (labels[x] != x):
        z = labels[x]
        labels[x] = y
        x = z
    return y

def union(labels, x, y):
    labels[find(labels, x)] = find(labels, y)

def is_connected(first, second):
    fxi, fyi, fxf, fyf = first
    sxi, syi, sxf, syf = second
    return (fxi + 1 == sxf) or (fxf + 1 == sxi) or (fyi + 1 == syf) or (fyf + 1 == syi)

def cluster_image(name):
    largest_label = 0
    total_labels = []
    positions_labels = []
    colors = []
    colors_label = []

    img = Image.open('./images_original/' + name + ".bmp")
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            gray = img.getpixel((i, j))
            if gray not in colors:
                colors.append(gray)

    for color in colors:
        # Matrix from image with zeros
        label = []
        for x in range(n_columns):
            label.append([])
            for y in range(n_rows):
                label[x].append(0)

        # Array containing integers from 0 to the size of the image
        labels = list(range(n_columns * n_rows + 1))

        for x in range(n_columns):
            for y in range(n_rows):
                if img.getpixel((x, y)) == color:
                    left = 0 if x == 0 else label[x - 1][y]
                    above = 0 if y == 0 else label[x][y - 1]
                    adjacent = 0 if x == 0 and y == 0 else label[x - 1][y - 1]

                    # Neither a label above nor to the left
                    if (left == 0) and (above == 0) and (adjacent == 0):
                        # Make a new, as-yet-unused cluster label
                        largest_label = largest_label + 1
                        label[x][y] = largest_label
                    elif (left != 0) and (above == 0) and (adjacent == 0):  # One neighbor, to the left
                        label[x][y] = find(labels, left)
                    elif (left == 0) and (above != 0) and (adjacent == 0):  # One neighbor, above
                        label[x][y] = find(labels, above)
                    elif (left == 0) and (above == 0) and (adjacent != 0):  # One neighbor, adjacent
                        label[x][y] = find(labels, adjacent)
                    # Neighbors BOTH to the left and above
                    elif (left != 0) and (above != 0) and (adjacent == 0):
                        # Link the left and above clusters
                        union(labels, left, above)
                        label[x][y] = find(labels, left)
                    # Neighbors BOTH to the left and adjacent
                    elif (left != 0) and (above == 0) and (adjacent != 0):
                        # Link the left and adjacent clusters
                        union(labels, left, adjacent)
                        label[x][y] = find(labels, left)
                    # Neighbors BOTH to the above and adjacent and ALL of them
                    else:
                        # Link the above and adjacent clusters
                        union(labels, above, adjacent)
                        label[x][y] = find(labels, above)

        colors_label.append(label)

    # Generate clustered
    img_clustered = Image.new('RGB', (256, 256))
    pixels = img_clustered.load()
    for label in colors_label:
        for i in range(img_clustered.size[0]):
            for j in range(img_clustered.size[1]):
                if (label[i][j] != 0):
                    code = label[i][j]

                    if code not in total_labels:
                        total_labels.append(code)
                        positions_labels.append([j, i, 0, 0])
                    else:
                        index = total_labels.index(code)
                        xi, yi, xf, yf = positions_labels[index]
                        positions_labels[index] = [xi, yi, j, i]

                    pixels[i, j] = cluster_colors[code - 1]

    img_clustered.convert('RGB').save('./images_generate/02/' + name + '_clustered.jpg')

    library.print_out('==========================')
    library.print_out('Nome: ' + name)
    library.print_out('Quantidade de grupos: ' + str(len(total_labels)))
    library.print_out('Rótulos dos grupos: ' + ", ".join([str(i) for i in total_labels]))

    if name == 'e':
        code_ref = random.randrange(0, len(total_labels) - 1)
        code_connected = random.randrange(0, len(total_labels) - 1)

        first = positions_labels[code_ref]
        second = positions_labels[code_connected]

        while (not is_connected(first, second)) or (code_ref == code_connected):
            code_connected = random.randrange(0, len(total_labels) - 1)
            second = positions_labels[code_connected]

        fxi, fyi, fxf, fyf = first
        sxi, syi, sxf, syf = second

        x1 = (fxf - fxi + 1) / 2 + fxi
        y1 = (fyf - fyi + 1) / 2 + fyi
        x2 = (sxf - sxi + 1) / 2 + sxi
        y2 = (syf - syi + 1) / 2 + syi

        library.print_out(
                "\nCoordenadas Primeiro: (" + 
                str(fxi) + ', ' + str(fyi) + ") a (" + 
                str(fxf) + ', ' + str(fyf) + ") centro (" + 
                str(x1) + ", " + str(y1) + ")"
            )
        library.print_out(
                "Coordenadas Segundo: (" + 
                str(sxi) + ', ' + str(syi) + ") a (" + 
                str(sxf) + ', ' + str(syf) + ") centro (" + 
                str(x2) + ", " + str(y2) + ")"
            )

        library.print_out(
                "Distância Euclidiana: " + distance_euclidean((x1, y1), (x2, y2))
            )
        library.print_out(
                "Distância Quadro: " + distance_four((x1, y1), (x2, y2))
            )
        library.print_out(
                "Distância Oito: " + distance_eight((x1, y1), (x2, y2))
            )

# Clustering image a.bmp
cluster_image('a')

# Clustering image b.bmp
cluster_image('b')

# Clustering image c.bmp
cluster_image('c')

# Clustering image d.bmp
cluster_image('d')

# Clustering image e.bmp
cluster_image('e')
