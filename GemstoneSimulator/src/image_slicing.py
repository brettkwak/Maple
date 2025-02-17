from skimage.metrics import structural_similarity as ssim
import cv2
import os
from pathlib import Path


def process_image(image_path, mask_path):
    image = cv2.imread(str(image_path))
    mask = cv2.imread(str(mask_path), cv2.IMREAD_GRAYSCALE)
    return cv2.bitwise_and(image, image, mask=mask)


def get_number_from_filename(filename):
    # Extract number from "match_X.png" format
    return int(filename.stem.split('_')[1])


def load_core_images(skill_path, mask_path):
    core_slices = {
        'part1': [], 'part2': [], 'part3': []
    }

    # Load and process all reference images
    for img_path in sorted(Path(skill_path).glob('match_*.png')):
        index = get_number_from_filename(img_path)

        # Process each part with corresponding mask
        for part_index in range(3):
            current_mask_path = os.path.join(mask_path, f'mask{part_index + 1}.png')
            processed_slice = process_image(img_path, current_mask_path)

            core_slices[f'part{part_index + 1}'].append({
                'index': index,
                'slice': processed_slice
            })

            # Save slices
            cv2.imwrite(f'../data/Extract/Slice/{index}_{part_index+1}.png', processed_slice)

    return core_slices


# Initialize paths
core_path = '../data/Extract'
mask_path = "../data/Mask"

# Load reference images once
core_slices = load_core_images(core_path, mask_path)
print("Loading Done")


