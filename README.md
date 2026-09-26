# MapReduce N-Gram Language Model

A two-stage Hadoop MapReduce pipeline written in Python using Hadoop Streaming.

The program processes a text corpus to calculate conditional trigram probabilities:

P(word3 | word1, word2)

## Pipeline

### Stage 1
- Cleans and normalizes input text
- Generates bigrams and trigrams
- Aggregates their occurrence counts

### Stage 2
- Groups trigrams with their corresponding bigrams
- Calculates conditional probabilities for each trigram

### Extra Credit
A final MapReduce job filters results beginning with "the united" and finds the third word with the highest conditional probability.

## Technologies
- Python
- Apache Hadoop
- Hadoop Streaming
- HDFS
- Docker