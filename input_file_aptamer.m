function FileName = input_file_aptamer1()
[FileName1, PathName, FilterIndex]=uigetfile('.txt','Select file to open');%��ʾʹ��������
[hf full] = fastaread(FileName1);
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
N = length(hf);

AA = 'ACGT'
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


fid = fopen(FileName1,'wt');
for k=1:N
    fprintf(fid,'%s%s\n%s\n','>',hf{1,k},full{1,k});
end
fclose('all');
[apater_head apater_seq]=fastaread(FileName1);
FileName = FileName1;
FileName
save apater_head apater_head
save apater_seq apater_seq
