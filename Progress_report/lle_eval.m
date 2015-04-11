function Y = lle_eval(origin, outputfile, freq, p, K) % for example, inputfile = 'PMA_HoxA_Interactions.txt' and outputfile = 'out.pdb' and K = 7
    %[freq,p] = random_structure();
    Y = lle_chroma(freq,K);
    printPDB(origin, p);
    printPDB(outputfile, Y);
end

function freq = readPDB(filename)
    input = importdata(filename);
    data = input.data;
    first = min(min(data(:,1:2)))-1;
    last = max(max(data(:,1:2)));
    N = last-first;
    freq = zeros(N);
    for i=1:length(data)
        freq(data(i,1)-first,data(i,2)-first) = data(i,3);
    end
    freq = freq + freq';
end

function printPDB(filename, Y)
    fid=fopen(filename,'w');
    fmt = 'ATOM   % 4d C    LIG A        % 8.3f% 8.3f% 8.3f  1.00 75.00    \n';
    fprintf(fid,fmt, [(1:length(Y)); Y]);
    fprintf(fid,'CONECT % 4d% 4d\n', [(1:length(Y)-1);(2:length(Y))]);
	fprintf(fid,'END');
end