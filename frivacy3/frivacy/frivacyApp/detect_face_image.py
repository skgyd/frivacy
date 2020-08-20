import cv2
import numpy as np

def detecting(title):
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('C:/Users/yooso/Desktop/frivacy/frivacy3/frivacy/frivacyApp/haarcascade_frontalface_default.xml')

    # Read the input image
    title = 'C:/Users/yooso/Desktop/frivacy/frivacy3/frivacy/frivacyApp/static/' + title
    print(title)
    img = cv2.imread(title)

    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    return faces


# Draw rectangle around the faces
# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the output
# cv2.imshow('img', img)
# cv2.waitKey()
