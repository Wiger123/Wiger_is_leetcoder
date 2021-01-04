class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        思路:
        dp[i]: 前 i 间房屋能偷窃到的最高总金额
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        此题与 918 环形最大子数组不同, 该题的限制为: 第 1 家与第 n - 1 家最多只能偷 1 家, 即存在 3 种情况, 需分析: 不偷第 1 家, 不偷第 n - 1 家, 两家都不偷 3 种情况即可, 由于两家都不偷实际上包含于前两种情况中, 故实际上只需分析两种情况
        ---
        转移方程:
        dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i]
        ---
        边界条件:
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        ---
        时间复杂度: O(n) : 两次遍历
        空间复杂度: O(1) : 常数值
        ---
        难点:
        '''

        # 数组长度
        n = len(nums)

        # 数组长度为 0 和 1
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]

        # 不偷第一家, dp[n - 2] 与 dp[n - 1] 的初始化
        dp_a_2, dp_a_1 = 0, nums[1]

        # 寻找不偷第一家情况下最大值
        for i in range(2, n):
            dp_a_2, dp_a_1 = dp_a_1, max(dp_a_2 + nums[i], dp_a_1)
        
        # 不偷第 n - 1 家, dp[n - 2] 与 dp[n - 1] 的初始化
        dp_b_2, dp_b_1 = nums[0], max(nums[0], nums[1])

        # 寻找不偷第 n - 1 家情况下最大值
        for i in range(2, n - 1):
            dp_b_2, dp_b_1 = dp_b_1, max(dp_b_2 + nums[i], dp_b_1)
        
        # 返回最大值
        return max(dp_a_1, dp_b_1)
