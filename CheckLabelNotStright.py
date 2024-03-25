import cv2
import numpy as np
from ROI import extract_roi


def check_if_label_not_straight(image):
    # Convert to greyscale
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_adjusted = cv2.equalizeHist(image_gray)

    # Extract the ROI for the top of the bottle label
    roi_horizontal = extract_roi(image_adjusted, 170, 110, 195, 250)

    # Carry out edge detection on the ROI
    edges = cv2.Canny(roi_horizontal, 0, 255)

    # Find contours in the edge-detected image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize variables for maximum width and height of bounding boxes
    max_width = 0
    max_height = 0

    # Loop over all contours discovered
    for contour in contours:
        # Get bounding box of contour
        x, y, w, h = cv2.boundingRect(contour)

        # Update maximum width and height
        max_width = max(max_width, w)
        max_height = max(max_height, h)

    # Draw rectangle around the area used for checking straightness
    image_with_rectangles = image.copy()  # Create a copy of the original image
    cv2.rectangle(
        image_with_rectangles, (110, 170), (250, 195), (0, 255, 0), 2
    )  # Adjust coordinates as needed

    # Extract the ROI for the top half of the label
    roi_label = extract_roi(image_adjusted, 180, 110, 230, 250)

    # Convert ROI to binary using a greyscale threshold of '50'
    _, roi_label_binary = cv2.threshold(roi_label, 50, 255, cv2.THRESH_BINARY)

    # Calculate the percentage of black pixels in the ROI
    black_percentage = (
        100 * np.sum(roi_label_binary == 0) / np.prod(roi_label_binary.shape)
    )

    # Condition 01: Check if the (white) horizontal line (at the top of the label) is within limits
    horizontal_result = max_width <= 100 or max_height >= 10

    # Condition 02: Check the percentage of black pixels on the label
    black_percentage_result = black_percentage <= 21

    # Combine both conditions

    is_stright = horizontal_result and black_percentage_result

    return is_stright
