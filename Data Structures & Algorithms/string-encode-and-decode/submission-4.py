class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for i in strs:
            res += str(len(i)) + "#" + i

        return res
        
    def decode(self, s: str) -> List[str]:
        

        result = []
        left = 0
        right = 0
        length = 0
        while right < len(s):
            
            if s[right] == "#":
                length = int(s[left:right])
                result.append(s[right+1:right+length+1])
                left = right+length+1
                length = 0
                right = left
            else:
                right += 1
        return result
            
        