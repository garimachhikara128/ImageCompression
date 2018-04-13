# import the libraries
import cv2
import sys
import numpy
import os
import time

# specify the path of folder
path = 'E:/Capstone Project/New Video For Journal Zip/original/'
encoded_path = 'F:/Capstone Project/3_New Video For Journal Only JPEG/Encoded/'
decoded_path = 'F:/Capstone Project/3_New Video For Journal Only JPEG/Decoded/'

dirs = os.listdir(path)

start_time = time.time()

# loop on all files in dir
for file in dirs:
    only_file_name = os.path.splitext(file)[0]
    
    srcfile = path + file ;
    
    original_image = cv2.imread(srcfile)

    # encoding of original image
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 95]
    result, encoded_image = cv2.imencode('.jpg', original_image, encode_param)

    # writing the encoded file
    encoded_filename = encoded_path + only_file_name + '_encoded.png'
    cv2.imwrite(encoded_filename, encoded_image)

    # decoding of enocded image
    decoded_image = cv2.imdecode(encoded_image, 1)

    # writing the decoded file
    decoded_filename = decoded_path + only_file_name + '_decoded.png'
    cv2.imwrite(decoded_filename, decoded_image)

end_time = time.time()

print(end_time - start_time)
