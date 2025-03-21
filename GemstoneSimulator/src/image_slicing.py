from skimage.metrics import structural_similarity as ssim
import cv2
import os
from pathlib import Path
import json


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


# Load & Slice class's skills
def load_skill_slices(class_name):
    skill_slices = {f'part{i + 1}': [] for i in range(3)}
    skill_dir = Path(f'../data/Class/{class_name}')

    print(f"Loading skills from {skill_dir}")

    for img_path in skill_dir.glob("*.png"):
        skill_name = img_path.stem
        print(f'Processing {skill_name}')

        for part_index in range(3):
            mask_path = f'../data/Mask/mask{part_index + 1}.png'

            processed_slice = process_image(img_path, mask_path)

            skill_slices[f'part{part_index + 1}'].append({
                'name': skill_name,
                'slice': processed_slice,
            })

    return skill_slices


# Compare two images and return a similarity scrore
def compare_images(img1, img2):
    """Compare two images using SSIM and return similarity score."""
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    score, _ = ssim(gray1, gray2, full=True)
    return score


# Match core part with skill part, and find out which skill it is
def match_core_with_skills(core_image_path, skill_slices):
    skills = [None, None, None]

    for part_index in range(3):
        mask_path = f'../data/Mask/mask{part_index + 1}.png'
        core_slice = process_image(core_image_path, mask_path)

        best_match = None
        best_score = 0

        for skill in skill_slices[f'part{part_index + 1}']:
            score = compare_images(core_slice, skill['slice'])
            if score > 0.98 and score > best_score:
                best_match = skill['name']
                best_score = score

        skills[part_index] = best_match

    return skills


# Process all cores into map format
def process_all_cores(core_number, class_name):
    skill_slices = load_skill_slices(class_name)
    core_skills_map = {}

    for core_num in range(1, core_number + 1):
        core_path = Path(f'../data/Extract/match_{core_num}.png')

        if core_path.exists():
            print(f"Processing Core {core_num}...")
            skills = match_core_with_skills(core_path, skill_slices)

            # Only add if all three skills were matched
            if all(skills):
                core_skills_map[core_num] = skills
                print(f"Core {core_num}: {', '.join(skills)}")
            else:
                print(f"Core {core_num}: Could not match all skills - {skills}")

    return core_skills_map


# Save core-skill map as file
def save_core_skills_map(core_skills_map):

    output_file_path = Path(f'../data/core_skill_mapping.txt')

    # Save as txt
    with open(output_file_path, 'w') as f:
        for core_num, skills in core_skills_map.items():
            f.write(f"Core {core_num}, {skills[0]}, {skills[1]}, {skills[2]}\n")

    print(f"Core-skills mapping saved to {output_file_path}")

    # Save as JSON
    json_file = output_file_path.with_suffix('.json')
    with open(json_file, 'w') as f:
        json.dump(core_skills_map, f, indent=2)

    print(f"Core-skills mapping saved as JSON to {json_file}")





def main(class_name=None, core_number=None):

    if class_name is None:
        class_name = input("Class Name : ")
    if core_number is None:
        core_number = int(input("Number of cores : "))

    # Initialize paths
    core_path = '../data/Extract'
    mask_path = "../data/Mask"

    load_skill_slices(class_name)
    core_skill_mapping = process_all_cores(core_number, class_name)
    save_core_skills_map(core_skill_mapping)
    print("Loading Done")

    return None


if __name__ == "__main__":
    main()
