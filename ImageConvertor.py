from PIL import Image
import bitarray

def file_to_bitarray(path):
    result = bitarray.bitarray()
    with open(path, "rb") as file:
        result.fromfile(file)
    return result

def bitarray_to_file(path,bits):
    with open(path, "wb") as file:
        bits.tofile(file)

def set_last_bit(value, integer):
    bits = '{0:b}'.format(integer)
    return int(bits[0:len(bits)-1] + str(value), 2)

def get_last_bit(integer):
    bits = '{0:b}'.format(integer)
    return int(bits[len(bits)-1])

def hide(in_file, secret="test.txt", out_file = "output.png"):
    im = Image.open(in_file)
    pic = im.load()
    width, height = im.size
    to_hide = file_to_bitarray(secret)
    k = 0
    l = len(to_hide)
    for y in range(height):
        for x in range(width):
            pixel = pic[x,y]
            r = set_last_bit(to_hide[k%l], pixel[0])
            k += 1
            g = set_last_bit(to_hide[k%l], pixel[1])
            k += 1
            b = set_last_bit(to_hide[k%l], pixel[2])
            k += 1
            pic[x,y] = (r,g,b)
    im.save(out_file)

def seek(in_file, out_file = "out.txt"):
    im = Image.open(in_file)
    pic = im.load()
    width, height = im.size
    bits = ""
    for y in range(height):
        for x in range (width):
            pixel = pic[x,y]
            bits += str(get_last_bit(pixel[0]))
            bits += str(get_last_bit(pixel[1]))
            bits += str(get_last_bit(pixel[2]))
    bitarray_to_file(out_file, bitarray.bitarray(bits))

