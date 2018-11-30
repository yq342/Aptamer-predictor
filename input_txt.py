#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkFileDialog

def self_input():
    '''
    自定义一个函数，目的是弹出一个对话框，来输入文件。
    :return:文件的路径
    '''

    # initialdir='E:/Python'
    # filename = tkFileDialog.askopenfilename(initialdir)
    filename = tkFileDialog.askopenfilename()
    return filename