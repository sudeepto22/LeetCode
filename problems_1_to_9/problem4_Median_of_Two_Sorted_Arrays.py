class Solution:
    @staticmethod
    def findMedianSortedArrays(nums1: list, nums2: list) -> float:
        """
        Problem 4: Median of Two Sorted Arrays

        :param nums1: list
        :param nums2: list

        :return median: float
        """
        median_index = (len(nums1)+len(nums2))//2
        flag = True
        if (len(nums1)+len(nums2)) % 2 == 0:
            flag = False
        l1 = l2 = 0
        r1, r2 = len(nums1), len(nums2)
        i = 0
        sorted_list = []
        while l1 < r1 and l2 < r2 and i <= median_index:
            if nums1[l1] < nums2[l2]:
                sorted_list.append(nums1[l1])
                l1 += 1
            else:
                sorted_list.append(nums2[l2])
                l2 += 1
            i += 1
        while l1 < r1 and i <= median_index:
            sorted_list.append(nums1[l1])
            l1 += 1
            i += 1
        while l2 < r2 and i <= median_index:
            sorted_list.append(nums2[l2])
            l2 += 1
            i += 1
        if flag:
            return sorted_list[-1]
        return (sorted_list[-1]+sorted_list[-2])/2


if __name__ == '__main__':
    print(Solution.findMedianSortedArrays([2, 3, 6, 9], [5, 7, 8, 10]))
