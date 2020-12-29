class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        思路:
        dp_max[i]: 以 nums[i] 结尾的最大子数组乘积
        dp_min[i]: 以 nums[i] 结尾的最小子数组乘积
        ---
        转移方程:
        dp_max[i] = max(nums[i], nums[i] * dp_max[i - 1], nums[i] * dp_min[i - 1])
        dp_min[i] = max(nums[i], nums[i] * dp_max[i - 1], nums[i] * dp_min[i - 1])
        ---
        边界条件:
        dp[0] = nums[0]
        ---
        时间复杂度: O(n) : 只需遍历一次数组
        空间复杂度: O(1) : 可以只记录 max, min 以及 i - 1 位的连续最大最小乘积, 空间为常数
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
        dp_max = [0] * n
        dp_min = [0] * n
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]

        # 遍历数组
        for i in range(1, n):
            dp_max[i] = max(nums[i], nums[i] * dp_max[i - 1], nums[i] * dp_min[i - 1])
            dp_min[i] = min(nums[i], nums[i] * dp_max[i - 1], nums[i] * dp_min[i - 1])

        # 返回结果
        return max(max(dp_max), max(dp_min))
