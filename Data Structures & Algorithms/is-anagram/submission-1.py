class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map, t_map = Counter(s), Counter(t)

        return s_map == t_map
