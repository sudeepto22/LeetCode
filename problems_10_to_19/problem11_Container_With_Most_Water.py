class Solution:
    @staticmethod
    def maxArea(height: list) -> int:
        """
        Problem 11: Container With Most Water

        :param height: list

        :return max_area: int
        """
        low = 0
        high = len(height)-1
        max_area = 0
        while low < high:
            max_area = max(max_area, (high-low)*min(height[low], height[high]))
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
        return max_area


if __name__ == '__main__':
    print(Solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
