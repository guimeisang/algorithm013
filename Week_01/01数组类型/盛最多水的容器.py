# 双指针解法
# 通过两个指针不断地移动，但是需要注意的就是 水量计算规则和如何移动i，j的规则需要好好理解下！
# 发现国际站写的还是更加的简介，虽然只是减少了一行代码；高赞下的都写的很简洁

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, res = 0, len(height) -1, 0
        while i < j:
            res = max(res, (j - i)) * min(height[i], height[k]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res

# 创建一个对象
solu = Solution()

print(solu.maxArea([1,1,1,2,3,4,5]))

                