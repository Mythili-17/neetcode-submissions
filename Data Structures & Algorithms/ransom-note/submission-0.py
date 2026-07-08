class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        temp = list(magazine)
        for ch in ransomNote:
            
            if ch in temp :
                temp.remove(ch)
            else:
                return False 
        return True 
        