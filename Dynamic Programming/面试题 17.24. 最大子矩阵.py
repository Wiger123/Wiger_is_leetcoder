class Solution(object):
    def getMaxMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        '''
        思路:
        将 n * m 的 matrix 数组从第 i 行到第 j 行的每一列求和, 形成长度为 m 的 nums 数组, 再对 nums 数组求最大子序列, 记录 i j 和最大子序列的起始结束位置即可
        ---
        转移方程:
        dp[i] = max(nums[i], nums[i] + dp[i - 1])
        ---
        边界条件:
        dp[0] = nums[0]
        ---
        时间复杂度: O(n^2 * m) : 起始行与结束行遍历两层, 每一列进行遍历
        空间复杂度: O(m) : 一行的数值进行求和
        ---
        难点:
        1. 降维思想: 想到将二维数组的最大子矩阵转化为一维数组的最大子序列问题
        2. 行数 i 和行数 j 的遍历: 循环的控制问题
        3. 记录最大子序列起始和截至位置: 每次更新位置需要记录一次
        4. 起始行改变, 才需要初始化 nums 数组, 不修改起始行时, 每加一行, 只需在原有基础上加一个元素就可以, 否则会超时
        '''
        # 获取数组尺寸
        n = len(matrix)
        m = len(matrix[0])

        # 子矩阵最大值
        max_dp = float('-inf')

        # 起始位置初始化
        max_r1, max_c1, max_r2, max_c2 = 0, 0, 0, 0
        start_c = 0

        # 外层遍历: 第 i 行开始
        for i in range(n):
            # 起始行改变, 才需要初始化 nums 数组, 不修改起始行时, 每加一行, 只需在原有基础上加一个元素就可以
            nums = [0] * m

            # 内层遍历: 第 j 行结束
            for j in range(i, n):
                # 初始化 dp
                dp = 0

                # 每一列进行计算
                for l in range(m):
                    # 当前列数值
                    nums[l] += matrix[j][l]

                    # dp[l - 1] < 0: dp[l] = nums[l]
                    if dp <= 0:
                        dp = nums[l]

                        # 由于此时 dp[i] 独立成字串, 起始位置改变
                        start_c = l

                    # dp[l - 1] > 0: dp[l] = nums[l] + dp[l - 1]    
                    else:
                        dp += nums[l]
                    
                    # 矩阵最大值更新
                    if dp > max_dp:
                        max_dp = dp
                        max_r1 = i
                        max_c1 = start_c
                        max_r2 = j
                        max_c2 = l

        # 返回最终结果
        return [max_r1, max_c1, max_r2, max_c2]
