clear all
[cdata1,cmap1]=imread('a:\TimgR.tif','tiff');
N=load('a:\TimgRed3by3.dat');
%N=net.iw{1,1};
%[r1 c1] = size(N);
%r2      = input('Put the desired row,r2=');
%temp1   =zeros(r2,r1*c1/r2);

%p1=1;
%for i1=1:1:r2;
   %for i2=1:1:r1*c1/r2;
     % temp1(i1,i2) = N(p1,1);
     % p1=p1+1;
  %end
%end
imwrite(N,cmap1,'a:\TimgRed3by3.tif','tiff');
%temp2=imread('c:\data\matlab\panda.tif');
%dlmwrite ('g:\Panda\testPSOM1.tif', temp1, 4, 9);
%[temp2,cmap3]=imread(
%h1=image(temp1);
