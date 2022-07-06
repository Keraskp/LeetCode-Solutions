class Solution:
    def __init__(self):
        self.num = 1
        
    def isPowerOfThree(self, n: int) -> bool:
        return self.recur(n)
    
    def recur(self,n):
        if self.num == n :
            return True
        if self.num > n :
            return False
        else :
            self.num = 3*self.num
            return self.recur(n)