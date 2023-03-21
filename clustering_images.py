# Install package `pip3 install pillow`
from PIL import Image

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


def cluster_image(name):
    largest_label = 0
    colors = []
    colors_label = []

    img = Image.open(name + ".bmp")
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

                    # Neither a label above nor to the left
                    if (left == 0) and (above == 0):
                        # Make a new, as-yet-unused cluster label
                        largest_label = largest_label + 1
                        label[x][y] = largest_label
                    elif (left != 0) and (above == 0):  # One neighbor, to the left
                        label[x][y] = find(labels, left)
                    elif (left == 0) and (above != 0):  # One neighbor, above
                        label[x][y] = find(labels, above)
                    else:  # Neighbors BOTH to the left and above
                        # Link the left and above clusters
                        union(labels, left, above)
                        label[x][y] = find(labels, left)

        colors_label.append(label)

    # Generate clustered
    img_clustered = Image.new('RGB', (256, 256))
    pixels = img_clustered.load()
    for label in colors_label:
        for i in range(img_clustered.size[0]):
            for j in range(img_clustered.size[1]):
                if (label[i][j] != 0):
                    pixels[i, j] = cluster_colors[label[i][j] - 1]

    img_clustered.save(name + '_clustered.bmp')


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
