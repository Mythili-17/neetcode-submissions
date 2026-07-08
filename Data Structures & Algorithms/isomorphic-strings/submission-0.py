class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        s_to_t = {}
        t_to_s = {}

        for i in range(len(s)):

            c1 = s[i]
            c2 = t[i]

            # Check mapping from s -> t
            if c1 in s_to_t:
                if s_to_t[c1] != c2:
                    return False
            else:
                s_to_t[c1] = c2

            # Check mapping from t -> s
            if c2 in t_to_s:
                if t_to_s[c2] != c1:
                    return False
            else:
                t_to_s[c2] = c1

        return True