import io

try:
    infile = io.open('tmp.txt', 'r')
    if infile.readable():
        line = infile.readline()
        infile.close()
        #print(line)
        linevalues = line.split(' ')
        print(len(linevalues))
        print(linevalues[1])

        #print[linevalues]
        
        
except:
    print("error\n")