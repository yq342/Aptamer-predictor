#!/usr/bin/env python
# encoding:utf-8
import pse
import argparse
from argparse import RawTextHelpFormatter
from mlab.releases import latest_release as matlab
from collections import OrderedDict


matlab.path(matlab.path(),r'E:\Bioinformation\yq_aptamer\yq_aptamer_web\Pse-in-One-2.0')
print "请输入适配体序列"
path_aptamer  = matlab.input_file_aptamer()
print path_aptamer
print "请输入靶点序列"
path_target  = matlab.input_file_target()
print path_target
# print path

def read_biodata(data_file):
    '''
    data_file是保存有生物序列的fasta格式的txt文件,并将它保存在字典中，原来的顺序保存在列表中
    :param data_file: data_file是保存有生物序列的fasta格式的txt文件
    :return:返回
    '''
    file = open(data_file)
    seq = {}
    list = []
    i = 1;
    for line in file:
        if line[0] == ">":
            name = line.strip()[1:]
            seq[name] = ''      #指的是序列
            list.append(name)       #将每一个键值保存到列表中
        else:
            seq[name] += line.replace('\n','')      #目的是把换行符给去掉
        i = i + 1;
    file.close()
    seq = OrderedDict(seq.iteritems())
    return seq,list

seq_aptamer, list_aptamer = read_biodata(path_aptamer)
seq_target, list_target = read_biodata(path_target)

# PseDNC
parse = argparse.ArgumentParser(description="This is pse module for generate pse vector.",
                                formatter_class=RawTextHelpFormatter)
args = parse.parse_args()
args.alphabet = 'DNA'
args.method = 'PseKNC'
args.k = 2
args.inputfiles = [path_aptamer]
args.out = ['PseDNC_TEST.txt']
args.lamada = 3
args.w = 0.05
args.i = 'propChosen_DNC.txt'
args.labels = ['+1', '-1']
args.f = 'csv'
args.e = None
args.a = 'False'
pse.main(args)

# PC-PseTNC-General
args = parse.parse_args()
args.alphabet = 'DNA'
args.method = 'PC-PseTNC-General'
args.k = 3
args.inputfiles = [path_aptamer]
args.out = ['PC_PseTNC_TEST.txt']
args.lamada = 2
args.w = 0.05
args.i = 'propChosen_TNC.txt'
args.labels = ['+1', '-1']
args.f = 'csv'
args.e = None
args.a = 'False'
pse.main(args)

# SC-PseTNC-General
args = parse.parse_args()
args.alphabet = 'DNA'
args.method = 'SC-PseTNC-General'
args.k = 3
args.inputfiles = [path_aptamer]
args.out = ['SC_PseTNC_TEST.txt']
args.lamada = 2
args.w = 0.05
args.i = 'propChosen_TNC.txt'
args.labels = ['+1', '-1']
args.f = 'csv'
args.e = None
args.a = 'False'
pse.main(args)

predict = matlab.yq_predict_01()
print '预测结果输出'

j = 0;
for i in (list_aptamer):
    if predict[j] == 1:
        print '\33[91m'+ '>' + i+ '(aptamer)' + '  +  >' + list_target[j] +'(target)'+'-----positve' + '\33[0m'
    else:
        print '>' + i + '(aptamer)'+ '  +  >' + list_target[j] +'(target)' + '-----negative'
    j = j + 1;