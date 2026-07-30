class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res = res + str(len(word)) + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        L = 0
        R = L + 1

        while L < R and R < len(s):
            while s[R] != "#":
                R += 1
            
            num = int(s[L:R])
            res.append(s[R+1:R+1+num])
            L = R+1+num
            R = L + 1
        
        return res