#! /usr/local/bin/python3
import click
from os import path as osp
from os import remove, listdir

RAW_FILE_EXT_LOWERCASE = [".nef", ".raw"]
JPG_FILE_EXT_LOWERCASE = [".jpg", ".jpeg"]
RAW_DIRECTORY_NAME = "RAW"


@click.command()
@click.argument(
    "input_dir",
    type=click.Path(exists=True, dir_okay=True, resolve_path=True, file_okay=False),
)
def purge_raw(input_dir):
    input_dir = osp.expanduser(input_dir)
    if osp.isdir(osp.join(input_dir, RAW_DIRECTORY_NAME)):
        # list kept JPG
        kept_pics_name_noext = get_jpg_of_dir(input_dir, drop_extension=True)
        # drop RAWs associated to dropped JPG
        raw_dir = osp.join(input_dir, RAW_DIRECTORY_NAME)
        raw_to_delete = []
        for raw_fname in listdir(raw_dir):
            raw_pic, ext = osp.splitext(raw_fname)
            if raw_pic not in kept_pics_name_noext and ext.lower() in RAW_FILE_EXT_LOWERCASE:
                raw_to_delete.append(osp.join(raw_dir, raw_fname))
        if len(raw_to_delete) > 0:
            for raw_fname in raw_to_delete:
                remove(raw_fname)
            print(f"{len(raw_to_delete)} RAW files were removed")
        else:
            print("Directory is already clear")

    else:
        print("No RAW directory detected: bye!")


def get_jpg_of_dir(directory, drop_extension):
    jpg_files = [
        osp.splitext(fname)[0] if drop_extension else fname
        for fname in listdir(directory)
        if osp.splitext(fname)[1].lower() in JPG_FILE_EXT_LOWERCASE
    ]
    return jpg_files


if __name__ == "__main__":
    purge_raw()
