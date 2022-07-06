class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = str(bin(int(a,2) + int(b,2)))
        return res[2:]
        
        