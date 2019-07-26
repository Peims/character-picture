#@author pms
from PIL import Image

def pic2ascii(pic, asciis, zoom, vscale):
    img = Image.open(pic)
    
    out = img.convert("L")
    
    width, height = out.size
    
    out = out.resize((int(width * zoom), int(height * zoom * vscale)))
    ascii_len = len(asciis)
    texts = ''

    for row in range(out.height):
        for col in range(out.width):
            gray = out.getpixel((col, row))
            texts += asciis[int((gray / 255) * (ascii_len - 1))]
        texts += '\n'

    return texts

def main():
    pic = input("input name of the picture")
    
    asciis = "@%#*+=-:. "
    
    zoom = 0.1
    
    vscale = 0.5
    texts = pic2ascii(pic, asciis, zoom, vscale)
    
    with open("ascii.txt", "w") as file:
        file.write(texts)

if __name__ == "__main__":
    main()
