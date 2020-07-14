#! /usr/local/bin/python3

import cv2
import click


def resize_image(image, max_resize_dim):
    orig_dim = image.shape
    if orig_dim[0] < orig_dim[1]:
        dim_of_max = 1
    else:
        dim_of_max = 0
    # deduce scale and secundary dimension
    scale = max_resize_dim / orig_dim[dim_of_max]
    width = int(orig_dim[1] * scale)
    height = int(orig_dim[0] * scale)
    dim = (width, height)
    return cv2.resize(image, dim, interpolation=cv2.INTER_AREA)


def load_image(image_path):
    # return cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
    return cv2.imread(image_path)


def dump_image(image, image_path):
    # image_rgb = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_RGB2BGR)
    cv2.imwrite(image_path, image)


@click.command()
@click.argument('input_path', type=click.Path(exists=True, dir_okay=False, resolve_path=True))
@click.option('-z', '--max-dim', 'max_dim', default=2200)
@click.option('-o', '--output', 'output_path', default=None)
def do_resize(input_path, max_dim, output_path):
    image = load_image(input_path)
    resized = resize_image(image, max_dim)
    if output_path is None:
        output_path = input_path
    cv2.imwrite(output_path, resized)


if __name__ == "__main__":
    do_resize()
