clear all
a=imread('g:\Panda\TimgG.tif');
t=a;
t=t(55:63,55:63);
[l m]=size(t);
d=zeros(1,l*m);
p=1;
for i=1:1:l;
   for r=1:1:m;
      d(1,p)=a(i,r);
      p=p+1;
   end
end
dlmwrite('g:\Panda\TestimgG.txt',d');
