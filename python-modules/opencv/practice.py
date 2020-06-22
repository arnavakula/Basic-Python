import cv2, glob
from pathlib import Path

images = glob.glob('images//*.jpg')
print(images)

for fp in images:
    img = cv2.imread(fp, 0)
    rimg = cv2.resize(img, (100, 100))
    cv2.imshow('images', rimg)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    print(Path(fp).stem)
    cv2.imwrite('resized_images//'+Path(fp).stem+'.jpg', rimg)