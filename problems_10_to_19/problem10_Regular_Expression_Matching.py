import re


class Solution:
    @staticmethod
    def isMatch(s: str, p: str) -> bool:
        """
        Problem 10: Regular Expression Matching

        :param s: str
        :param p: str

        :return is_match: bool
        """
        if len(re.findall(p, s)) == 0:
            return False
        return re.findall(p, s)[0] == s


if __name__ == '__main__':
    print(Solution.isMatch('aa', '.*'))
    print(Solution.isMatch('aa', '.*c'))
