import cv2
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import os

class_name = input("Class Name : ")
image1_name = input("Core Name : ")
image2_name = input("Skill Name : ")
mask_name = input("Mask Name : ")
show_plot = input("Show Plot? (Yes/No) : ")

def compare_core_with_skill(image1_path, image2_path, mask_path):
    # Read images and mask
    img1 = cv2.imread(image1_path)
    img2 = cv2.imread(image2_path)
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

    # Ensure binary mask
    # _, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)

    # Apply same mask to both images
    img1_masked = cv2.bitwise_and(img1, img1, mask=mask)
    img2_masked = cv2.bitwise_and(img2, img2, mask=mask)

    # Calculate similarity using SSIM
    gray1 = cv2.cvtColor(img1_masked, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2_masked, cv2.COLOR_BGR2GRAY)
    ssim_score, _ = ssim(gray1, gray2, full=True)

    # Show results
    if show_plot == "Yes":
        plt.figure(figsize=(12, 5))
        plt.subplot(151)
        plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
        plt.title('Image 1')

        plt.subplot(152)
        plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
        plt.title('Image 2')

        plt.subplot(153)
        plt.imshow(mask, cmap='gray')
        plt.title('Mask')

        plt.subplot(154)
        plt.imshow(cv2.cvtColor(img1_masked, cv2.COLOR_BGR2RGB))
        plt.title('Masked Image 1')

        plt.subplot(155)
        plt.imshow(cv2.cvtColor(img2_masked, cv2.COLOR_BGR2RGB))
        plt.title('Masked Image 2')

        plt.show()

    return {
        'ssim_score': ssim_score,
    }


def find_matching_skill():
    folder_path = f"../data/Class/{class_name}"
    matching_skills = []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".png"):
            skill_path = os.path.join(folder_path, filename)

            results = compare_core_with_skill(image1_path, skill_path, mask_path)

            if results['ssim_score'] > 0.97:
                skill_name = os.path.splitext(filename)[0]
                matching_skills.append((skill_name, results['ssim_score']))

    if matching_skills:
        print("\nMatching Skills ")
        for skill, score in matching_skills:
            print(f"{skill}: {score:.4f}")

    return matching_skills


# Usage
image1_path = '../data/' + image1_name + '.png'
image2_path = '../data/Class/' + class_name + "/" + image2_name + '.png'
mask_path = '../data/' + mask_name + '.png'
results = compare_core_with_skill(image1_path, image2_path, mask_path)
print(f"SSIM Score: {results['ssim_score']:.4f}")
matching_skill = find_matching_skill()

