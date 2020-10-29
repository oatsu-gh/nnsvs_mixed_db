#! /usr/bin/env python3
# coding: utf-8
# Copyright (c) oatsu
"""
配布用フォルダを準備する
"""

from glob import glob
from os import makedirs
from shutil import copy2

from tqdm import tqdm

SINGER = 'mixed'
RELEASE_DIR = 'release/mixed_---'
PATH_QUESTION = 'conf/jp_qst001_nnsvs_simple_4-4_mix.hed'
NAME_EXPERIMENT = 'simple_4-4_mix'


def copy_question(path_question, release_dir):
    """
    hedファイル(question)をコピー
    """
    makedirs(f'{release_dir}/conf', exist_ok=True)
    print('copying question')
    copy2(path_question, f'{release_dir}/{path_question}')


def copy_scaler(singer, release_dir):
    """
    dumpフォルダにあるファイルをコピー
    """
    makedirs(f'{release_dir}/dump/{singer}/norm', exist_ok=True)
    list_path_scaler = glob(f'dump/{singer}/norm/*_scaler.joblib')

    print('copying scaler')
    for path_scaler in tqdm(list_path_scaler):
        copy2(path_scaler, f'{release_dir}/{path_scaler}')


def copy_model(singer, name_exp, release_dir):
    """
    name_exp: 試験のID
    """
    name_exp = singer + '_' + name_exp
    makedirs(f'{release_dir}/exp/{name_exp}/acoustic', exist_ok=True)
    makedirs(f'{release_dir}/exp/{name_exp}/duration', exist_ok=True)
    makedirs(f'{release_dir}/exp/{name_exp}/timelag', exist_ok=True)
    list_path_model = glob(f'exp/{name_exp}/*/best_loss.pth')
    list_path_model += glob(f'exp/{name_exp}/*/latest.pth')
    list_path_model += glob(f'exp/{name_exp}/*/model.yaml')

    print('copying model')
    for path_model in tqdm(list_path_model):
        copy2(path_model, f'{release_dir}/{path_model}')


def main():
    """
    各種ファイルをコピーする
    """
    copy_question(PATH_QUESTION, RELEASE_DIR)
    copy_scaler(SINGER, RELEASE_DIR)
    copy_model(SINGER, NAME_EXPERIMENT, RELEASE_DIR)


if __name__ == '__main__':
    main()
