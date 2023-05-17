import cv2
import numpy as np
def white(image_path, output_path):
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED) 
    alpha = img[:, :, 3]
    white_image = np.full_like(img[:, :, :3], 255) 
    combined_image = cv2.merge([white_image, alpha])  
    cv2.imwrite(output_path, combined_image)


white("KSK.png", "result.png")