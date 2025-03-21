import cv2
import numpy as np


def get_search_area(image_width, image_hegiht):
    # Crop search area depending on image size
    # x, y, width, height
    if image_width == 800 and image_hegiht == 600:
        return (70, 0, 450, 600)
    elif image_width == 1024 and image_hegiht == 768:
        return (170, 50, 450, 600)
    elif image_width == 1280 and image_hegiht == 720:
        return (310, 30, 450, 600)
    elif image_width == 1366 and image_hegiht == 768:
        return (350, 50, 450, 600)
    elif image_width == 1920 and image_hegiht == 1080:
        return (630, 210, 450, 600)
    else:
        print("Check Image Size!")

def extract_core(large_img, image_number, previous_count=0):

    # Mask path
    mask_path = f"../data/inner_tight.png"

    # Read images with alpha channel (Transparent)
    template = cv2.imread(mask_path, cv2.IMREAD_UNCHANGED)
    full_image = cv2.imread(large_img)
    img_height, img_width = full_image.shape[:2]
    x, y, w, h = get_search_area(img_width, img_height)
    image = full_image[y:y+h, x:x+w].copy()
    cv2.imwrite('../data/Extract/cropped_area.png', image)

    # Ensure template has alpha channel
    if template.shape[2] != 4:
        raise ValueError("Template image must have transparency (alpha channel)")

    # Split the template into color and alpha channels
    template_bgr = template[:, :, :3]
    alpha = template[:, :, 3]

    # Create mask from alpha channel
    mask = alpha > 0

    # Get dimensions
    h, w = template.shape[:2]

    # Counter for matches
    match_count = previous_count

    # Template matching with mask
    result = cv2.matchTemplate(
        image,
        template_bgr,
        cv2.TM_CCOEFF_NORMED,
        mask=mask.astype(np.uint8)
    )

    # Threshold
    threshold = 0.8

    # Find locations where matching exceeds threshold
    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))

    # Process each match
    for pt in locations:
        # Check if points are far enough from previous matches
        valid_match = True
        for prev_pt in locations[:locations.index(pt)]:
            if np.sqrt((pt[0] - prev_pt[0]) ** 2 + (pt[1] - prev_pt[1]) ** 2) < w / 2:
                valid_match = False
                break

        if valid_match:
            match_count += 1

            # Draw rectangle around match
            cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)

            # Adjust text position slightly above the match
            text_x = pt[0]
            text_y = pt[1] - 5  # 5 pixels above the match

            # Write match number on top of the rectangle
            text = str(match_count)
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 0.7
            font_thickness = 2

            # Get text size
            (text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, font_thickness)

            # Draw red number
            cv2.putText(image,
                        text,
                        (text_x, text_y),
                        font,
                        font_scale,
                        (0, 0, 255),  # Red color (BGR)
                        font_thickness)

            # Crop and save matched region
            cropped = image[pt[1]:pt[1] + h, pt[0]:pt[0] + w]
            cv2.imwrite(f'../data/Extract/match_{match_count}.png', cropped)

    # Write total counter on top of image
    text = f'Total Matches: {match_count}'
    cv2.putText(image, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 255), 2)

    # Save final image with annotations
    cv2.imwrite(f'../data/Extract/result{image_number}.png', image)

    return match_count


def main(page_count = None):

    if page_count is None:
        page_count = int(input("Number of pages: "))

    total_matches = 0
    for i in range(1, page_count + 1):
        large_image_path = f"../data/ab_{i}.png"
        print(f"Extracting core from page{i}.png...")
        total_matches = extract_core(large_image_path, i, total_matches)
        print(f"Total matches found: {total_matches}")
    return total_matches


if __name__ == "__main__":
    main()
