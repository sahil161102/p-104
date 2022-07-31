import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,  
           "Sun",
           (80, 100),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=2,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Mercury",
           (120, 250),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Venus",
           (200, 260),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Earth",
           (280, 260),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Mars",
           (390, 250),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Jupiter",
           (520, 400),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=2,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Sarturn",
           (720, 350),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=2,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Uranus",
           (950, 300),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Neptune",
           (1100, 300),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(255,255,255)
           )
cv2.imshow("Solar-System",img)
cv2.waitKey(0)