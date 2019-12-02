//给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
//
// 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
//
// 示例:
//
// 给定 nums = [2, 7, 11, 15], target = 9
//
//因为 nums[0] + nums[1] = 2 + 7 = 9
//所以返回 [0, 1]
//
// Related Topics 数组 哈希表

package main

import "fmt"

//leetcode submit region begin(Prohibit modification and deletion)
func twoSum(nums []int, target int) []int {
	// hash

	h := make(map[int]int)
	for i, n := range nums {
		h[target-n] = i
	}

	for j, n := range nums {
		if i, ok := h[n]; ok && i != j {
			return []int{j, i}
		}
	}

	return []int{}

}

func twoSum2(nums []int, target int) []int {
	// hash 优化，缓存一次

	h := make(map[int]int)
	for i, n := range nums {
		if j, ok := h[n]; ok && i != j {
			return []int{j, i}
		}

		h[target-n] = i
	}

	return []int{}

}

//leetcode submit region end(Prohibit modification and deletion)

func main() {
	nums := []int{2, 7, 11, 15}
	target := 9
	fmt.Println(twoSum2(nums, target))

}
