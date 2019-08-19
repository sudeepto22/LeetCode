from typing import List


class Solution:
    @staticmethod
    def threeSum(nums: List[int]) -> List[List[int]]:
        """
        Problem 15: 3Sum

        :param nums: List[int]

        :return three_sum_list: List[List[int]]
        """
        if len(nums) < 3:
            return []
        if set(nums) == {0}:
            return [[0, 0, 0]]
        nums.sort()
        three_sum_list = []

        for i in range(len(nums)):
            j = i + 1
            k = len(nums)-1
            while j < k and i < k:
                three_sum = nums[i] + nums[j] + nums[k]
                if three_sum == 0:
                    three_sum_list.append([nums[i], nums[j], nums[k]])
                    j += 1
                elif three_sum < 0:
                    j += 1
                else:
                    k -= 1
        return list(list(x) for x in list(set(tuple(x) for x in three_sum_list)))


if __name__ == '__main__':
    print(Solution.threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]))
