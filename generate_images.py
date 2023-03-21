# Create images 
# in BMP from the struture 
# http://www.ue.eti.pg.gda.pl/fpgalab/zadania.spartan3/zad_vga_struktura_pliku_bmp_en.html

# Install package `pip3 install pillow`
from PIL import Image

# Define function to create image
def create_images(name, quantization): 
    # Create a new black image with 256x256
    # Mode - P (8-bit pixels, mapped to any other mode using a color palette)
    img = Image.new('P', (256, 256))

    pixels = img.load() # Create the pixel map
    for i in range(img.size[0]): # For every pixel:
        for j in range(img.size[1]):
            pixels[i,j] = (quantization(i, j)) # Set the colour accordingly

    img.save(name + '.bmp') # Save file from name

# Create a.bmp image
create_images('a', lambda x, y: 200)

# Create b.bmp image
create_images('b', lambda x, y: 200 if y < 128 else 150)

# Create c.bmp image
def quantization_c(y, x):
    positions_boxs = [
        [20, 40, 20, 40], 
        [20, 40, 120, 140]
    ]
    
    if x < 128:
        for p in positions_boxs:
            if (x > p[0]) and (x <= p[1]) and (y > p[2]) and (y <= p[3]):
                return 150

        return 200

    for p in positions_boxs:
        if (x > (p[0] + 128)) and (x <= (p[1] + 128)) and (y > p[2])  and (y <= p[3]):
            return 200              

    return 150

create_images('c', quantization_c)

# References
# https://stackoverflow.com/questions/20304438/how-can-i-use-the-python-imaging-library-to-create-a-bitmap
# https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes
# https://en.wikipedia.org/wiki/Hoshen%E2%80%93Kopelman_algorithm