import cv2
from CheckCap import check_if_bottle_cap_missing
from CheckBottel import check_if_bottle_missing
from CheckUnderFilled import check_if_bottle_underfilled
from CheckLableMissing import check_if_label_missing
from CheckLabelNotPrinted import check_if_label_not_printed


def main():
    # Load image
    normal_image_path = "./Images/Normal/normal-image001.jpg"
    cap_image_path = "./Images/BottleCapMissing/capmissing-image080.jpg"
    underFilled_image_path = "./Images/BottleUnderfilled/underfilled-image032.jpg"
    label_missing_image_path = "./Images/LabelMissing/nolabel-image051.jpg"
    label_not_printed_image_path = "./Images/LabelNotPrinted/nolabelprint-image060.jpg"
    image = cv2.imread(label_not_printed_image_path)

    # Check if the cap is missing
    results = {
        "bottle_missing": False,
        "bottle_cap_missing": False,
        "bottle_underFilled": False,
        "label_missing": False,
        "label_not_printed:": False,
    }
    bottle_missing = check_if_bottle_missing(image)
    if bottle_missing:
        results["bottle_missing"] = bottle_missing
    else:
        bottle_cap_missing = check_if_bottle_cap_missing(image)
        bottle_underFilled = check_if_bottle_underfilled(image)
        label_missing = check_if_label_missing(image)
        if bottle_cap_missing:
            results["bottle_cap_missing"] = bottle_cap_missing
        if bottle_underFilled:
            results["bottle_underFilled"] = bottle_underFilled
        if label_missing:
            results["label_missing"] = label_missing
        else:
            label_not_printed = check_if_label_not_printed(image)
            if label_not_printed:
                results["label_not_printed"] = label_not_printed

    for index, (key, value) in enumerate(results.items()):
        print(f"{index + 1}:  {key} : {value}")


if __name__ == "__main__":
    main()
