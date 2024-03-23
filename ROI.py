def extract_roi(image_in, y1, x1, y2, x2):
    # Check if any of the points are '0'
    if x1 == 0 or x2 == 0 or y1 == 0 or y2 == 0:
        print("[ERROR]: Oops, you forgot Python indices start at 0!")
        return None

    # Get image dimensions
    h, w = image_in.shape

    if x1 > w or x2 > w or y1 > h or y2 > h:
        print(f"[ERROR]: Image dimensions ({h}, {w}) exceeded!")
        return None

    image_out = image_in[y1:y2, x1:x2]
    return image_out
