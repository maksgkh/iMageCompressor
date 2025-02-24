from PIL import Image
import os,sys

#Path of your library/photo(in progress)
path = r'C:/programming/2025/iMageCompressor'

# Convertion to PNG function
def converter_png():
    for file in os.listdir(path): 
        if file.endswith(".jpg"): 
            img = Image.open(file)
            file_name, file_ext = os.path.splitext(file)
            img.save('C:/programming/2025/iMageCompressor/{}.png'.format(file_name))

#open programm
def open():
    im= Image.open('123.png')
    print(im.format,im.size, im.mode)
    print(im.show())


# Convertion to JPEG function

def converter_jpeg():
    for file in os.listdir(path): 
        if file.endswith(".png"): 
            img = Image.open(file)
            file_name, file_ext = os.path.splitext(file)
            img.save('C:/programming/2025/iMageCompressor/{}.jpg'.format(file_name))

#Main function
def main():
    print(os.listdir())
    print("Вот список файлов в вашей папке,что вы хотите сделать с ними")
    print('1.Converter to JPEG. 2.Converter to PNG')
    arg=input("Please select your option: ")
    arg = int(arg)
    if arg == 1: converter_jpeg()
    elif arg == 2: converter_png()
    else:
        arg=input("Please select your option: ")
        arg = int(arg)
    
main()