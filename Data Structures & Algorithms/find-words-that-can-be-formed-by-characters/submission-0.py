from collections import Counter 
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = Counter(chars)
        
        total = 0

        for word in words:
            word_count = Counter(word)
            if word_count <= char_count:
                total += len(word)
        return total 
        