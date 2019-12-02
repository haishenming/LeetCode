#给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
#因为 nums[0] + nums[1] = 2 + 7 = 9
#所以返回 [0, 1]
#
# Related Topics 数组 哈希表



#leetcode submit region begin(Prohibit modification and deletion)
from typing import List

class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        """ 暴力求解
         循环遍历nums所有元素，找到target

         时间复杂度： n^2
         """

        l = len(nums)

        for i in range(l):
            for j in range(l):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]

        return []

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        """ 哈希表
         使用哈希表缓存结果

         时间复杂度： n
         """
        nt_map = {}
        l = len(nums)
        for i in range(l):
            nt_map[target-nums[i]] = i

        for j in range(l):
            i = nt_map.get(nums[j])
            if i and j != i:
                return [j, i]

        return []

    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        """ 哈希表优化
         缓存的同时检查是否匹配

         时间复杂度： n
         """
        nt_map = {}
        l = len(nums)
        for i in range(l):

            k = nt_map.get(nums[i])
            if k is not None:
                return [k, i]
            else:
                nt_map[target-nums[i]] = i

        return []





#leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    nums = [2, 7, 9, 10]

    print(s.twoSum3(nums, 9))

