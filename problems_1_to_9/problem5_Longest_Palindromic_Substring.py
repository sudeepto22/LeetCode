class Solution:
    @staticmethod
    def longestPalindrome(s: str) -> str:
        """
        Problem 5: Longest Palindromic Substring (Manacher's Algorithm)

        :param s: str

        :return longest_palindromic_substring: str
        """
        t = "$#"
        for i in s:
            t += i+'#'
        t = t + "@"
        p = [0] * len(t)
        c = 0
        r = 0
        for i in range(len(t)-1):
            mirr = 2 * c - i
            if i < r:
                p[i] = min(r-i, p[mirr])
            while t[i+(1+p[i])] == t[i-(1+p[i])]:
                p[i] += 1
            if i + p[i] > r:
                c = i
                r = i + p[i]
        m = max(p)
        return t[p.index(m)-m+1:p.index(m)+m+1:2]


if __name__ == '__main__':
    print(Solution.longestPalindrome("truemadamer"))
