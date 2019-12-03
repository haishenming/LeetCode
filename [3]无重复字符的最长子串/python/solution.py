# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#
#
# 示例 2:
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#
#
# 示例 3:
#
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
# Related Topics 哈希表 双指针 字符串 Sliding Window


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """ 暴力法 """

        l = []
        maxlen = 0
        for c in s:
            if c in l:
                index = l.index(c)
                l = l[index+1:]

            l.append(c)
            maxlen = max(maxlen, len(l))

        return maxlen


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = Solution()
    print("3", s.lengthOfLongestSubstring("abcabcbb"))
    print("3", s.lengthOfLongestSubstring("dvdf"))
    print("0", s.lengthOfLongestSubstring(""))
    print("1", s.lengthOfLongestSubstring(" "))
