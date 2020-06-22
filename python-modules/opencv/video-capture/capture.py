import cv2, time

video = cv2.VideoCapture(0) #num for webcam, fp for recorded video
frames = 1

while True:
    frames += 1
    check, frame = video.read() 

    cv2.imshow('Video-Capture', frame) #first frame of video

    key = cv2.waitKey(1)

    if key == ord('q'):
        break


print('Frames:', frames)
video.release()
cv2.destroyAllWindows()