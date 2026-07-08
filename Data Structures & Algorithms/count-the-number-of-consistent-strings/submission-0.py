class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            good = True
            temp = list(allowed)
            for ch in word:
                if ch not in temp:
                    good = False 
                    break
            if good:
                count += 1
                

        return count 
            


        