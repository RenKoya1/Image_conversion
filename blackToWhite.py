import cv2
import numpy as np

def change_background(src_path, dst_path):
    img = cv2.imread(src_path, cv2.IMREAD_UNCHANGED) 
    alpha = img[:, :, 3]   # alpha channel
    img_rgb = img[:, :, :3]
    gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 2, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    img_rgb[binary == 255] = 255

    result_with_alpha = np.concatenate([img_rgb, alpha[..., None]], axis=2)
    result_with_alpha[alpha == 0] = [0, 0, 0, 0]

    cv2.imwrite(dst_path, result_with_alpha)

change_background("JGG copy.png", "result.png")
