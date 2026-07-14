class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        count = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):

                x = words[i]
                y = words[j]

                if y[:len(x)] == x and y[-len(x):] == x:
                    count += 1

        return count