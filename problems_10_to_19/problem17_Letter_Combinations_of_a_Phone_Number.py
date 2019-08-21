import time
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Problem 17: Letter Combinations of a Phone Number

        :param digits: str

        :return all_combination_list: List[str]
        """
        keypad = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res = []

        def find_combinations(local_word, index):
            current_str = keypad[int(digits[index]) - 2]

            for i in range(len(current_str)):
                local_word += current_str[i]
                if index == len(digits) - 1:
                    res.append(local_word)
                else:
                    find_combinations(local_word, index + 1)
                local_word = local_word[:-1]

        if len(digits) != 0:
            find_combinations('', 0)
        return res

    def letterCombinations_method2(self, digits: str) -> List[str]:
        """
        Problem 17: Letter Combinations of a Phone Number

        :param digits: str

        :return all_combination_list: List[str]
        """
        keypad = {'1': [],
                  '2': ['a', 'b', 'c'],
                  '3': ['d', 'e', 'f'],
                  '4': ['g', 'h', 'i'],
                  '5': ['j', 'k', 'l'],
                  '6': ['m', 'n', 'o'],
                  '7': ['p', 'q', 'r', 's'],
                  '8': ['t', 'u', 'v'],
                  '9': ['w', 'x', 'y', 'z']}
        output = []

        def backtrack(combination: str, next_digits: str):
            if len(next_digits) == 0:
                output.append(combination)
            else:
                for letter in keypad[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])

        if digits:
            backtrack("", digits)
        return output


if __name__ == '__main__':
    print(Solution().letterCombinations("23"))
    print(Solution().letterCombinations_method2("23"))
