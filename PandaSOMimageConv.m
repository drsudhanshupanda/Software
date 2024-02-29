[cdata1,cmap1]=imread('a:\TimgR1.tif','tiff');
[r1 c1] = size(classes);
r2      = input('Put the desired row, r2=');
temp1   = zeros(r2,r1*c1/r2);

p1=1;
for i1=1:1:r2;
   for i2=1:1:r1*c1/r2;
      temp1(i1,i2) = classes(p1,1);
      p1=p1+1;
   end
end
imwrite(temp1,cmap1,'G:\Panda\ClusteringChicagoPaper\BMP\RedSOM1.tif','tiff');