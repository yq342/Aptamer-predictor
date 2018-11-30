function test_sea = sea_data()

load('target_seq.mat')
load('target_head.mat')
hf = target_head;
full = target_seq; 

N =length(hf);
AA='ACDEFGHIKLMNPQRSTVWY';
for i = 1:N
    L = length(full{i});
    M1 = zeros(20,52);
    for j = 1:52
        h = full{i}(j);
        k=strfind(AA,h);
        M1(k,j) = 1;
    end

    M(:,:,i) = M1;
%     figure
%     imshow(M(:,:,i))
end
A = reshape(M,1040,N);
B = A';
test_sea = B;


