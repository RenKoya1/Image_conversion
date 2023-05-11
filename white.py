import cv2

def color_to_white(image_path, output_path):
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED) 
    alpha = img[:, :, 3]
    img_rgb = img[:, :, :3]

    gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    _, binary_image = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)

    combined_image = cv2.merge([binary_image, binary_image, binary_image, alpha])

    cv2.imwrite(output_path, combined_image)

