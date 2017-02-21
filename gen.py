import sys
import PIL
from PIL import Image
from lib import data_mgmt
from lib import image_generators


def image_order(order_dct, i):
    img = image_generators.obscuface(order_dct, i)

    background_color = (
        order_dct["background_color"][0],
        order_dct["background_color"][1],
        order_dct["background_color"][2],
        order_dct["background_alpha"]
    )

    image_size = (order_dct["size_x"], order_dct["size_x"])

    if order_dct["background_alpha"] == 0:
        new_image = PIL.Image.new("RGBA", image_size, background_color)
        new_image.paste(img, (0, 0), img)
    else:
        new_image = PIL.Image.new("RGB", image_size, background_color)
        new_image.paste(img, mask=img.split()[3])


    if order_dct["preview"]:
        new_image.show()

    if order_dct["save_image"]:
        data_mgmt.save_pil_image(
            new_image,
            order_dct["save_path"],
            order_dct["filename"],
            order_dct["extension"],
            order_dct["append_date"]
    )


def process_order(order):
    order_dct = data_mgmt.json_to_dict(order[1])

    for i in range(order_dct["item_count"]):
        image_order(order_dct, i)


process_order(sys.argv)
#process_order(["", "order.json", "some_string"])