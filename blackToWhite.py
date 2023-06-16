import cv2
import numpy as np

def black_to_white(src_path, dst_path):
    img = cv2.imread(src_path, cv2.IMREAD_UNCHANGED)
    alpha = img[:, :, 3]   # alpha channel
    img_rgb = img[:, :, :3]
    
    img_rgb[(img_rgb <= [50,50,50]).all(axis=2)] = [255,255,255]

    result_with_alpha = np.concatenate([img_rgb, alpha[..., None]], axis=2)
    result_with_alpha[alpha == 0] = [0, 0, 0, 0]

    cv2.imwrite(dst_path, result_with_alpha)

black_to_white("Pmeta.png", "result.png")
