# -*- coding: utf-8 -*-

"""

1、安装库 pip install pymupdf

2、直接运行

"""
import os
import fitz

pdf_path = '1.pdf'

def conver_img(pdf):
    doc = fitz.open(pdf)
    for pg in range(doc.page_count):
        page = doc[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为2，这将为我们生成分辨率提高四倍的图像。
        zoom_x = 2.0
        zoom_y = 2.0
        trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
        pm = page.get_pixmap(matrix=trans, alpha=False)
        pm.save('%s.png' % pg)


if __name__ == '__main__':
    conver_img(pdf_path)
