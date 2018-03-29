# import the libraries
import cv2
import sys
import numpy

# take input of original image
image_filename = 'C:/Users/Garima/Desktop/original.png'
original_image = cv2.imread(image_filename)

# encoding of original image
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
result, encoded_image = cv2.imencode('.jpg', original_image, encode_param)

cv2.imwrite('encoded.png', encoded_image)

# decoding of enocded image
decoded_image = cv2.imdecode(encoded_image, 1)

cv2.imwrite('decoded.jpg', decoded_image)


