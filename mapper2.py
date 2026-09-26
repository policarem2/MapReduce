import sys

def read_input(input):
    for lines in input:
        yield lines.strip().split()

def main(separator='\t'):

    data = read_input(sys.stdin)
    count = 0

    for words in data:
        # split the trigram so it can be grouped with its corresponding bigram
        if len(words) == 4:
            bigram = " ".join(words[0:2])
            tri = words[2]
            count = words[3]
            # output the bigram, third word, and trigram count separately
            print('%s%s%s%s%s' % (bigram, separator, tri, separator, count))
        # len(words) == 3
        else:
            bigram = " ".join(words[0:2])
            count = words[2]
            # output the bigram and its count
            print('%s%s%s' % (bigram,separator,count)) 
        

        

if __name__ == "__main__":
    main()