class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        ans = []

        for i in range(len(words)):#outer loops
            for j in range(len(words)):#checks each word again 

                if i != j and words[i] in words[j]:
                    ans.append(words[i])
                    break

        return ans