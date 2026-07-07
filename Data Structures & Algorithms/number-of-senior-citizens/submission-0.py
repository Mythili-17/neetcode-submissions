class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for word in details:
            if int(word[11:13]) > 60 :
                count += 1
        return count 


           

        