function predict_label = yq_predict()

load('train.mat')
load('order_index.mat')
%% Ãÿ’˜Ã·»°
test_mnc = MNC();
[PseDNC_TEST,PC_PseTNC_TEST,SC_PseTNC_TEST] = read_pse_data_test();
SEA = SAE_feature();
fea_target = SEA;
fea_aptamer = [test_mnc PseDNC_TEST PC_PseTNC_TEST SC_PseTNC_TEST];

m1 = size(fea_aptamer,1);
m2 = size(fea_target,1);
h = 1;
for h1 = 1:m1
    for h2 = 1:m2

        all_test_x = [fea_target(h1,:) fea_aptamer(h2,:)];
        
        N = size(all_test_x,1);
        for i = 1:616
            j = order_index(i);
            test_X(:,i) = all_test_x(:,j);
        end

        predict_label(h,1)= SVM_enesmble(train_X1,train_X2,train_X3,test_X,train_y,N);
        h = h + 1;
    end
end
