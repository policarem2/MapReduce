import sys

def read_mapper_output(input, separator='\t'):
    for lines in input:
        yield lines.rstrip().split(separator)

def main(separator='\t'):
    data = read_mapper_output(sys.stdin, separator=separator)

    bigram_counter = 0
    trigrams = []
    bigram = None
    p = 0

    for key in data:

        # if a new bigram starts, calculate and output probabilities for the previous bigram
        if bigram != None and key[0] != bigram:
            for trigram in trigrams: 
                p = int(trigram[1]) / bigram_counter 
                full_trigram = " ".join([bigram, trigram[0]])
                print('%s%s%s' % (full_trigram, separator, p))
            # reset the count and stored trigrams for the new bigram
            bigram_counter = 0
            trigrams = []
            bigram = key[0]

        if len(key) == 2:
            # store the count for the current bigram
            if bigram == None:
                bigram = key[0]
                bigram_counter = int(key[1])
            elif key[0] == bigram:
                bigram_counter = int(key[1])
            elif key[0] != bigram:
                bigram = key[0]
                bigram_counter = int(key[1])
        # len(key) == 3
        else:
            # save each third word and its trigram count until the bigram count is available
            trigrams.append([key[1], int(key[2])])
            
    # calculate probabilities for the final bigram after the loop ends
    for trigram in trigrams: 
        p = int(trigram[1]) / bigram_counter 
        full_trigram = " ".join([bigram, trigram[0]])
        print('%s%s%s' % (full_trigram, separator, p))

if __name__ == "__main__":
    main()