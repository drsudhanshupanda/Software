clear all
a=imread('g:\Panda\TimgR.tif');
[l m]=size(a);
d=zeros(1,l*m);
p=1;
for i=1:1:l;
   for r=1:1:m;
      d(1,p)=a(i,r);
      p=p+1;
   end
end
dlmwrite('g:\Panda\TimgR.dat',d');
y=min(d);
z=max(d);
