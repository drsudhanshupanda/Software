clear all
a=imread('G:\Panda\ClusteringChicagoPaper\BMP\R1.bmp');
[l m]=size(a);
d=zeros(1,l*m);
p=1;
for i=1:1:l;
   for r=1:1:m;
      d(1,p)=a(i,r);
      p=p+1;
   end
end
[cdata1,cmap1]=imread('a:\TimgR1.tif','tiff');
N=d';
[r1 c1] = size(N);
k       = input ('Put the number of clusters, k=');
classes = dcKMeans(N,k);
classes = 35*classes;
r2      = input('Put the desired row, r2=');
temp1   = zeros(r2,r1*c1/r2);

p1=1;
for i1=1:1:r2;
   for i2=1:1:r1*c1/r2;
      temp1(i1,i2) = classes(p1,1);
      p1=p1+1;
   end
end
imwrite(temp1,cmap1,'G:\Panda\ClusteringChicagoPaper\BMP\Red1.tif','tiff');

