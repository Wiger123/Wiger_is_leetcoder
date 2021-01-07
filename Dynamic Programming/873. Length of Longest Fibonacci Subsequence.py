class Solution(object):
    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        '''
        思路:
        dp[i][j]: 以倒数第二位 arr[i] 最后一位 arr[j] 的子序列长度
        ---
        转移方程: 
        1. arr[j] - arr[i] 不在数组中, 即 i 为第一项, j 为第二项
            dp[i][j] = 2
        2. arr[j] - arr[i] 在数组中, 位置为 k
            dp[i][j] = dp[k][i] + 1
        ---
        边界条件:
        ---
        时间复杂度: O(n^2) : 两层遍历完成计算
        空间复杂度: O(n^2) : 转移矩阵占用空间
        ---
        难点:
        1. 采用 hash 表的存储结构
        2. 判断 arr[j] - arr[i] 是否在数组中, 并且需要结果的数值小于 arr[i]
        '''
        # 数组长度
        n = len(arr)

        # 数组转化集合
        arr_set = set(arr)

        # 初始化矩阵
        dp = [[1] * n for _ in range(n)]

        # 记录最大长度
        max_len = 1

        # 外层遍历: 倒数第二位 i: 0 -- n - 2
        for i in range(n - 1):
            # 内层遍历: 倒数第一位 j: i + 1 -- n - 1
            for j in range(i + 1, n):
                # 判断 arr[j] - arr[i] 是否在数组中
                # 并且需要结果的数值小于 arr[i]              
                if arr[j] - arr[i] in arr_set and 2 * arr[i] > arr[j]:
                    # 元素位置
                    k = arr.index(arr[j] - arr[i])

                    # 状态转移方程
                    dp[i][j] = dp[k][i] + 1
                    
                    # 更新最大长度
                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
                
                # 不在数组中则作为新的数列起始
                else:
                    dp[i][j] = 2

        # max_len == 1 即不存在斐波拉契数列
        max_len = 0 if max_len == 1 else max_len

        # 返回最大值
        return max_len
