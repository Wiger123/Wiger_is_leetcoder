class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        思路:
        dp[i]: 以 nums[i] 结尾的最长递增子序列长度
        counts[i]: 最长长度为 i 的子序列个数
        ---
        转移方程:
        if k < i and nums[k] < nums[i]:
            dp[i] = max(dp[k]) + 1 
            counts[i] = counts[k] / counts[i] += count[k]
        
        例如:
        i     0 1 2 3 4 5
        nums  1 3 5 0 8 2
        dp    1 2 3 1 4 2
        count 1 1 1 1 1 2
        
        i = 3: 由于以 nums[3] 无法构成最长字符串, count[3] = 1 不变
        i = 4: nums[4] 比前面的 i = 0, 1, 2 大, dp[i]: 1 -> 2 -> 3 -> 4, count[i]: 1 -> 1 -> 1 -> 1
        i = 5: dp[i]: 1 -> 2 -> 2, count[i]: 1 -> 1 -> 2
        ---
        边界条件:
        ---
        时间复杂度: O(n^2) : 只需遍历一次数组
        空间复杂度: O(n) : 只需建立一个与字符串长度相同的数组
        ---
        难点:
        '''
        # 数组长度
        n = len(nums)
        
        # 长度为 0 和 1 时序列个数为 0 和 1
        if n <= 1:
            return n

        # 状态数组和子序列个数
        dp = [0] * n
        counts = [1] * n

        # 外层遍历: 整个数组
        for j, num in enumerate(nums):
            # 内层遍历: 从 0 到 j
            for i in range(j):
                # 找到最长数组
                if nums[i] < nums[j]:
                    # 长度大于则替换
                    if dp[i] >= dp[j]:
                        dp[j] = 1 + dp[i]
                        counts[j] = counts[i]
                    # 长度相同则相加
                    elif dp[i] + 1 == dp[j]:
                        counts[j] += counts[i]
                        
        # 返回最终结果
        longest = max(dp)
        return sum(c for i, c in enumerate(counts) if dp[i] == longest)
