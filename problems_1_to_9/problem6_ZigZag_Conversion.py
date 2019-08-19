class Solution:
    @staticmethod
    def convert(s: str, num_rows: int) -> str:
        """
        Problem 6: ZigZag Conversion

        :param s: str
        :param num_rows:int

        :return  zig_zag_str: str
        """
        if num_rows == 1:
            return s
        s1 = [""] * num_rows
        i = 0
        j = 0
        while i < len(s):
            s1[j] += s[i]
            i += 1
            if j == num_rows - 1:
                flag = True
            elif j == 0:
                flag = False
            if flag:
                j -= 1
            else:
                j += 1
        return "".join(s1)


if __name__ == '__main__':
    print(Solution.convert('PAYPALISHIRING', 3))
