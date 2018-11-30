function predict_label = yq_predict_01()
clear
clc
load('train.mat')
load('order_index.mat')
%% Ãÿ’˜Ã·»°
test_mnc = MNC();
[PseDNC_TEST,PC_PseTNC_TEST,SC_PseTNC_TEST] = read_pse_data_test();
SEA = SAE_feature();
fea_target = SEA;
fea_aptamer = [test_mnc PseDNC_TEST PC_PseTNC_TEST SC_PseTNC_TEST];

m1 = size(fea_target,1);
m2 = size(fea_aptamer,1);

h = 1;

all_test_x = [fea_target fea_aptamer];

N = size(all_test_x,1);
for i = 1:616
    j = order_index(i);
    test_X(:,i) = all_test_x(:,j);
end
predict_label= SVM_enesmble(train_X1,train_X2,train_X3,test_X,train_y,N);

predict_label;

