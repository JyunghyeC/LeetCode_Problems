class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed_num = 0
        num = x

        while num != 0:
            remainder = num % 10
            reversed_num = reversed_num * 10 + remainder
            num //= 10

        return reversed_num == x

