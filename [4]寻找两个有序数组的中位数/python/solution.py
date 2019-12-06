# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
#
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
#
# 你可以假设 nums1 和 nums2 不会同时为空。
#
# 示例 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# 则中位数是 2.0
#
#
# 示例 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# 则中位数是 (2 + 3)/2 = 2.5
#
# Related Topics 数组 二分查找 分治算法


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1
        nums.extend(nums2)
        nums.sort()

        l = len(nums)

        if l % 2 == 0:
            return (nums[int(l / 2)] + nums[int(l / 2 - 1)]) / 2
        else:
            return float(nums[int(l/2)])



# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2]
    nums2 = [3]
    print(s.findMedianSortedArrays(nums1, nums2))
