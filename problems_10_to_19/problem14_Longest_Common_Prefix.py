class Solution:
    @staticmethod
    def longestCommonPrefix(strs: list) -> str:
        """
        Problem 14: Longest Common Prefix
        
        :param strs: list
        
        :return longest_common_prefix: str 
        """
        if len(strs) == 0:
            return ""
        flag = True
        longest_common_prefix = min(strs, key=lambda x: len(x))
        for i in range(len(longest_common_prefix)):
            for j in strs:
                if j[i] != longest_common_prefix[i]:
                    flag = False
                    break
            if not flag:
                longest_common_prefix = longest_common_prefix[:i]
                break
        return longest_common_prefix


if __name__ == '__main__':
    print(Solution.longestCommonPrefix(["flower", "flow", "flight"]))
