intpos=0;
intneg=0;
n=size(t)-1;
for i=1:n(1)
    if FluxP(i)> 0
    intpos=intpos+(FluxP(i)*(t(i+1)-t(i)));  
    elseif FluxP(i)<0
    intneg=intneg+(FluxP(i)*(t(i+1)-t(i)));    
    end
end
totalrechargeP=intpos;
totaldischargeP=intneg;

intpos=0;
intneg=0;
n=size(t)-1;
for i=1:n(1)
    if FluxR(i)> 0
    intpos=intpos+(FluxR(i)*(t(i+1)-t(i)));
    elseif FluxR(i)<0
    intneg=intneg+(FluxR(i)*(t(i+1)-t(i)));    
    end
end
totalrechargeR=intpos;
totaldischargeR=intneg;

int=0;
n=size(t)-1;
for i=1:n(1)
    int=int+(FluxI(i)*(t(i+1)-t(i)));  %fluxI is in mm/day, and t is days, so answer in mm 
end
totaldischargeI=int;