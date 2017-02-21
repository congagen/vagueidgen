from lib import seed_generators
from lib import image_filters


def obscuface(order_dct, img_num):

    singe_layer_opacity = int(255 * (1 / order_dct["iterations"]))
    seed_size = order_dct["seed_size"]

    face_center_x = int(order_dct["size_x"] * 0.5)
    face_center_y = int(order_dct["size_y"] * 0.5)

    eye_size = int(order_dct["size_x"] * order_dct["feature_detail_ratio"])
    nose_size = int(order_dct["size_x"] * order_dct["feature_detail_ratio"])
    mouth_size = int(order_dct["size_x"] * (order_dct["feature_detail_ratio"] * 1.1))

    eye_center = face_center_x - int(eye_size * 0.5)
    nose_center = face_center_y - int(nose_size * 0.5)
    mouth_center = face_center_y - int(mouth_size * 0.5)

    eye_dist = int(order_dct["size_x"] * order_dct["eye_distance"])
    nose_dist = int(order_dct["size_y"] * order_dct["nose_distance"])
    mouth_dist = int(order_dct["size_y"] * order_dct["mouth_distance"])

    eye_seed_size = abs(int(seed_size * order_dct["feature_detail_ratio"])) + 1
    nose_seed_size = abs(int(seed_size * order_dct["feature_detail_ratio"])) + 1
    mouth_seed_size = abs(int(seed_size * order_dct["feature_detail_ratio"])) + 1


    composite_seed = seed_generators.scaled_noise(seed_size,
                                                  order_dct["size_x"],
                                                  order_dct["gamma"],
                                                  order_dct["mask_sharpness"],
                                                  order_dct["random_seed"])[0]

    eye_seed = seed_generators.scaled_noise(eye_seed_size,
                                            eye_size,
                                            order_dct["gamma"],
                                            order_dct["mask_sharpness"],
                                            order_dct["random_seed"])[0]

    nose_seed = seed_generators.scaled_noise(nose_seed_size,
                                             nose_size,
                                             order_dct["gamma"],
                                             order_dct["mask_sharpness"],
                                             order_dct["random_seed"])[0]

    mouth_seed = seed_generators.scaled_noise(mouth_seed_size,
                                              mouth_size,
                                              order_dct["gamma"],
                                              order_dct["mask_sharpness"],
                                              order_dct["random_seed"])[0]


    composite = image_filters.alpha_color(composite_seed,
                                          order_dct["head_color"])[0]

    eye = image_filters.alpha_color(eye_seed,
                                    order_dct["eye_color"])[0]

    nose = image_filters.alpha_color(nose_seed,
                                     order_dct["nose_color"])[0]

    mouth = image_filters.alpha_color(mouth_seed,
                                      order_dct["mouth_color"])[0]

    composite.paste(eye, (eye_center - eye_dist, eye_center - eye_dist), eye)
    composite.paste(eye, (eye_center + eye_dist, eye_center - eye_dist), eye)
    composite.paste(mouth, (mouth_center, mouth_center + mouth_dist), mouth)

    file_path = order_dct["save_path"] + str(img_num) + order_dct["filename"]

    return composite