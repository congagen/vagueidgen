import PIL
import json
import datetime
import random


def get_datetime():
    now = datetime.datetime.now()
    date = str(now.year) + '-' + str(now.month) + '-' + str(now.day)
    clock = str(now.hour) + '.' + str(now.minute) + '.' + str(now.second)

    return str(date + '_' + clock)


def json_to_dict(json_request):
    j_dict = {}

    with open(json_request) as json_data:
        j_dict = json.load(json_data)

    return j_dict


def save_img_array(img_array, save_path, size_w, size_h, append_date):
    image_out = PIL.Image.new("RGBA", (size_w, size_h), 0)
    image_out.putdata(img_array)

    image_out.save(save_path)


def save_pil_image(pil_image, folderpath, filename, extension, append_date):
    date_comp = get_datetime()
    rnd = random.randint(0, 999999)

    f_path = folderpath + str(rnd) + "_" + filename

    if append_date:
        save_path = f_path + str(date_comp) + extension
        pil_image.save(save_path)
    else:
        save_path = f_path + extension
        pil_image.save(save_path)
