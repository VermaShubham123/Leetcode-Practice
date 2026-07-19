class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        ans = s
        if n == 1:
            return ans
        ans+= m * (n//2)
        ans-= (n//2 -1)
        return ans
        