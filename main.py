import cv2
import copy
import numpy
from math import floor

#---------------------------------------------------------------------------------------------------------

last = None

video = cv2.VideoCapture(0)     # Open default Webcam, gotta change when i get hands on intel rlsense
if not video.isOpened():
    print("Cannot open camera")
    exit()

#-----------------------------------------


while True:    
        ret, img = video.read()
        #ret is a boolean that checks if the camera is reding anything
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        

        # Convert to graycsale
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Blur the image for better edge detection
        img_blur = cv2.GaussianBlur(img_gray, (1,1), 0)

        # Sobel Edge Detection
        sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
        sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
        sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection

        # Canny Edge Detection
        edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection




        #===========================================================================
        # img_gray = cv2.cvtColor(sobelxy, cv2.COLOR_BGR2GRAY)
        # # Blur the image for better edge detection
        # img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
        # sobelxyxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)
        # edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
        # # Display Canny Edge Detection Image
        # print('Canny Edge Detection')
        # cv2_imshow(edges)
        # cv2.waitKey(0)
        #===========================================================================

        cv2.imshow("Frame", edges)    # Show video frame
        
        key = cv2.waitKey(1)        # Breaks the loop if 'q' is pressed
        if key == ord('q'):
            break

video.release()
cv2.destroyAllWindows()





     

