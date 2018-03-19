import os, sys, time, subprocess

# Open a file
path = "E:/Capstone Project/New for Journal/2_MPEF with JPEG/"
srcpath = path + "/1_Compressed Image Frames/lou_dyn/"
dstpath = path + "2_Compressed MPEG/lou_dyn/"
dirs = os.listdir( srcpath )

start_time = time.time()

# This would print all the files and directories
for file in dirs:
    #print (file)
    srcfile = srcpath + file ;
    dstfile = dstpath + file ;

    #print(srcfile)
    #os.system('ffmpeg -i "' + srcfile + '" -q:v 3 "' + dstfile + '"')
    #first three - 3, franck - 5 , ll - 3.5  
    subprocess.call('ffmpeg -i "' + srcfile + '" -q:v 3.4 "' + dstfile + '"', shell = True)

end_time = time.time()

print(end_time - start_time)
