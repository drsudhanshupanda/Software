pathfrom = 'G:\Panda\ClusteringChicagoPaper\BMP\';
d = dir(pathfrom);
for count = 3:length(d);
   datafile = d(count).name;
   a=imread(strcat(pathfrom,datafile));
	[l m]=size(a);
	q=zeros(1,l*m);
	p=1;
	for i=1:1:l;
   	for r=1:1:m;
     		 q(1,p)=a(i,r);
      	 p=p+1;
   	end
   end
   pathto  = 'G:\Panda\ClusteringChicagoPaper\BMP\';
	%pathto  = 'G:\Panda\SOM\Txt99\';   
   b = strcat(pathto,datafile(1:length(datafile)-3));
   %fileName = strcat(b,'txt');
   %dlmwrite(fileName,num2str(double(q')),'');
   y=max(q);
	z=min(q);
	net=newsom([z y;[]],[12]);
	net.trainParam.epochs=1000;
	net=train(net,q);
	%plotsom(net.iw{1,1},net.layers{1}.distances)
   x=net.iw{1,1};
   %pathto  = 'G:\Panda\SOM\99SOMCentroid\';   
   fileName3 = strcat(b,'txt');
   dlmwrite(fileName3,num2str(double(x')),'');
end