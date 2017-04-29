function [X] = read_file(meta_file)

X = [];
meta_fildes = fopen(meta_file, 'rt');
while ~feof(meta_fildes)
   line = fgetl(meta_fildes);
   if size(line,2) ~= 5
       continue;
   end
   if line(3) == '_'
       path = strcat('../data/', line(1:2), '/', line(1:5), '.amc');
   else
       path = strcat('../data/', line(1:3), '/', line(1:6), '.amc');
   end
   x = amc_to_matrix(path);
   X = [X; x];
end

end