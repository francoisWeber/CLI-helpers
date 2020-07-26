#! /usr/local/bin/python3
import click
from os import path as osp
from os import remove, listdir

EXTRA_FILE_EXT_LOWERCASE = [".nef", ".raw", ".mov"]
MAIN_FILE_EXT_LOWERCASE = [".jpg", ".jpeg", ".heic", ".heif"]
EXTRA_DIRECTORY_NAME = "RAW"

help = "Purge side-files associated to JPEG/HEIC files associated to deleted files"
@click.command(help=help, no_args_is_help=True)
@click.argument(
    "input_dir",
    type=click.Path(exists=True, dir_okay=True, resolve_path=True, file_okay=False),
)
@click.option("--extra-dir", default=EXTRA_DIRECTORY_NAME, type=click.Path(), help="Directory containing the extra files")
def purge_raw(input_dir, extra_dir):
    input_dir = osp.expanduser(input_dir)
    if osp.isdir(osp.join(input_dir, extra_dir)):
        # list kept JPG
        kept_pics_name_noext = get_jpg_of_dir(input_dir, drop_extension=True)
        # drop RAWs associated to dropped JPG
        raw_dir = osp.join(input_dir, extra_dir)
        raw_to_delete = []
        for raw_fname in listdir(raw_dir):
            raw_pic, ext = osp.splitext(raw_fname)
            if raw_pic not in kept_pics_name_noext and ext.lower() in EXTRA_FILE_EXT_LOWERCASE:
                raw_to_delete.append(osp.join(raw_dir, raw_fname))
        if len(raw_to_delete) > 0:
            for raw_fname in raw_to_delete:
                remove(raw_fname)
            print(f"{len(raw_to_delete)} extra files were removed")
        else:
            print("Directory is already clear")

    else:
        print("Extra-files' directory not found: bye!")


def get_jpg_of_dir(directory, drop_extension):
    jpg_files = [
        osp.splitext(fname)[0] if drop_extension else fname
        for fname in listdir(directory)
        if osp.splitext(fname)[1].lower() in MAIN_FILE_EXT_LOWERCASE
    ]
    return jpg_files


if __name__ == "__main__":
    purge_raw()
