import base64

# read the input image
image_name = 'C:/Users/Garima/Desktop/original.png'
image_read = open(image_name , 'rb').read()

# perform encoding
image_64_encode = base64.encodestring(image_read)

# calculate the compression ratio
compress_ratio = (float(len(image_read)) - float(len(image_64_encode))) / float(len(image_read))
print('CR : %d%%' % (100.0 * compress_ratio))  

# write the compressed result
f = open('compressed.png', 'wb')  
f.write(image_64_encode)  
f.close()

# perform decoding
image_64_decode = base64.decodestring(image_64_encode)

# create a writable image and write the decoding result
image_result = open('decompressed.png', 'wb')
image_result.write(image_64_decode)


