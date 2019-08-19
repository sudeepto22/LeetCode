class Solution:
    @staticmethod
    def romanToInt(s: str) -> int:
        """
        Problem 13: Roman To Integer

        :param s: str

        :return roman_to_int: int
        """
        romans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        i = len(s) - 1
        right_char = ''
        num = 0
        while i >= 0:
            if s[i] == 'I' and right_char in ['V', 'X'] \
                    or s[i] == 'X' and right_char in ['L', 'C'] \
                    or s[i] == 'C' and right_char in ['D', 'M']:
                num -= romans[s[i]]
            else:
                num += romans[s[i]]
            right_char = s[i]
            i -= 1
        return num


if __name__ == '__main__':
    print(Solution.romanToInt('MCMXCIV'))
