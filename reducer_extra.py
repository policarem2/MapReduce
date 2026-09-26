import sys

def read_input(input):
    for lines in input:
        yield lines.strip().split()

def main(separator='\t'):
    data = read_input(sys.stdin)

    target = None
    highest_probability = 0
    for key in data: 
        # keep track of the key that contains the highest probability while we iterate through the wholle list
        if float(key[1]) > highest_probability:
            highest_probability = float(key[1])
            target = key
    print('%s%s%s' % (target[0], separator, target[1]))

        


    

if __name__ == "__main__":
    main()