class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = str(x)
        l = 0
        r = len(number) - 1
        while l < len(number) - 1 and r > 0:
            if number[l] != number[r]:
                return False    
            l += 1
            r -= 1

        return True
