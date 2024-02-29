clear all
load G:\Panda\G77.txt;
p=G77';
net=newsom([y z;[]],[6]);
net.trainParam.epochs=1000;
net=train(net,p);
 	 plotsom(net.iw{1,1},net.layers{1}.distances)

x=net.iw{1,1};