import cv2
import numpy as np


def check_if_bottle_cap_missing(image):
    # Convert to greyscale
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height, width = image_gray.shape
    crop_width = 70
    start_x = (width - crop_width) // 2
    end_x = start_x + crop_width
    start_y = 5
    end_y = height // 5  # Calculate the end y-coordinate correctly
    # Extract the ROI for the bottle cap
    roi = image_gray[start_y:end_y, start_x:end_x]

    # Convert to a binary image using a greyscale threshold of '150'
    _, roi_binary = cv2.threshold(roi, 150, 255, cv2.THRESH_BINARY)

    # Calculate the percentage of black pixels in the binary image
    black_percentage = 100 * np.sum(roi_binary == 0) / np.prod(roi_binary.shape)

    # Fault detected if % black pixels is less than 25%
    bottle_cap_missing = black_percentage < 25

    # Draw rectangle around the region of interest
    cv2.rectangle(image, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)

    # Define the text to display based on whether the bottle cap is missing
    text = "Missing" if bottle_cap_missing else "Not Missing"

    # Put text inside the rectangle
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.5
    font_thickness = 1
    text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
    text_x = (start_x + end_x - text_size[0]) // 2
    text_y = (start_y + end_y + text_size[1]) // 2
    cv2.putText(
        image, text, (text_x, text_y), font, font_scale, (0, 0, 0), font_thickness
    )
    # Define the path to save the image
    output_folder = "./result/"
    output_filename = "capResult.jpg"
    output_path = output_folder + output_filename

    # Save the modified image
    cv2.imwrite(output_path, image)

    return bottle_cap_missing
