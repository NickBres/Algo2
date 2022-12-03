def spaceInsert(sentence, index):

    beforeIndex = sentence[:index]
    afterIndex = sentence[index:]
    return beforeIndex + " " + afterIndex


class Lang:
    def __init__(self, words):
        self.dictionary = sorted(words)

    # O(qn)
    def splitWords(self, sentence):
        i = 0
        j = 1
        while j < len(sentence):
            while j < len(sentence) and not (sentence[i:j] in self.dictionary): # find first word
                j += 1
            k = j + 1
            while k < len(sentence) and not (sentence[j:k] in self.dictionary): # find second word
                k += 1
            if sentence[j:k] in self.dictionary: # split first and second word
                sentence = spaceInsert(sentence,j)
                i = j + 1
                j = k + 1
            else:
                j += 1
        return sentence
