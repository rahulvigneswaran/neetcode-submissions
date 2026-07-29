class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        base = ord("a")
        for word in strs:
            template = [0]*26
            w_c = Counter(word)
            for letter in w_c.keys():
                template[ord(letter)-base] = w_c[letter]
            res[tuple(template)].append(word)
        return list(res.values())