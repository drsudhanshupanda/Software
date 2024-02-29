clear all
a=imread('g:\Panda\RedBand\R90.tif');
[l m]=size(a);
d=zeros(1,l*m);
p=1;
for i=1:1:l;
   for r=1:1:m;
      d(1,p)=a(i,r);
      p=p+1;
   end
end
dlmwrite('g:\Panda\RedBand\R90.txt',d');

y=max(d);
z=min(d);
%clear all
%load G:\Panda\imgG.txt;
p=d;
net=newsom([z y;[]],[3]);
net.trainParam.epochs=1000;
net=train(net,p);
%plotsom(net.iw{1,1},net.layers{1}.distances)
x=net.iw{1,1};
x'