class Solution(object):
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        """
        Problem 3: Longest Substring Without Repeating Characters

        :param s: str

        :return max_length: int
        """
        str_list = []
        max_length = 0

        for x in s:
            if x in str_list:
                str_list = str_list[str_list.index(x) + 1:]

            str_list.append(x)
            max_length = max(max_length, len(str_list))

        return max_length


if __name__ == '__main__':
    print(str(Solution.lengthOfLongestSubstring('dvdf')))
