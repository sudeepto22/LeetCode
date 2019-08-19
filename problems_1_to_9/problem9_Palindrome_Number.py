import math


class Solution:
    @staticmethod
    def isPalindrome(x: int) -> bool:
        """
        Problem 9: Palindrome Number

        :param x: int

        :return is_palindrome: bool
        """
        if x < 0:
            return False
        elif x == 0:
            return True
        temp = x
        multiplier = int(math.log(temp, 10))
        new_num = 0
        while temp > 0:
            rem = temp % 10
            temp //= 10
            new_num += 10**multiplier*rem
            multiplier -= 1
        return x == new_num


if __name__ == '__main__':
    print(Solution.isPalindrome(23532))
    print(Solution.isPalindrome(2353))

