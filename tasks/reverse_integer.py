"""
Task "Reverse Integer"
from LeetCode
"""


class Solution:
    def reverse(self, x: int) -> int:
        """
        Function reverse integer
        >>> Solution.reverse(1, 123)
        321
        >>> Solution.reverse(1, 987654321000)
        123456789
        """
        new_num = 0
        while (x > 0):
            temporary_num = x % 10
            new_num = new_num * 10 + temporary_num
            x = x // 10
        return new_num
