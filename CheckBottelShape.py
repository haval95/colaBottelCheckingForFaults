import cv2
from ROI import extract_roi


def check_if_bottle_deformed(image):

    image_r = image[:, :, 2]

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    image_r = clahe.apply(image_r)

    return image_r


def binarize_image(image, threshold):
    _, binary_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
    return binary_image


def find_bounding_boxes(mask):
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(mask)

    bounding_boxes = [stats[i][:4] for i in range(1, num_labels)]

    return bounding_boxes


def check_limits(area, width, height):
    area_result = (area >= 6000) and (area <= 7900)
    width_result = (width >= 80) and (width <= 100)
    height_result = (height >= 75) and (height <= 92)

    return area_result, width_result, height_result


def check_if_bottle_outOfShape(image):

    image_r = check_if_bottle_deformed(image)

    roi_r = extract_roi(image_r, 190, 100, 280, 260)

    mask_r = binarize_image(roi_r, 200)

    bounding_boxes = find_bounding_boxes(mask_r)

    max_area, max_area_w, max_area_h = 0, 0, 0
    for bb in bounding_boxes:
        area = bb[2] * bb[3]
        if area > max_area:
            max_area = area
            max_area_w = bb[2]
            max_area_h = bb[3]

    area_result, width_result, height_result = check_limits(
        max_area, max_area_w, max_area_h
    )
    result = area_result and width_result and height_result

    return result
