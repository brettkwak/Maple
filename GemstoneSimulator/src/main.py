import cv2
from skimage.metrics import structural_similarity as ssim
import os

class_name = input("Class Name : ")
image1_name = input("Core Name : ")
image2_name = input("Skill Name : ")
mask_name = input("Mask Name : ")

def process_image(image_path, mask_path):
    image = cv2.imread(image_path)
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
    masked_image = cv2.bitwise_and(image, image, mask=mask)

    # Ensure binary mask
    # _, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)

    return cv2.cvtColor(masked_image, cv2.COLOR_BGR2GRAY)

def compare_core_with_skill(gray1, image2_path, mask_path):

    gray2 = process_image(image2_path, mask_path)

    ssim_score, _ = ssim(gray1, gray2, full=True)


    return ssim_score


def find_matching_skill(mask_number):
    folder_path = f"../data/Class/{class_name}"
    matching_skills = []
    mask_path = f'../data/mask{mask_number}.png'
    gray1 = process_image(image1_path, mask_path)

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".png"):
            skill_path = os.path.join(folder_path, filename)

            ssim_score = compare_core_with_skill(gray1, skill_path, mask_path)

            if ssim_score > 0.97:
                skill_name = os.path.splitext(filename)[0]
                matching_skills.append((skill_name, ssim_score))

    if matching_skills:
        print("\nMatching Skills ")
        for skill, score in matching_skills:
            print(f"{mask_number}번째 코어 : {skill}")
            print(f"SSIM Score : {score:.4f}")

    return matching_skills


# Usage
image1_path = '../data/' + image1_name + '.png'
image2_path = '../data/Class/' + class_name + "/" + image2_name + '.png'
mask_path = '../data/' + mask_name + '.png'
# results = compare_core_with_skill(image1_path, image2_path, mask_path)
# print(f"SSIM Score: {results['ssim_score']:.4f}")
for mask_num in range(1, 4):
    matching_skill = find_matching_skill(mask_num)

