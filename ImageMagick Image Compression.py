# run in python idle

from wand.image import Image

with Image(filename="C:/Users/Garima/Desktop/original.png") as img:
    
    img.compression_quality = 75
    img.save(filename="C:/Users/Garima/Desktop/compressed.png")
