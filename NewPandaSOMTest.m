clear all
a=imread('g:\Panda1\timgR1.tif');
[l m]=size(a);
d=zeros(1,l*m);
p=1;
for i=1:1:l;
   for r=1:1:m;
      d(1,p)=a(i,r);
      p=p+1;
   end
end
dlmwrite('g:\Panda1\Oct22timgR1.txt',d','txt');

y=max(d);
z=min(d);
%clear all
%load G:\Panda\imgG.txt;
p=d;
net=newsom([z y;[]],[36]);
net.trainParam.epochs=1000;
net=train(net,p);
%plotsom(net.iw{1,1},net.layers{1}.distances)
%x=net.iw{1,1};
%x'
N=net.iw{1,1};
[r1 c1] = size(N);
r2      = input('Put the desired row,r2=');
temp1   =zeros(r2,r1*c1/r2);

p1=1;
for i1=1:1:r2;
   for i2=1:1:r1*c1/r2;
      temp1(i1,i2) = N(p1,1);
      p1=p1+1;
   end
end
imwrite(temp1,'g:\Panda1\testtimgR1.tif','tiff');
%temp2=dlmread('c:\data\matlab\panda.tif');
%dlmwrite ('g:\Panda\testPSOM1.tif', temp1, 4, 9);
h1=image(temp1);
