from typing import List


class Solution:
    @staticmethod
    def threeSumClosest(nums: List[int], target: int) -> int:
        """
        Problem 16: 3Sum Closest

        :param nums: List[int]
        :param target: int

        :return closest_sum: int
        """
        nums.sort()
        if len(nums) < 3:
            return
        closest_sum = sum(nums[0:3])
        diff = abs(closest_sum - target)
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k and i < k:
                three_sum = nums[i] + nums[j] + nums[k]
                if three_sum - target == 0:
                    return three_sum
                elif three_sum - target < 0:
                    j += 1
                else:
                    k -= 1
                if abs(three_sum - target) < diff:
                    diff = abs(three_sum - target)
                    closest_sum = three_sum
        return closest_sum


if __name__ == '__main__':
    print(Solution.threeSumClosest([-1, 2, 1, -4], 1))

