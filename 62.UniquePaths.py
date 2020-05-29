class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def factorial(num: int) -> int:
            if num == 1:
                return 1
            else:
                result = num * factorial(num-1)
                return result
        if m == 1 or n == 1:
            result = 1
        else:
            result = int(factorial(m+n-2)/(factorial(m-1)*factorial(n-1)))
        return result
