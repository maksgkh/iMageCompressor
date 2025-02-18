from PIL import Image
import os,sys

#Path of your library/photo(in progress)
''''path = r'C:\Users\''''

for file in os.listdir(path): 
    if file.endswith(".jpg"): 
        img = Image.open(file)
        file_name, file_ext = os.path.splitext(file)
        img.save('/png/{}.png'.format(file_name))

#main ALG programm
def main():
    im= Image.open('test.jpg')
    print(im.format,im.size, im.mode)
    print(im.show())
main()

# Convertion to JPEG function(in progress)
def converter_jpeg(f):
    for file in os.listdir(path): 
        if file.endswith(".jpg"): 
            img = Image.open(file)
            file_name, file_ext = os.path.splitext(file)
            img.save('/png/{}.png'.format(file_name))