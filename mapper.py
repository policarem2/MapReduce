import sys
import re

def read(input):
    for line in input:
        # replace anything that isn't a letter or number with a space; regex lets me identify and replace this pattern
        line = re.sub(r"[^a-zA-Z0-9]"," ", line)
        yield line.lower().strip().split()

def main(separator ='\t'):
    data = read(sys.stdin)

    for words in data:
        #  stop at len(words)-2 so each iteration has three words available for a trigram
        for index in range(0, len(words)-2):
            # use join to create the bigram and trigram from each group of words
            bigram = " ".join(words[index:index+2])
            trigram = " ".join(words[index:index+3])

            print('%s%s%d' % (bigram, separator, 1))
            print('%s%s%d' % (trigram, separator, 1))


if __name__ == "__main__":
    main()