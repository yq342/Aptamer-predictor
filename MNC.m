function test_mnc = MNC()
load('apater_head.mat')
load('apater_seq.mat')
nucleotide_hp = apater_head;
nucleotide_positive = apater_seq; 
Np=length(nucleotide_hp);%number of positive samples
for i=1:Np
    Str=nucleotide_positive{1,i};
    Str=char(Str);
    nucleotide_positive{1,i}=Str;
end

% L=length(positive{1,1});%ÿ���Ķεĳ���
AA='ACGT';
PPT1=zeros(Np,4);
for i=1:Np
       Peptide=nucleotide_positive{1,i};
       L = length(Peptide);
    for j=1:L
        s=Peptide(j);
        if s == 'U'
            s = 'T';
        end
        k=strfind(AA,s);
        PPT1(i,k)= PPT1(i,k)+1;
    end
    PPT1(i,:)=PPT1(i,:)/L;
end

%------------------
PPT1(:,4)=[];
test_mnc = PPT1;