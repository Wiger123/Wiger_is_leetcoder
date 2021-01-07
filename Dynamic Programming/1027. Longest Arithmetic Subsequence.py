class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        '''
        思路:
        dp[i][j]: 以倒数第二位 A[i] 最后一位 A[j] 的等差数列长度
        ---
        转移方程: 
        1. 2 * A[i] - A[j] 不在数组中, 即 i 为第一项, j 为第二项
            dp[i][j] = 2
        2. 2 * A[i] - A[j] 在数组中, 且元素位置必须位于 i 之前, 位置为 k, 
            dp[i][j] = dp[k][i] + 1
        ---
        边界条件:
        ---
        时间复杂度: O(n^2) : 两层遍历完成计算
        空间复杂度: O(n^2) : 转移矩阵占用空间
        ---
        难点:
        1. 采用 hash 表的存储结构
        2. 判断 2 * A[i] - A[j] 是否在数组中, 且元素位置必须位于 i 之前
        3. 需要找到所有满足条件 2 的元素, 并根据 dp[k][i] 中的最大值加一, 否则当数组中出现重复元素, 结果会变小
        4. 通过一个哈希表记录每个在 i 之前的数出现的最后一个下标, 就可以在 O(1) 的时间内找到 k 所在的下标, 将总体时间 O(n^3) 降为 O(n^2)
        '''
        # 数组长度
        n = len(A)

        # 动态规划数组初始化
        dp = [[1] * n for _ in range(n)]

        # 最大长度
        max_len = 1

        # 建立字典记录在 i 之前的数出现的最后一个下标
        dict = {}

        # 外层循环: 从 0 -- n - 2
        for i in range(n - 1):
            # 内层循环: 从 i -- n - 1
            for j in range(i + 1, n): 
                # 判断是否在数组中, 且元素位置必须位于 i 之前
                k = 2 * A[i] - A[j]
                if k in dict:
                    dp[i][j] = dp[dict[k]][i] + 1

                    # 更新最大长度
                    max_len = max(max_len, dp[i][j])

                # 不在数组中则为初始值
                else:
                    dp[i][j] = 2

                    # 更新最大长度
                    max_len = max(max_len, dp[i][j])
            
            # 加入字典
            dict[A[i]] = i

        # 返回最大值
        return max_len
