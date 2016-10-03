from models import *
from random import choice

class TripleToWordManager(TripleToWord):
    def get_frequency_list(triple):
        next_words = filter(word1=triple[0],
                        word2=triple[1],
                        word3=triple[2])
        freq_list = []
        for next_word in next_words:
            freq_list += [next_word.next_word]*next_word.frequency
            # TODO: Check if len(next_words) == 1

        return freq_list
    def get_next_word(triple):
        freq_list = TripleToWordManager.get_frequency_list(triple)
        next_word = choice(freq_list)
        return next_word

class StartTripleManager(StartTriple):
    start_triples = None
    def new_start_triple():
        if not start_triples:
            query = StartTriple.objects.all()
            start_triples = []
            for row in query:
                start_triples.append(row) #transform row into 
                                                #sth pythonesque
        while True:
            yield choice(start_triples)
