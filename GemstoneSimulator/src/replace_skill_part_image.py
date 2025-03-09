import cv2

skill_name = input('Skill Name : ')
mask_part = input('Part to be replaced : ')

# Load the images and mask
image1 = cv2.imread(f'../data/Class/{skill_name}_Base.png')
image2 = cv2.imread(f'../data/Class/{skill_name}_Part.png')
mask = cv2.imread(f'../data/Mask/mask{mask_part}.png', cv2.IMREAD_GRAYSCALE)

# Process
_, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
masked_image = cv2.bitwise_and(image2, image2, mask=mask)
result = image1.copy()
result[mask > 0] = masked_image[mask > 0]

# Display results
# cv2.imshow('Base Image', image1)
# cv2.imshow('Part Image', image2)
# cv2.imshow('Mask', mask)
# cv2.imshow('Masked Image', masked_image)
# cv2.imshow('Result', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Save the result
cv2.imwrite(f'../data/Class/{skill_name}.png', result)
