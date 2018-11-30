function predict_label = SVM_enesmble(train_X1,train_X2,train_X3,test_X,yapp,N)
test_y = zeros(N,1);
model1=svmtrain(yapp,train_X1,'-c 16 -g 2 -w1 1 -w-1 1');
[pre(:,1), accuracy1, dec_values1]=svmpredict(test_y,test_X,model1);
model2=svmtrain(yapp,train_X2,'-c 16 -g 2 -w1 1 -w-1 1');
[pre(:,2), accuracy1, dec_values1]=svmpredict(test_y,test_X,model2);
model3=svmtrain(yapp,train_X3,'-c 16 -g 2 -w1 1 -w-1 1');
[pre(:,3), accuracy1, dec_values1]=svmpredict(test_y,test_X,model3);

Nt = length(test_y);
for i = 1:Nt
    if (sum(pre(i,:)) >= 1)
        predict_label(i,1) = 1;
    elseif (sum(pre(i,:)) < 1)
        predict_label(i,1) = -1;
    elseif ((pre(i,:)) <= -1)
        predict_label(i,1) = -1;
    elseif ((pre(i,:)) > -1)
        predict_label(i,1) = 1;
    end
end

