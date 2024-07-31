class Solution(object):
    def findWordsContaining(self, words, x):
        indices = []
        
        for index, word in enumerate(words):
            if x in word:
                indices.append(index)
        
        return indices
