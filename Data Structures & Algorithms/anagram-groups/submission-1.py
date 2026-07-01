class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        words_map = {}

        for strings in strs:
            sorted_key = "".join(sorted(strings))

            if sorted_key not in words_map:
                words_map[sorted_key] = []

            words_map[sorted_key].append(strings)

        return list(words_map.values())
            
        