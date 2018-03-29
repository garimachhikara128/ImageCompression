import zlib

# take input of original image
image_filename = 'C:/Users/Garima/Desktop/original.png' 
original_data = open(image_filename, 'rb').read()

# compress the original image
compressed_data = zlib.compress(original_data, 1)

# write the compressed content to file
fc = open('compressed.jpg', 'wb')  
fc.write(compressed_data)  
fc.close()  

# calculate the compression ratio
# compression_ratio = (float(len(original_data)) - float(len(compressed_data))) / float(len(original_data))
# print('Compressed: %d%%' % (100.0 * compression_ratio))  
 
# decompress the compressed file
decompressed_data = zlib.decompress(compressed_data)

# write the decompressed content to file
fd = open('decompressed.jpg', 'wb')  
fd.write(decompressed_data)  
fd.close()  

