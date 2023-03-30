# Create images
# in BMP from the struture
# http://www.ue.eti.pg.gda.pl/fpgalab/zadania.spartan3/zad_vga_struktura_pliku_bmp_en.html

# Install package `pip3 install pillow`
from PIL import Image


def create_images(name, quantization):  # Define function to create image
    # Create a new black image with 256x256
    # Mode - P (8-bit pixels, mapped to any other mode using a color palette)
    img = Image.new('P', (256, 256))

    pixels = img.load()  # Create the pixel map
    for i in range(img.size[0]):  # For every pixel:
        for j in range(img.size[1]):
            pixels[i, j] = (quantization(i, j))  # Set the colour accordingly

    img.save('./images/' + name + '.bmp')  # Save file from name


# Create a.bmp image
create_images('a', lambda x, y: 200)


# Create b.bmp image
create_images('b', lambda x, y: 200 if y < 128 else 150)


# Create c.bmp image
def quantization_c(x, y):
    # Coordenates to Boxs
    # (X initial, Y inital, X final, Y final)
    positions_boxs = [
        [45, 55, 85, 75],
        [173, 55, 213, 75],
        [45, 55 + 128, 85, 75 + 128],
        [173, 55 + 128, 213, 75 + 128]
    ]

    def inner_box(a, b):
        for p in positions_boxs:
            if (a > p[0]) and (a <= p[2]) and (b > p[1]) and (b <= p[3]):
                return True
        return False

    if y < 128:
        if inner_box(x, y):
            return 150

        return 200

    if inner_box(x, y):
        return 200

    return 150


create_images('c', quantization_c)


# Create d.bmp image
def quantization_d(x, y):
    if (x // 128 == 1) and (y // 128 == 1):
        return 225

    if (x // 128 == 1) or (y // 128 == 1):
        return 200

    return 150


create_images('d', quantization_d)


# Create e.bmp image
create_images('e', lambda x, y: 110 + (x // 64 * 10) + (y // 64 * 40))


# References
# https://stackoverflow.com/questions/20304438/how-can-i-use-the-python-imaging-library-to-create-a-bitmap
# https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes
# https://en.wikipedia.org/wiki/Hoshen%E2%80%93Kopelman_algorithm
