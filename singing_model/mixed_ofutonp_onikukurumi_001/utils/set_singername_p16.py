#! /usr/bin/env python3
# coding: utf-8
# Copyright (c) 2020 oatsu
"""
混合モデル用にフルラベルを改変する。
未設定のラベルの部分に歌唱者名を入れる。
p16に歌唱者名を入れる。
"""

# from os.path import basename
from glob import glob
from sys import argv

from tqdm import tqdm


def main(path_dir_lab):
    """
    フルラベルファイルのp16に歌唱者名を仕込む。
    """
    # 歌唱者名を選択
    d_singer = {'1': 'OfutonP', '2': 'OnikuKurumi'}
    key = str(input(f'Select singer by number {d_singer}\n>>> '))
    singer = d_singer[key]

    # フルラベルファイルが入ってるフォルダを指定
    # フルラベル全ファイル取得
    l = glob(f'{path_dir_lab}/*.lab')
    # ラベルファイルのp16部分に歌唱者名を埋め込む
    for path_label in tqdm(l):
        with open(path_label, 'r') as fl:
            s = fl.read()
        s = s.replace(']xx/A:', f']{singer}/A:')
        with open(path_label, 'w') as fl:
            fl.write(s)


if __name__ == '__main__':
    main(argv[1])
