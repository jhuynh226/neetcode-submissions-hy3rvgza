class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDictionary, tDictionary = {}, {}

        for char in s:
            if char in sDictionary:
                sDictionary[char] += 1
            else:
                sDictionary[char] = 1

        for char in t:
            if char in tDictionary:
                tDictionary[char] += 1
            else:
                tDictionary[char] = 1
        
        return sDictionary == tDictionary
        