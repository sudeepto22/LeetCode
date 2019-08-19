import math


class Solution:
    @staticmethod
    def reverse(x: int) -> int:
        """
        Problem 7: Reverse Integer

        :param x: int

        :return reverse_x: int
        """
        if x <= -2 ** 31 or x >= 2 ** 31 - 1 or x == 0:
            return 0
        flag = False
        if x < 0:
            x *= -1
            flag = True
        temp = x
        multiplier = int(math.log(temp, 10))
        rev_num = 0
        while temp > 0:
            rem = temp % 10
            temp //= 10
            rev_num += 10 ** multiplier * rem
            multiplier -= 1
        if rev_num >= 2 ** 31 - 1 or rev_num <= -2 ** 31:
            return 0
        if flag:
            return rev_num * -1
        return rev_num


if __name__ == '__main__':
    print(Solution.reverse(43621))
    print(Solution.reverse(-43621))
    print(Solution.reverse(0))

