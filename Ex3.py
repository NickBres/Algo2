def spaceInsert(sentence, index):
    beforeIndex = sentence[:index]
    afterIndex = sentence[index:]
    return beforeIndex + " " + afterIndex


class Lang:
    def __init__(self, words):
        self.dictionary = sorted(words)

    # O(q)
    def isDictionaryContainsWordStartWith(self, text):
        for word in self.dictionary:
            if text in word:
                return True
        return False

    # O(qn)
    def splitWords(self, sentence):
        i = 0
        while i < len(sentence):
            j = i + 1
            while j < len(sentence) and self.isDictionaryContainsWordStartWith(sentence[i:j]):
                j += 1
            if j < len(sentence):
                sentence = spaceInsert(sentence, j - 1)
            i = j
        return sentence
