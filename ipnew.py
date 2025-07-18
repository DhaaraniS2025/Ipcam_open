import cv2
import requests
import numpy as np
import imutils

url = "http://192.168.1.25:8080/shot.jpg"

while True:
    img_resp= requests.get(url)
    img_arr= np.array(bytearray(img_resp.content), dtype=np.uint8)
    image= cv2.imdecode(img_arr, -1)
    image= imutils.resize(image,width=1000,height=800)
    cv2.imshow("IPcam",image)

    if cv2.waitKey(1)==27:
        break

cv2.destroyAllWindows
