# image-to-sketch
Image to sketch
This Project is for converting image into sketch.
Language used:- Python
version used:- 3.8.8
Library used: opencv for image recognization.
for installing open cv type **pip install opencv-python on terminal opencv will be install.**


What is difference in your approach and edge detectors?
ans:- Edge detection is an image processing technique for finding the boundaries of objects within images. It works by detecting discontinuities in brightness. Edge detection is used for image segmentation and data extraction in areas such as image processing, computer vision, and machine vision. In this method we convert first the convert original image is converted into gray image and then gray image is inverted using bitwised not function in opencv library and then invertd image is convert blur image using guasianblur method in opencv and then using blur image convert the sketch using divide method in opencv.

Why you chose not to use the edge detectors?
ans:- It cosumes lot of time due to complex computation
difficult to implement ot reach the real time response

What is sober/ canny edge detectors do?
ans:- The Canny Edge Detector is an edge detection operator that is used to detect a wide range of edges in images. It uses a multi-stage algorithm to do so..Canny edge detection is a technique to extract useful structural information from different vision objects . The Sobel edge detector is used in image processing and computer vision, particularly within edge detection algorithms where it creates an image emphasising edges.Canny Edge Operator handily produces an orientation at every point which can be very useful for the post-processing of the image.

What are sobel/ canny edge detectors and how they work?
ans:- The Sobel filter is used for edge detection. It works by calculating the gradient of image intensity at each pixel within the image. The result shows how abruptly or smoothly the image changes at each pixel, and therefore how likely it is that that pixel represents an edge.
Canny edge detection uses linear filtering with a Gaussian kernel to smooth noise and then computes the edge strength and direction for each pixel in the smoothed image. 
The Canny edge detector requires the user to input three parameters. The first is sigma, the standard deviation of the Gaussian filter specified in pixels. The second parameter low is the low threshold which is specified as a fraction of a computed high threshold. The third parameter high is the high threshold to use in the hysteresis and is specified as a percentage point in the distribution of gradient magnitude values for the candidate edge pixels.
