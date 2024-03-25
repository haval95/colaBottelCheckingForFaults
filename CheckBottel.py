import cv2
import numpy as np
from ROI import extract_roi


def check_if_bottle_missing(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    roi = extract_roi(image, 1, 135, 250, 225)

    if roi is None:
        return False

    _, roi_binary = cv2.threshold(roi, 150, 255, cv2.THRESH_BINARY)

    # Calculate the percentage of black pixels
    black_percentage = 100 * np.sum(roi_binary == 0) / np.prod(roi_binary.shape)

    result = black_percentage < 10
    return result
