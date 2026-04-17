class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list) 

        for word in strs:
            print(word)
            sorted_word = ''.join(sorted(word))
            anagram_dict[sorted_word].append(word)
        
        result = []
        for value in anagram_dict.values():
            result.append(value)
        
        return result