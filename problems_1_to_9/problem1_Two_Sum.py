class Solution:
    @staticmethod
    def twoSum(nums: list, target: int) -> list:
        """
        Problem 1: Two Sum

        :param nums: list
        :param target: int

        :return indices_list: list
        """
        for i in range(len(nums)):
            s = target - nums[i]
            if s in nums and nums.index(s) != i:
                return sorted([i, nums.index(s)])
        return []


if __name__ == '__main__':
    print(Solution.twoSum([12, 34, 54, 32, 67, 86, 54, 13, 76], 25))
