import cv2
from CheckCap import check_if_bottle_cap_missing
from CheckBottel import check_if_bottle_missing
from CheckUnderFilled import check_if_bottle_underfilled
from CheckLableMissing import check_if_label_missing
from CheckLabelNotPrinted import check_if_label_not_printed
from CheckLabelNotStright import check_if_label_not_straight
from CheckBottelShape import check_if_bottle_outOfShape
from CheckOverFilled import check_if_bottle_overfilled


def main():
    # Load image
    normal_image_path = "./Images/Normal/normal-image003.jpg"
    cap_image_path = "./Images/BottleCapMissing/capmissing-image090.jpg"
    underFilled_image_path = "./Images/BottleUnderfilled/underfilled-image032.jpg"
    label_missing_image_path = "./Images/LabelMissing/nolabel-image051.jpg"
    label_not_printed_image_path = "./Images/LabelNotStraight/nolabelprint-image071.jpg"
    BottleOverFilled_image_path = "./Images/BottleOverFilled/overfilled-image040.jpg"
    label_not_stright_image_path = (
        "./Images/LabelNotStraight/labelnotstraight-image074.jpg"
    )
    bottel_out_of_shape_image_path = (
        "./Images/BottleDeformed/deformedbottle-image013.jpg"
    )
    image = cv2.imread(label_missing_image_path)

    # Check if the cap is missing
    results = {
        "bottle_missing": None,
        "bottle_cap_missing": None,
        "bottle_underFilled": None,
        "label_missing": None,
        "label_not_printed:": None,
        "is_label_stright": None,
        "bottel_out_of_shape": None,
        "bottel_over_filled": None,
    }
    bottle_missing = check_if_bottle_missing(image)
    results["bottle_missing"] = bottle_missing
    if not bottle_missing:
        bottle_cap_missing = check_if_bottle_cap_missing(image)
        results["bottle_cap_missing"] = bottle_cap_missing
        bottle_underFilled = check_if_bottle_underfilled(image)
        results["bottle_underFilled"] = bottle_underFilled
        label_missing = check_if_label_missing(image)
        results["label_missing"] = label_missing

        if not label_missing:
            label_not_printed = check_if_label_not_printed(image)
            results["label_not_printed"] = label_not_printed
            if not label_not_printed:
                is_label_stright = check_if_label_not_straight(image)
                results["is_label_stright"] = is_label_stright
                bottel_out_of_shape = check_if_bottle_outOfShape(image)
                results["bottel_out_of_shape"] = bottel_out_of_shape
        bottel_over_filled = check_if_bottle_overfilled(image)
        results["bottel_over_filled"] = bottel_over_filled
        # If any of these faults happen, the bottle is not out of shape
        if bottle_underFilled or label_missing or label_not_printed or is_label_stright:
            bottel_out_of_shape = False
            results["bottel_out_of_shape"] = bottel_out_of_shape
        if bottel_out_of_shape:
            # If bottle is deformed, the bottle should not be detected as
            # overfilled
            bottel_over_filled = False
            results["bottel_over_filled"] = bottel_over_filled

    for index, (key, value) in enumerate(results.items()):
        print(f"{index + 1}:  {key} : {value}")


if __name__ == "__main__":
    main()
