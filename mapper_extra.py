import sys

def read_input(input):
    for lines in input:
        yield lines.strip().split()

def main(separator ='\t'):
    data = read_input(sys.stdin)
    target = "the united"
    for key in data:
        if len(key) == 4:
            temp = " ".join(key[0:2])
            if temp == target:
                print("%s%s%s" % (key[2],separator,key[3]) )
 

if __name__ == "__main__":
    main()