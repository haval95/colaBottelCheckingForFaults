import cv2
import numpy as np
from ROI import extract_roi


def check_if_bottle_underfilled(image):
    # Convert to greyscale
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Extract the ROI just under the ideal liquid level in the bottle
    roi = extract_roi(image_gray, 130, 140, 170, 220)

    if roi is None:
        return False  # Return False if ROI extraction failed

    # Convert to a binary image using a greyscale threshold of '150'
    _, roi_binary = cv2.threshold(roi, 150, 255, cv2.THRESH_BINARY)

    # Calculate the percentage of black pixels in the binary image
    black_percentage = 100 * np.sum(roi_binary == 0) / np.prod(roi_binary.shape)

    # Underfilled bottle detected if % black pixels is less than 25%
    result = black_percentage < 25
    return result
