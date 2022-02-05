import cv2 as cv

img = cv.imread('images/park.jpg')
cv.imshow("Park",img)

# kernel = window
# kernel size = nbr columns and rows
# blur is applied on the middle pixel as a result of the surronding pixels

# Average Blur : middle pixel intensity = avg surrounding pixel intensity
average = cv.blur(img,(7,7))
cv.imshow("Average Blur",average)

# Gaussian Blur : less blurring, more natural, add weights to surrounding pixels
gauss = cv.GaussianBlur(img,(7,7),0)
cv.imshow("Gaussian Blur",gauss)

# Median Blur : reduce amount of noise, middle pixel intensity = median surrounding pixel intensity
median = cv.medianBlur(img,3)
cv.imshow("Median Blur",median)

# Bilateral Blur : most effective , retains the edges in the img
bilateral = cv.bilateralFilter(img,10,35,25) # sigmaspace : how further pixels influence calculation of middle pixel 
cv.imshow("Bilateral Blur",bilateral)


cv.waitKey(0)