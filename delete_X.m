[hf full] = fastaread('test_Target.txt');
N=length(hf);

AA = 'ACDEFGHIKLMNPQRSTVWY';
for i = 1:N
    seq=full{1,i};
    L = length(seq);
    k = 0;
    for j = 1:L
        j = j- k ;
        k1 = 0;
        if ~length(strfind(AA,seq(j)))
            k1 = k1 + 1;
            seq(j) = [];
        end
        k  = k + k1;
    end    
    full{1,i} = seq;
end
fid = fopen('123.txt','wt');
for k=1:N
    fprintf(fid,'%s%d\n%s\n%s\n%s\n','>P',k,full{k});
end
fclose('all');