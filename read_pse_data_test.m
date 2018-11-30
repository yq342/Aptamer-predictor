function [PseDNC_TEST,PC_PseTNC_TEST,SC_PseTNC_TEST]= read_pse_data_test()

f1 = importdata('PseDNC_TEST.txt');
PseDNC_TEST = f1;
f2 = importdata('PC_PseTNC_TEST.txt');
PC_PseTNC_TEST = f2;
f3 = importdata('SC_PseTNC_TEST.txt');
SC_PseTNC_TEST = f3;
