from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w']+")


class MRWordCount(MRJob):

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            if word[0]=="a" or word[0]=="b" or word[0]=="c" or word[0]=="d" or word[0]=="e" or word[0]=="f" or word[0]=="g" or word[0]=="h" or word[0]=="i" or word[0]=="j" or word[0]=="k" or word[0]=="l" or word[0]=="m" or word[0]=="n":
            	yield "a_to_n", 1
            else:
            	yield "other", 1
            

    def combiner(self, word, counts):
        yield word, sum(counts)

    def reducer(self, word, counts):
        yield word, sum(counts)


if __name__ == '__main__':
    MRWordCount.run()


