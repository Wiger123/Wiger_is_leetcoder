class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        '''
        思路:
        考虑行数远大于列数, 将 n * m 的 matrix 数组从第 i 列到第 j 列的每一行求和, 形成长度为 n 的 nums 数组, 再对 nums 数组求不超过 k 的最大子序列 max, 过程中每次计算以第 l 行为止的最大子矩阵
        第一种情况: max <= k 直接满足; 第二种情况: max > k 这里需要暴力, 目前暴力思路是: nums 数组从第 l 行加到第 0 行, 逐行计算结果
        ---
        转移方程:
        dp[i] = max(nums[i], nums[i] + dp[i - 1])
        ---
        边界条件:
        dp[0] = nums[0]
        ---
        时间复杂度: O(n^2 * m^2) : 起始行与结束行遍历两层, 每一列进行遍历
        空间复杂度: O(m) : 一行的数值进行求和
        ---
        难点:
        1. 由于行数远大于列数, 外层 i 跑 10 次, 内层 j 跑 10000 次, 对 j 需要定义 10 次, 舍弃 10 次, 用时较少, 而反过来, 对 j 定义 10000 次, 占用内存不同, 故之前对列求和转化为对行求和
        '''
        # 矩阵初始化
        n = len(matrix)
        m = len(matrix[0])

        # 最大值初始化
        max_dp = float('-inf')

        # 外层遍历: 第 i 列开始
        for i in range(m):
            # 起始列改变, 才需要初始化 nums 数组, 不修改起始列时, 每加一列, 只需在原有基础上加一个元素就可以
            nums = [0] * n

            # 内层遍历: 第 j 列结束
            for j in range(i, m):
                # 初始化 dp: dp[l - 1] = 0
                dp = 0

                # 每一行进行计算, 以第 l 行结尾的矩阵数值
                for l in range(n):
                    # 当前行数值
                    nums[l] += matrix[l][j]

                    # 判断 dp[l - 1] 是否大于 0
                    if dp <= 0:
                        dp = nums[l]
                    else:
                        dp += nums[l]
                    
                    # 结合矩阵最大值进行阈值判断, 若满足则无需进行暴力判断
                    if dp >= max_dp and dp <= k:
                        max_dp = dp

                    # 若 dp >= max_dp 但超过了最大值, 此时只能每次加上前面每一行逐行判断
                    elif dp >= max_dp and dp > k:
                        # 逐行行相加和
                        row_sum = 0

                        # 逐行更新
                        for p in range(l, -1, -1):
                            row_sum += nums[p]

                            # 阈值判断
                            if row_sum >= max_dp and row_sum <= k:
                                max_dp = row_sum
    
                    # 若 dp < max_dp, 即当前矩阵最大值仍无法更新全局最大值, 无需进行暴力搜索
                    
        # 返回不超过 k 的最大值
        return max_dp
