class Solution:
    def customSortString(self, order: str, s: str) -> str:

        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        ans = ""

        # Add characters according to custom order
        for ch in order:
            if ch in freq:
                ans += ch * freq[ch]
                del freq[ch]

        # Add remaining characters
        for ch, count in freq.items():
            ans += ch * count

        return ans