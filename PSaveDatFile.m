%Creates a file in the target directory with the name in datafile.
a=imread('g:\Panda\GreenBand\G5.tif');
target_path='g:\panda\txt\';

      fid = fopen(strcat(target_path,a.dat),'w');		
      
      %Writes numbers2 data into created file
      for i = 1:12
         for j = 1:27
         count = fprintf(fid,'%1.7f\n',a(i,j)); 
        end
      end
      
      %closes the file previously identified
      fclose(fid);		