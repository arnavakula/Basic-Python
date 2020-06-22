import cv2

img = cv2.imread('galaxy.jpg', 0) #second param handles color/transparency

print(type(img)) #numpy array
print(img.shape) #rows, columns, channels(color)
print(img.ndim) #num of dimensions

resized_img = cv2.resize(img,(int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow('galaxy', resized_img)
cv2.imwrite('resized_galaxy.jpg', resized_img)
cv2.waitKey(0) #ms
cv2.destroyAllWindows()