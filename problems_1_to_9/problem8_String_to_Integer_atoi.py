import re


class Solution:
    @staticmethod
    def myAtoi(str1: str) -> int:
        """
        Problem 8: String to Integer (atoi)
        :param str1:
        :return:
        """
        int_value = 0
        str1 = str1.lstrip()
        a = re.findall(r'(^[-+]?\d*)\s?', str1)
        if len(a) > 0:
            try:
                int_value = int(a[0])
            except ValueError:
                return 0
        if int_value < -2 ** 31:
            int_value = -2 ** 31
        elif int_value >= 2 ** 31:
            int_value = 2 ** 31 - 1
        return int_value


if __name__ == '__main__':
    print(Solution.myAtoi('words and 987'))
    print(Solution.myAtoi('-42'))
    print(Solution.myAtoi('    42'))
