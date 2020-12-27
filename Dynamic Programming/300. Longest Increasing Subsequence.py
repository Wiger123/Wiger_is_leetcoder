class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        思路: 
        dp[i]: 以 num[i] 结尾的最长递增子序列长度
        ---
        转移方程:
        dp[i] = max(dp[k]) + 1 nums[k] < nums[i]
        ---
        边界条件:
        dp[0] = 1
        ---
        时间复杂度: O(n^2) : 只需遍历一次数组
        空间复杂度: O(n) : 只需建立一个与字符串长度相同的数组
        ---
        难点:
        '''
        # 数组长度
        n = len(nums)

        # 长度为 1 直接返回
        if n == 1:
            return 1

        # 初始化 dp 数组
        dp = []

        # 自下而上(迭代)
        for i in range(n):
            dp.append(1)
            for j in range(i):
                # 转移方程
                if nums[j] < nums[i]:
                    # 取 dp[i] 和 dp[j] + 1 中的较大值
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # 返回 dp 数组中最大值
        return max(dp)
