function SEA = SAE_feature()
test_sea = sea_data();
load('W1_best.mat')
SEA_test = test_sea;
W1 = W1_best;
N=size(test_sea,1);
k = N;
A = ones(k,1);
test_SEA = [SEA_test,A];
SEA = test_SEA * W1;


