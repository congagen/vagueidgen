import sys
import PIL
import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFilter
from PIL import ImageOps


def mirror_image(input_iamge, image_size):
    flipped = PIL.ImageOps.mirror(input_iamge)
    c_area = (int(image_size * 0.5), 0, image_size, image_size)
    cropped = flipped.crop(c_area)
    input_iamge.paste(cropped, c_area)

    return input_iamge


def circle_mask(input_image, margin, blur_amount):
    mask_imgae_size = input_image.size

    x_margin = margin
    y_margin = 1 - margin

    mask_margins = [int(mask_imgae_size[0] * x_margin),
                    int(mask_imgae_size[0] * x_margin),
                    int(mask_imgae_size[1] * y_margin),
                    int(mask_imgae_size[1] * y_margin)]

    m_image = Image.new('L', mask_imgae_size, color=255)
    draw = PIL.ImageDraw.Draw(m_image)
    draw.ellipse(mask_margins, fill=0)
    mask = m_image.filter(PIL.ImageFilter.GaussianBlur(radius = blur_amount))
    input_image.paste(mask, (0, 0), mask)

    return input_image


def alpha_color(image_data, new_rgb):
    raw_image_data = []
    size = image_data.size

    img_raw_nparray = np.asarray(image_data.convert("RGBA"))

    for row in range(len(img_raw_nparray)):
        for pix in range(len(img_raw_nparray[row])):
            r = int(img_raw_nparray[row][pix][0])
            g = int(img_raw_nparray[row][pix][1])
            b = int(img_raw_nparray[row][pix][2])
            avg = int(abs(r + g + b) * (1 / 3))

            new_pixel = (new_rgb[0],
                         new_rgb[1],
                         new_rgb[2],
                         avg)

            raw_image_data.append(new_pixel)

    pil_image = PIL.Image.new("RGBA", size, 0)
    pil_image.putdata(raw_image_data)

    return pil_image, raw_image_data