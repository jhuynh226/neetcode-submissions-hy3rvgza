class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_map, t_map = Counter(s), Counter(t)
        # return s_map == t_map
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for key in countS:
            if countS[key] != countT.get(key, 0):
                return False
                
        return True


