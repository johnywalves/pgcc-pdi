# Install package `pip3 install pillow`
from PIL import Image

n_columns = 256
n_rows = 256
cluster_colors = [
    (255, 0, 0), (128, 0, 0),
    (0, 128, 0), (0, 255, 0),
    (0, 0, 128), (0, 0, 255)
]

colors = [200]

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


def cluster_image(labels, label, name):
    largest_label = 0
    img = Image.open(name + ".bmp")

    for c in range(len(colors)):
        for x in range(n_columns):
            for y in range(n_rows):
                if img.getpixel((x, y)) == colors[c]:
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
                        union(labels, left, above)  # Link the left and above clusters
                        label[x][y] = find(labels, left)

    # Generate clustered
    img_clustered = Image.new('RGB', (256, 256))
    pixels = img_clustered.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            labelred = label[i][j]
            if (labelred == 0):
                pixels[i, j] = (200, 200, 200)
            else:
                pixels[i, j] = cluster_colors[labelred - 1]

    img_clustered.save('clustered_' + name + '.bmp')

def main(name):
    label = []
    for x in range(n_columns):
        label.append([])
        for y in range(n_rows):
            label[x].append(0)

    # Array containing integers from 0 to the size of the image
    labels = list(range(n_columns * n_rows + 1))

    cluster_image(labels, label, name)

# Clustering image a.bmp
main('a')

# Clustering image b.bmp
main('b')

# Clustering image c.bmp
main('c')

# Clustering image d.bmp
main('d')

# Clustering image e.bmp
main('e')
