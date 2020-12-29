class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        '''
        思路:
        dp[i]: 以 nums[i] 结尾的最大子数组和
        考虑到循环, 将数组复制一遍, 即 A = A + A
        ---
        转移方程:
        dp[i] = max(nums[i], nums[i] + dp[i - 1])
        ---
        边界条件:
        dp[0] = nums[i]
        ---
        时间复杂度: O(n ^ 2) : 遍历一次数组, 每次遍历计算 n 个 dp 值
        空间复杂度: O(n) : 只需建立一个大小为 n 的空间
        ---
        难点:
        '''
        # 数组为空或长度为一直接返回
        if not A:
            return 0
        
        if len(A) == 1:
            return A[0]
    
        # 初始化
        n = len(A)

        # 数组扩展
        A = A + A

        # 最大值
        ans = -30001

        # 遍历数组
        for i in range(n):
            # 初始化
            dp = [0] * n
            dp[0] = A[i]
            
            # 对 A[i] 起始的连续 n 个元素进行动态规划计算
            for j in range(i + 1, i + n):
                dp[j - i] = max(A[j], A[j] + dp[j - i - 1])
            
                # 记录当前最大值
                ans = max(ans, dp[j - i])

        # 返回结果
        return ans
