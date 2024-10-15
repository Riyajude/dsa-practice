class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        pattern_set = set(pattern)
        char_to_word = {}
        word_to_char = {}
        
        for p, w in zip(pattern, words):
            if p in char_to_word:
                if char_to_word[p] != w:
                    return False  
            else:
                char_to_word[p] = w 
            
            if w in word_to_char:
                if word_to_char[w] != p:
                    return False 
            else:
                word_to_char[w] = p
        constructed_words = [char_to_word[p] for p in pattern]
        
        if constructed_words == words:
            return True
        else:
            return False
