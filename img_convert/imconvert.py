#! /usr/local/bin/python3

from cv2 import imread, imwrite, IMWRITE_JPEG_QUALITY
import click
from os import path as osp
from os import remove
from tqdm import tqdm


@click.command()
@click.argument('input_paths', nargs=-1, type=click.Path(exists=True, dir_okay=False, resolve_path=True))
@click.option('-t', '--output-type', default="jpg", type=click.STRING)
@click.option('-d', '--delete-original', default=False, is_flag=True)
def main_convert(input_paths, output_type, delete_original):
    if any([fpath.endswith("heic") for fpath in input_paths]):
        print("HEIC files detected : not gonna convert them !")
        input_paths = [fpath for fpath in input_paths if fpath.endswith("heic")]
    for input_path in tqdm(input_paths):
        convert(input_path, output_type, delete_original)

def convert(input_path, output_type, delete_original):  
    image = imread(input_path)
    # compute output path
    output_type = output_type.lower()
    input_path_no_ext = osp.splitext(input_path)[0]
    output_path = f"{input_path_no_ext}.{output_type}"
    # write image
    if output_type == "jpg":
        params = [IMWRITE_JPEG_QUALITY, 100]
    else:
        params = None
    imwrite(output_path, image, params)
    # eventually delete original file
    remove(input_path)


if __name__ == "__main__":
    main_convert()
