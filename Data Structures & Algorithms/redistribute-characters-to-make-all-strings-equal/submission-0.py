class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        freq = {}

        for word in words:
            for ch in word:
                freq[ch] = freq.get(ch, 0) + 1

        for count in freq.values():
            if count % len(words) != 0:
                return False

        return True