class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        思路:
        数组从小到大排序, 计算每个元素出现个数乘以元素数值的结果, 相邻元素不能同时取, 问题转化为打家劫舍
        dp[i]: 前 i 间房屋能偷窃到的最高总金额
        dp[i] = max(dp[j]) + nums[i]  i - 1 > j
        ---
        转移方程:
        dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i]
        ---
        边界条件:
        dp[0] = count[0]
        dp[1] = count[1]
        ---
        时间复杂度: O(n) : 多次遍历
        空间复杂度: O(1) : 常数值
        ---
        难点:
        1. 建立数组统计每个元素出现次数
        '''
        # 元素个数
        n = len(nums)

        # 空数组返回 0
        if n == 0:
            return 0

        # 数组最大数值
        max_num = max(nums)

        # 初始化辅助数组, 长度为数组最大值加 1
        count = [0] * (max_num + 1)

        # 遍历数组, 统计元素出现个数
        for i in range(n):
            count[nums[i]] += 1
        
        # 打家劫舍问题, 此时只需考虑 count 数组, 初始化 dp[i - 2] 和 dp[i - 1]
        dp_2, dp_1 = count[0], count[1]

        # 遍历获取最大值
        for i in range(2, max_num + 1):
            dp_2, dp_1 = dp_1, max(count[i] * i + dp_2, dp_1)

        # 返回最终结果
        return dp_1
