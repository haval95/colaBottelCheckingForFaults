import cv2
from ROI import extract_roi


def check_if_bottle_overfilled(image):
    # Convert to grayscale
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Extract the ROI just over the ideal liquid level in the bottle
    roi = extract_roi(image_gray, 110, 140, 140, 220)

    # Convert to a binary image using a grayscale threshold of '150'
    _, roi_binary = cv2.threshold(roi, 150, 255, cv2.THRESH_BINARY)

    # Calculate the percentage of black pixels in the binary image
    black_percentage = 100 * (
        cv2.countNonZero(roi_binary) / (roi_binary.shape[0] * roi_binary.shape[1])
    )

    result = black_percentage < 40

    return result
