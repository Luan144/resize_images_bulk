import os
from pathlib import Path
from PIL import Image
from utils.logics import resize_with_padding, resize_without_padding
from utils.parser import parser


args = parser.parse_args()
padding = args.padding
expected_size = (args.x, args.y)
prefix = args.prefix

if __name__ == "__main__":

    dir_list = [x for x in Path("datasets").iterdir() if x.is_dir()]
    assert dir_list != [], "Datasets folder is empty."

    for folder in dir_list:
        if folder.stem not in os.listdir("results"):
            os.mkdir("results/"+folder.stem)
        for image_file in os.listdir(f"datasets/{folder.stem}"):
            origin = os.path.join("datasets", folder.stem, image_file)
            destination = os.path.join("results", folder.stem)

            img = Image.open(origin)
            if padding == "padding":
                img = resize_with_padding(img, expected_size)
            else:
                img = resize_without_padding(img, expected_size)

            img.save(fp=f"{destination}/{prefix}{image_file}", format="JPEG")
