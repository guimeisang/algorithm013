# 题目：
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

# 示例:

# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]

# 思路：1. 双指针的方式，当为0的时候，i 会往一直前走，但是i 不为零的时候，就会进行替换，并且j也往前面走；
# 但是i 为零的时候，i会往前面走，但是不置换，j也不会往前面走，在那边等i找到非零的数

class Solution(object):
    def moveZeroes(self, nums):
        """
		:type nums: List[int]
		:rtype: None Do not return anything, modify nums in-place instead.
		"""
        if not nums:
            return 0
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1         
        print(nums)


solu = Solution()
solu.moveZeroes([0,1,0,1,0,3])