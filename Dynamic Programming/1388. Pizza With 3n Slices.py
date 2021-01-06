class Solution(object):
    def maxSizeSlices(self, slices):
        """
        :type slices: List[int]
        :rtype: int
        """
        '''
        思路:
        此题与 213 打家劫舍II不同:
        打家劫舍II限制为: 1. 不相邻; 2. 首位不能同时取; 3. 数量上限 n // 2;
        该题的限制为: 1. 不相邻; 2. 首位不能同时取; 3. 数量上限 n // 3;
        加一层块数限制: dp[i][j]: 一共取 j 块的情况下, 在肉饼前 i 块中能取得的最大收益
        这里需要考虑一个数学论证: 任何一种满足上述限制的指定取法都至少有 1 种实现方式
        用数学归纳法可以推出:
        n = 1: 
            3 块肉饼均可选择
        n >= 2: 1 表示要取的数字, 0 表示不取的数字
            先证明: 至少存在一个 1 的一侧有连续两个 0： 若不存在这样的 1, 则所有的 1 之间必然最多只有 1 个 0, 则 1 的数目大于等于 0 的数目, 题目中 1 与 0 的数目应该是 1 : 2, 矛盾, 因此必有一个 1 的单侧有连续两个 0
            取出这样的 1 和相邻的 0 之后, 就会剩下一个 0, 此时剩下待取的 1 之间, 仍然至少有一个 0 进行隔开, 剩余肉饼个数为 3 * (n - 1), 问题规模从 n 减少为 n - 1
        所以不需要考虑细节是按照什么顺序取的, 只需要按照约束条件进行最大化即可
        ---
        转移方程:
        1. 如果我们选择了第 i 个数, 那么第 i - 1 个数不能被选择, 相当于需要在前 i - 2 个数中选择 j - 1 个, 即：
            dp[i][j] = dp[i - 2][j - 1] + slices[i]
        
        2. 如果我们没有选择第 i 个数, 那么需要在前 i - 1 个数中选择 j 个，即：
            dp[i][j] = dp[i - 1][j]
        
        取两者的最大值即为状态转移方程：
            dp[i][j] = max(dp[i − 2][j − 1] + slices[i], dp[i − 1][j])
        ---
        边界条件:
        ---
        时间复杂度: O(n^2) : 外层遍历每个元素考察到第 i 个元素位置最大收益, 内层遍历计算取不同的 j 个肉饼的收益情况
        空间复杂度: O(n^2) : 动态规划数组占用空间, 可以降至 O(n)
        ---
        难点:
        1. 数学归纳法
        2. 分清和打家劫舍的区别
        3. 加一层 dp
        '''

        def maxValue(s):
            # 数组长度
            n = len(s)

            # 需要取出的肉饼块数
            size = n // 3

            # 取 0 或 1 块直接返回结果
            if size == 0:
                return 0
            
            if size == 1:
                return max(s)

            # 初始化状态转移矩阵: dp[i][j]
            # i: 0 -- n
            # j: 0 -- size
            dp = [[0] * (size + 1) for _ in range(n + 1)]

            # 遍历数组: 不取第一个
            for i in range(1, n + 1):
                for j in range(1, size + 1):
                    # 考虑边界溢出的问题
                    if i < 2:
                        # 转移方程
                        dp[i][j] = max(s[i], dp[i − 1][j])        
                    else:
                        # 转移方程
                        dp[i][j] = max(dp[i − 2][j − 1] + s[i], dp[i − 1][j])

            # 返回结果
            return dp[n][size]
        
        # 不取第一块
        ans1 = maxValue(slices[1:])

        # 不取最后一块
        ans2 = maxValue(slices[:-1])
                
        print(ans1)
        print(ans2)

        # 最终结果
        return max(ans1, ans2)
