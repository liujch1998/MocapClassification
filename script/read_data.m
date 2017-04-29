X = cell(8,1);

X{1} = read_file('file_index/01_walk');
X{2} = read_file('file_index/02_run');
X{3} = read_file('file_index/03_jump');
X{4} = read_file('file_index/04_climb');
X{5} = read_file('file_index/05_kick');
X{6} = read_file('file_index/06_swing');
X{7} = read_file('file_index/07_boxing');
X{8} = read_file('file_index/08_eating');

csvwrite('01.csv', X{1});
csvwrite('02.csv', X{2});
csvwrite('03.csv', X{3});
csvwrite('04.csv', X{4});
csvwrite('05.csv', X{5});
csvwrite('06.csv', X{6});
csvwrite('07.csv', X{7});
csvwrite('08.csv', X{8});
