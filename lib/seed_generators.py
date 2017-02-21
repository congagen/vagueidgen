import random
import numpy as np

from lib import image_filters

import PIL
from PIL import ImageDraw
from PIL import ImageOps


def generate_noise_seed(seed_size):
    s_img_raw = []

    for row in range(seed_size):
        for pix in range(seed_size):
            clr = 255 if (random.randint(0, 1) > 0) else 0
            print("1") if clr == 255 else print("0")
            pixel = (clr, clr, clr, 255)
            s_img_raw.append(pixel)

    return np.asarray(s_img_raw)


def scaled_noise(init_size, image_size, noise_gamma, mask_blur, r_seed):
    final_size = int(image_size)

    mask_blur_r = int(final_size * mask_blur)
    noise_seed = np.random.rand(init_size, init_size, 3) * noise_gamma

    raw_noise = PIL.Image.fromarray(noise_seed.astype('uint8')).convert('L')

    flipped = image_filters.mirror_image(raw_noise, init_size)
    scaled_noise = flipped.resize((final_size, final_size), PIL.Image.ANTIALIAS)

    masked = image_filters.circle_mask(scaled_noise, 0.3, mask_blur_r)
    inverted_image = ImageOps.invert(masked)

    return inverted_image, np.asarray(inverted_image)