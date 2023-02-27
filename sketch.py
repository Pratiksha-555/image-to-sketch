#import opencv libraries
import cv2
import matplotlib.pyplot as plt

#read image using opencv
path=r'C:\Users\pawar shubham govind\Desktop\pratu.jpeg'


img=cv2.imread(path)

#show image using opencv
def showimage():
    #grey_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('original image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



#convert original image into  grey image using cvtColor of opdncv
grey_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

invert_img=cv2.bitwise_not(grey_img)

blur_img=cv2.GaussianBlur(invert_img, (111,111),0)

invblur_img=cv2.bitwise_not(blur_img)

sketch_img=cv2.divide(grey_img,invblur_img, scale=256.0)

cv2.imwrite('sketch.png', sketch_img)

def displaysketch():
    cv2.imshow('sketch image',sketch_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Call main function
if _name_ == '_main_':
    showimage()
    displaysketch()	


plt.figure(figsize=(14,8))
plt.subplot(1,2,1)
plt.title('Original image', size=18)
plt.imshow(img)
plt.axis('off')
plt.subplot(1,2,2)
plt.title('Sketch', size=18)
rgb_sketch=cv2.cvtColor(sketch_img, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_sketch)
plt.axis('off')
plt.show()
