'''SCRIPT FOR GETTING SHARP FRAMES'''
  
import cv2
import numpy as np
# from serve import 

def ext():
    path = 'static/rbc.mp4' # return filename from serve.py and use it here
    # path = serve.getVideoPath()
    def FrameCapture(path,frame_vector):                               #function to capture the frames
        vidObj= cv2.VideoCapture(path)
        count=0
        success=1
        while success:
            success, image=vidObj.read()
            #image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            frame_vector.append(image) 
            count+=1

    def show(img):                                                    #function to display images
        cv2.imshow('image',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    frames=[]
    img_gray=[]
    FrameCapture(path,frames)
    i=0

    while(i<len(frames)-1):
        temp=cv2.cvtColor(frames[i],cv2.COLOR_BGR2GRAY) #converting rgb to grayscale
        img_gray.append(temp)
        i=i+1
    kernal = np.ones((3,3),np.float32)/9
    sharpness=0
    index=0
    grad_var=[]    
    for i in range(len(img_gray)):
                img_temp=img_gray[i]
                img_blurred=cv2.filter2D(img_temp,-1,kernal)   #blurring filter
                img_blurred=np.array(img_blurred,dtype='float32')
                gy, gx = np.gradient(img_blurred)

                gnorm = np.sqrt(gx**2 + gy**2)
                temp = np.sum(gnorm)
                grad_var.append(temp)
                if(temp>sharpness):
                    sharpness=temp
                    index=i
                    
    # show(frames[index])   #displaying the output image
    cv2.imwrite('./static/sharpFrame.jpg', frames[index])
    # cv2.imshow('Sharp frame', frames[index])
    # cv2.waitKey(0);
    prompt = 'Frame extraction successful!'
    print(prompt)
    # send frames[index] to app.py
    # OR
    # save it as a JPG file ./images using this script only





















# import cv2
# import numpy as np

# # def getVideo():
# #     vid = request.form['inp']
# #     return vid

# # path=r'./video/rbc.mp4' #set path for the video (TO BE RECEIVED FROM THE FRONTEND)
# # # path = app.getVideo()

# def FrameCapture(path,frame_vector):                               #function to capture the frames
#     vidObj=cv2.VideoCapture(path)
#     count=0;
#     success=1;
#     while success:
#         success, image=vidObj.read()
#         #image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#         frame_vector.append(image) 
#         count+=1

# def show(img):                                                    #function to display images
#     cv2.imshow('image',img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# frames=[]
# img_gray=[]
# index = 0

# def process(path):
#     FrameCapture(path,frames)

#     i=0;
#     while(i<len(frames)-1):
#         temp=cv2.cvtColor(frames[i],cv2.COLOR_BGR2GRAY) #converting rgb to grayscale
#         img_gray.append(temp)
#         i=i+1;

#     kernal = np.ones((3,3),np.float32)/9
#     sharpness=0
#     grad_var=[]    
#     for i in range(len(img_gray)):
#                 img_temp=img_gray[i];
#                 img_blurred=cv2.filter2D(img_temp,-1,kernal)   #blurring filter
#                 img_blurred=np.array(img_blurred,dtype='float32')
#                 gy, gx = np.gradient(img_blurred)

#                 gnorm = np.sqrt(gx**2 + gy**2)
#                 temp = np.sum(gnorm)
#                 grad_var.append(temp)
#                 if(temp>sharpness):
#                     sharpness=temp
#                     index=i;
#     cv2.imwrite("images/sharp_frame.jpg", frames[index])        

# # show(frames[index])   #displaying the output image

# # save image frame