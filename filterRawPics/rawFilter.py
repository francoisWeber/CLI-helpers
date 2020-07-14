#! /usr/bin/python

import argparse
import os.path as osp
import os
import sys

RAW_SUBDIR_NAME = 'RAW'

# where to search ?
parser = argparse.ArgumentParser(
    description='Filter RAW files in a photo album')
parser.add_argument('dir',
                    type=str,
                    default=os.getcwd(),
                    nargs='?',
                    help='Path in which to work. Default is "."')
args = parser.parse_args()
dir_path = args.dir

# List JPG files in main directory
remaining_pics = []
for f in os.listdir(dir_path):
    if osp.isfile(osp.join(dir_path, f)):
        fname_and_ext = f.split('.')
        if fname_and_ext[-1].lower() in ['jpg', 'jpeg']:
            remaining_pics.append(fname_and_ext[0])

# if nothing to do : exit
if len(remaining_pics) == 0:
    sys.exit()

# now look into RAW/ subdir and delete files not in remaining_pics
raw_files = os.listdir(osp.join(dir_path, RAW_SUBDIR_NAME))
for f in raw_files:
    if osp.isfile(osp.join(dir_path, RAW_SUBDIR_NAME, f)):
        fname = f.split('.')[0]
        if fname not in remaining_pics:
            os.remove(osp.join(dir_path, RAW_SUBDIR_NAME, f))
