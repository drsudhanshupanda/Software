clear all
a=imread('g:\Panda\TimgR.tif');
[l m]=size(a);
dlmwrite('g:\Panda\TimgR.dat',a);
