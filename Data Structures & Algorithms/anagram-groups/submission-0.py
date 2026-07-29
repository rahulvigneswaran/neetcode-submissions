class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            template = [0]*26
            for letter in word:
                template[ord(letter)-ord("a")] += 1
            res[tuple(template)].append(word)
        return list(res.values())