import cv2
from pathlib import Path

def get_file_name(filename):
    return filename.stem[0]

def process_image(image_path, mask_path):
    image = cv2.imread(str(image_path))
    mask = cv2.imread(str(mask_path), cv2.IMREAD_GRAYSCALE)
    return cv2.bitwise_and(image, image, mask=mask)


class_name = input("Class Name : ")
class_path = f"../data/Class/{class_name}"
# Get all PNG files in the directory
for img_path in sorted(Path(class_path).glob('*.png')):

    filename_without_ext = img_path.stem
    for i in range(1, 4):
        mask_path = f"../data/Mask/mask{i}.png"
        sliced_image = process_image(img_path, mask_path)
        new_filename = f"{filename_without_ext}_{i}.png"
        cv2.imwrite(f"{class_path}/Slice/{new_filename}", sliced_image)
        print(f"Saved: {new_filename}")

    img = None
    cv2.destroyAllWindows()
