import sys

def read_mapper_output(input, separator='\t'):
    for lines in input:
        yield lines.rstrip().split(separator, 1)


def main(separator='\t'):
    data = read_mapper_output(sys.stdin, separator=separator)

    prev_key = None
    counter = 0
    # compare each sorted key to the previous key to count repeated bigrams/trigrams
    for key in data:
        key = key[0]
        if prev_key == None:
            prev_key = key
            counter = 1
        elif key != prev_key:
            # when the key changes, output the completed count and start counting the new key
            print('%s%s%d' % (prev_key, separator, counter))
            prev_key = key
            counter = 1  
        # key == prev_key:
        else:
            prev_key = key
            counter = counter + 1
    
    print('%s%s%d' % (prev_key, separator, counter))
    

        

if __name__ == "__main__":
    main()

