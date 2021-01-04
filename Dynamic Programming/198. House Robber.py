class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        思路:
        dp[i]: 前 i 间房屋能偷窃到的最高总金额
        dp[i] = max(dp[j]) + nums[i]  i - 1 > j
        ---
        转移方程:
        dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i]
        ---
        边界条件:
        dp[0] = nums[0]
        dp[1] = nums[1]
        ---
        时间复杂度: O(n) : 一次遍历
        空间复杂度: O(1) : 常数值
        ---
        难点:
        1. 容易想到的思路是: dp[i]: 偷第 i 家情况下最多能偷到的价值, 代码不够简洁, 需要对前 3 位进行考虑, 改成题解思路: dp[i]: 前 i 间房屋能偷窃到的最高总金额, 较为简洁
        '''

        # 长度
        n = len(nums)
        
        # n = 0, 1 直接返回
        if n == 0:
            return 0

        if n == 1:
            return nums[0]
        
        # 初始化第 1 个第 2 个前可以投到的最大值
        first, second = nums[0], max(nums[0], nums[1])

        # 因为都是正数, nums[i] + first 总会越来越多, 只需要和 second 做比较即可
        for i in range(2, n):
            first, second = second, max(first + nums[i], second)
        
        return second
       
       class Solution(object):
----------------------------------------------------------------------------------------
def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        思路:
        i - 1 > j
        dp[i] = max(dp[j]) + nums[i]
        ---
        转移方程:
        dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i]
        ---
        边界条件:
        dp[0] = nums[0]
        dp[1] = nums[1]
        ---
        时间复杂度: O(n) : 一次遍历
        空间复杂度: O(1) : 常数值
        ---
        难点:
        '''

        # 长度
        n = len(nums)

        # 数组仅 0 1 2 个直接返回
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums)

        # 动态规划数组初始化
        dp_3 = nums[0]
        dp_2 = nums[1]
        dp_1 = nums[2] + nums[0]
        dp = 0

        # 数组最大值
        max_dp = max(dp_3, dp_2, dp_1)

        # 数组长度为 3 直接返回
        if n == 3:
            return max_dp

        # 从第四个数开始遍历
        for i in range(3, n):
            dp = max(dp_3, dp_2) + nums[i]
            dp_3 = dp_2
            dp_2 = dp_1
            dp_1 = dp

            # 更新最大值
            if dp > max_dp:
                max_dp = dp

        # 返回最大结果
        return max_dp
