# import cv2
# vidcap = cv2.VideoCapture('/home/tahn/VS_Code/3D/Gopro.mp4')
# print(vidcap.isOpened())
# success, image = vidcap.read()
# count = 1
# while success:
#   cv2.imwrite("video_data/image_%d.jpg" % count, image)    
#   success, image = vidcap.read()
#   print('Saved image ', count)
#   count += 1

# Importing all necessary libraries
import cv2
import os
  
# Read the video from specified path
cam = cv2.VideoCapture('/home/tahn/VS_Code/3D/IMG_7663.MOV')
  
try:
      
    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')
  
# if not created then raise error
except OSError:
    print ('Error: Creating directory of data')
  
# frame
currentframe = 0
count = 0
while(True):
      
    # reading from frame
    ret,frame = cam.read()
    
    if ret:
        count += 1
        if count % 10 == 0:
            # if video is still left continue creating images
            name = './data/frame' + str(currentframe) + '.jpg'
            print ('Creating...' + name)
        
            # writing the extracted images
            cv2.imwrite(name, frame)
            count = 0
  
        # increasing counter so that it will
        # show how many frames are created
            currentframe += 1
    else:
        break
  
# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()
