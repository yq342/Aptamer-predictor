#!/usr/bin/python
# -*- coding: UTF-8 -*-


import input_txt
import numpy as np
from collections import OrderedDict
from mlab.releases import latest_release as matlab

#弹出对话框，提示用户输入文件
path = input_txt.self_input()

def read_biodata(data_file):
    '''
    data_file是保存有生物序列的fasta格式的txt文件,并将它保存在字典中，原来的顺序保存在列表中
    :param data_file: data_file是保存有生物序列的fasta格式的txt文件
    :return:返回
    '''
    file = open(data_file)
    seq = {}
    list = []       #由于字典不记录顺序，因此创建一个列表，用来保存键
    #将>进行命名,保存成为字典的形式
    for line in file:
        if line.startswith('>'):
            name = line.replace('>','').split()[0]
            seq[name] = ''      #指的是序列
            list.append(name)       #将每一个键值保存到列表中
        else:
            seq[name] += line.replace('\n','')      #目的是把换行符给去掉
    file.close()
    seq = OrderedDict(seq.iteritems())
    return seq,list

seq,list = read_biodata(path)

matlab.path(matlab.path(),r'E:\Bioinformation\yq_aptamer\yq_aptamer_web\Pse-in-One-2.0')#设置路径，注意E:\python&matlab为放置MATLAB程序的路径
mnc = matlab.web()#调用自己定义的m函数就可以了，注意，这里的k3mer为自己定义的MATLAB函数，然后将结果赋给k3mer就好了。
