import cv2
from CheckCap import check_if_bottle_cap_missing
from CheckBottel import check_if_bottle_missing
from CheckUnderFilled import check_if_bottle_underfilled
from CheckLableMissing import check_if_label_missing


def main():
    # Load image
    normal_image_path = "./Images/Normal/normal-image001.jpg"
    cap_image_path = "./Images/BottleCapMissing/capmissing-image080.jpg"
    underFilled_image_path = "./Images/BottleUnderfilled/underfilled-image032.jpg"
    label_missing_image_path = "./Images/LabelMissing/nolabel-image051.jpg"
    image = cv2.imread(label_missing_image_path)

    # Check if the cap is missing
    results = {
        "Bottel": "Not Missing",
        "BottelCap": "Missing",
        "BottelUnderFilled": "No",
        "LableMissing": "No",
    }
    bottle_missing = check_if_bottle_missing(image)
    if bottle_missing:
        results["Bottel"] = "Missing"
    else:
        bottle_cap_missing = check_if_bottle_cap_missing(image)
        bottle_underFilled = check_if_bottle_underfilled(image)
        label_missing = check_if_label_missing(image)
        if bottle_cap_missing:
            results["BottelCap"] = "Missing"
        if bottle_underFilled:
            results["BottelUnderFilled"] = "Yes"
        if label_missing:
            results["LableMissing"] = "Yes"

    for index, (key, value) in enumerate(results.items()):
        print(f"{index + 1}:  {key} is {value}")


if __name__ == "__main__":
    main()
