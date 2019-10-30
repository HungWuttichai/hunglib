import cv2
from datetime import datetime
font = cv2.FONT_HERSHEY_DUPLEX


def timestamp(image):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cv2.putText(image, now, (0, 25), font, 1.0, (255, 255, 255), 1)
    return image
