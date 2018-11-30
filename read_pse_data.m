function [PseDNC,PseTNC_66,PseTNC_88]= read_pse_data()
f1 = importdata('pos_PseDNC.txt');
PseDNC_1 = f1;
f2 = importdata('neg_PseDNC.txt');
PsedNC_2 = f2;
f3 = importdata('pos_SC_PseTNC.txt');
PseTNC01_1 = f3;
f4 = importdata('neg_SC_PseTNC.txt');
PseTNC01_2 = f4;
f5 = importdata('pos_PC_PseTNC.txt');
PseTNC02_1 = f5;
f6 = importdata('neg_PC_PseTNC.txt');
PseTNC02_2 = f6;
PseDNC = [PseDNC_1;PsedNC_2];
PseTNC_88 = [PseTNC01_1;PseTNC01_2];
PseTNC_66 = [PseTNC02_1;PseTNC02_2];


% save PseDNC PseDNC
% save PseTNC_66 PseTNC_66
% save PseTNC_88 PseTNC_88