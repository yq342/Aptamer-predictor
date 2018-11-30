
[hf full] = fastaread('train_protain_Target_pos.txt');
N = length(hf);
for i = 1 : N  
    seq = full{1,i};
    L = length(seq); 
    for j = 1 : L
        if seq(j) == 'U'
            seq(j) = 'T';
        end
    end
    full{1,i} = seq;
end


fid = fopen('123.txt','wt');
for k=1:N
    fprintf(fid,'%s%d\n%s\n%s\n%s\n','>P',k,full{k});
end
fclose('all');