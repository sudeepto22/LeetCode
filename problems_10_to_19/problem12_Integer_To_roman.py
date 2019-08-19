class Solution:
    @staticmethod
    def intToRoman(num: int) -> str:
        """
        Problem 12: Integer To Roman

        :param num: int

        :return roman: str
        """
        values = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        i = 0
        roman = []
        while num > 0:
            if num >= nums[i]:
                roman.append(values[i])
                num -= nums[i]
            else:
                i += 1
        return "".join(roman)


if __name__ == '__main__':
    print(Solution().intToRoman(356))
