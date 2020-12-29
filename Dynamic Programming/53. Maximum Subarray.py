class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        思路:
        dp[i]: 以 nums[i] 结尾的最大子数组和
        ---
        转移方程:
        dp[i] = max(nums[i], nums[i] + dp[i - 1])
        ---
        边界条件:
        dp[0] = nums[0]
        ---
        时间复杂度: O(n) : 只需遍历一次数组
        空间复杂度: O(1) : 只需建立一个大小为常数的空间
        ---
        难点:
        '''
        # 数组为空或长度为一直接返回
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
    
        # 初始化
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        # 遍历数组
        for i in range(1, n):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
        
        # 返回结果
        return max(dp)
