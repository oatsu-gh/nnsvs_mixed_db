#! /usr/bin/env python3
# coding: utf-8
# Copyright (c) 2020 oatsu
"""
混合モデル用にフルラベルを改変する。
未設定のラベルの部分に歌唱者名を入れる。
p16に歌唱者名を入れる。
"""

from os.path import basename
from glob import glob
from tqdm import tqdm


def main():
    """
    フルラベルファイルのp16に歌唱者名を仕込む。
    """
    # フルラベルファイルが入ってるフォルダを指定
    label_dir = input('label_dir: ').strip('"')
    # フルラベル全ファイル取得
    l = glob(f'{label_dir}/**/*.lab', recursive=True)
    # ラベルファイルのp16部分に歌唱者名を埋め込む
    for path_label in tqdm(l):
        singer = basename(path_label).split('__')[0]
        with open(path_label, 'r') as fl:
            s = fl.read()
        s = s.replace(']xx/A:', f']{singer}/A:')
        with open(path_label, 'w') as fl:
            fl.write(s)


if __name__ == '__main__':
    main()
