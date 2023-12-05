# -*- coding: utf-8 -*-

import os
import glob
import argparse


def get_parse():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--path')
    parser.add_argument('--save_path', )

    args = parser.parse_args()
    return args

opt = get_parse()
video_names = os.listdir(opt.path)

os.makedirs(opt.save_path,exist_ok = True)

for video_name in video_names:
    video_path = os.path.join(opt.path, video_name).replace(' ','\ ')
    target_path = os.path.join(opt.save_path, video_name).replace(' ','\ ')

    os.system('ffmpeg -i {} -b:v 1.0M {}'.format(video_path, target_path))



