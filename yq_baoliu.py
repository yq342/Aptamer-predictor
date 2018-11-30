#!/usr/bin/env python
# encoding:utf-8
import pse
import argparse
from argparse import RawTextHelpFormatter
from mlab.releases import latest_release as matlab
from mlab.releases import latest_release as matlab
from mlab.releases import latest_release as matlab
from collections import OrderedDict
import numpy as np
import math


matlab.path(matlab.path(),r'E:\Bioinformation\yq_aptamer\yq_aptamer_web\Pse-in-One-2.0')#设置路径，注意E:\python&matlab为放置MATLAB程序的路径
print "请输入适配体序列"
path_aptamer  = matlab.input_file_01()#调用自己定义的m函数就可以了，注意，这里的k3mer为自己定义的MATLAB函数，然后将结果赋给k3mer就好了。
print "请输入靶点序列"
path_target  = matlab.input_file_02()#调用自己定义的m函数就可以了，注意，这里的k3mer为自己定义的MATLAB函数，然后将结果赋给k3mer就好了。
# print path

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

seq, list = read_biodata(path_aptamer)


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
print args
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
print args
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
print args
pse.main(args)

predict_label  = matlab.web()#调用自己定义的m函数就可以了，注意，这里的k3mer为自己定义的MATLAB函数，然后将结果赋给k3mer就好了。
# test_Y = np.row_stack([np.ones([145,1]),-1*np.ones([435,1])])

# print predict_label
# TP1 = 0
# FP1 = 0
# TN1 = 0
# FN1 = 0
# for i in range(len(test_Y)):
#     if (test_Y[i] == 1 and (predict_label[i]) == 1):
#         TP1 = TP1 + 1
#     elif (test_Y[i] == 1 and (predict_label[i]) == -1):
#         FN1 = FN1 + 1
#     elif (test_Y[i] == -1 and (predict_label[i]) == -1):
#         TN1 = TN1 + 1
#     elif (test_Y[i] == -1 and (predict_label[i]) == 1):
#         FP1 = FP1 + 1
#
# SN = TP1 / (float(TP1 + FN1)) * 100  # Sensitivity = TP/P  and P = TP + FN
# SP = TN1 / float(FP1 + TN1) * 100  # Specificity = TN/N  and N = TN + FP
# ACC = (TP1 + TN1) / (float(TP1 + FP1 + TN1 + FN1)) * 100
# MCC = (TP1 * TN1 - FP1 * FN1) / (math.sqrt(TP1 + FP1) * math.sqrt(TP1 + FN1) * math.sqrt(TN1 + FP1) * math.sqrt(TN1 + FN1))
#
# # print 'SN= ',SN
# # print 'SP= ',SP
# # print 'ACC= ',ACC
# # print 'MCC= ',MCC
# # print
# for i in range(len(predict_label)):
#     if predict_label[i] == 1:
#         print '\33[91m '+ '>'+list[i]+ '\33[0m'
#         print '\33[91m '+ seq[list[i]]+'-----positve'+ '\33[0m'
#     else:
#         print '>' + list[i]
#         print seq[list[i]]+'-----negative'
for i in range(len(predict_label)):
    if predict_label[i] == 1:
        print '\33[91m '+ '>'+list[i]+ '\33[0m'
        print '\33[91m '+ seq[list[i]]+'-----positve'+ '\33[0m'
    else:
        print '>' + list[i]
        print seq[list[i]]+'-----negative'
