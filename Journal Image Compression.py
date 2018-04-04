# import the libraries
import cv2
import sys
import numpy
import os

# specify the path of folder
path = 'C:/Users/Garima/Desktop/src/'
encoded_path = 'C:/Users/Garima/Desktop/nen/'
decoded_path = 'C:/Users/Garima/Desktop/nde/'

dirs = os.listdir(path)

# loop on all files in dir
for file in dirs:
    only_file_name = os.path.splitext(file)[0]
    
    srcfile = path + file ;
    
    original_image = cv2.imread(srcfile)

    # encoding of original image
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
    result, encoded_image = cv2.imencode('.jpg', original_image, encode_param)

    # writing the encoded file
    encoded_filename = encoded_path + only_file_name + '_encoded.png'
    cv2.imwrite(encoded_filename, encoded_image)

    # decoding of enocded image
    decoded_image = cv2.imdecode(encoded_image, 1)

    # writing the decoded file
    decoded_filename = decoded_path + only_file_name + '_decoded.jpg'
    cv2.imwrite(decoded_filename, decoded_image)
