import cv2
import numpy as np
from ROI import extract_roi


def check_if_bottle_underfilled(image):
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    roi = extract_roi(image_gray, 130, 140, 170, 220)

    if roi is None:
        return False
    _, roi_binary = cv2.threshold(roi, 150, 255, cv2.THRESH_BINARY)
    black_percentage = 100 * np.sum(roi_binary == 0) / np.prod(roi_binary.shape)

    result = black_percentage < 25
    return result
