from models import *
from random import choice

class TripleToWordManager(TripleToWord):
    def get_frequency_list(self,triple):
        next_words = TripleToWord.objects.filter(word1=triple[0],
                        word2=triple[1],
                        word3=triple[2])
        freq_list = []
        for next_word in next_words:
            freq_list += [next_word.next_word]*next_word.frequency

        return freq_list
    def get_next_word(self,triple):
        freq_list = self.get_frequency_list(triple)
        next_word = choice(freq_list)
        return next_word

class StartTripleManager(StartTriple):
    def new_start_triple(self):
        start_triples = []
        
        query = StartTriple.objects.all()
        print(query,type(query))
        start_triples = []
        for row in query:
            print(row)
            start_triples.append((row.word1,row.word2,row.word3))
        
        return choice(start_triples)

def generate_random_text():
    text = ""
    stm = StartTripleManager()  
    ttwm = TripleToWordManager()

    triple = stm.new_start_triple()
    text += triple[0] + ' ' + triple[1] + ' ' + triple[2]
    next_word = ttwm.get_next_word(triple)

    while next_word[0] not in "!.?":
        text += ' ' + next_word

        triple = triple[1:3] + (next_word,)
        next_word = ttwm.get_next_word(triple)
    text += next_word

    return text

    


