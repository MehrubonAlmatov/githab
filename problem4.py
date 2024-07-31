class Solution(object):
    def mostWordsFound(self, sentences):
        max_words = 0
        
        for sentence in sentences:
            words = sentence.split()
            
            word_count = len(words)
            
            if word_count > max_words:
                max_words = word_count
        
        return max_words
