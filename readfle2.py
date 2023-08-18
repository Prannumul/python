import io

try:
    infile = io.open('tmp2.txt', 'r')
    if infile.readable():
        line = infile.read()
        infile.close()
        print(line)

except:
    print("error\n")