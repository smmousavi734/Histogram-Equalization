import cv2
import numpy as np
from matplotlib import pyplot as plt

def plotting(img1,img2):
    plt.subplot(321)
    plt.title("Original Image")
    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))

    plt.subplot(312)
    plt.title("Histogram for Original picture")
    plt.hist(img1.flatten(),256,[0,256])

    plt.subplot(322)
    plt.title("Normalized Picture")
    plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))

    plt.subplot(313)
    plt.title("Histogram for Equalized Picture")
    plt.hist(img2.flatten(),256,[0,256])

    plt.show()
def plotting2(img1,img2):
    plt.subplot(121)
    plt.title("Original Image")
    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))

    plt.subplot(122)
    plt.title("Equalized Picture")
    plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))

    plt.show()

img = cv2.imread('2222.jpg',0)

hist,bins = np.histogram(img.flatten(),256,[0,256]) #Calculating Histogram of an image

cdf = hist.cumsum()#Calculate the Cumilative Distribution Function via cumsum()
                   #which compute the cumulative sum of hist array 

cdf_m = np.ma.masked_equal(cdf,0) #ommitting zeors from cdf with help of Masked Arrays 
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min()) #Equalization
cdf2 = np.ma.filled(cdf_m,0).astype('uint8') #Fill back the zeros omitted
img2 = cdf2[img]


hist2,bins = np.histogram(img2.flatten(),256,[0,256])
cdf2 = hist2.cumsum()

plotting(img,img2)
#plotting2(img,img2)
cv2.waitKey(0)