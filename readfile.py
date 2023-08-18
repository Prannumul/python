import io

try:
    infile = io.open('tmp.txt', 'r')
    if infile.readable():
        #print("file is readable")
        line = infile.readlines()
        length = len(line)
        lineIndex = 0
        while(lineIndex < length):
            print(line[lineIndex])
            lineIndex = lineIndex + 1

        #print(line)
        infile.close()
except:
    print("error\n")

