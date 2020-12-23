class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''
        思路: 
        通过动态规划找到文中所有回文串的起始和中止位置, 选择最长段落的作为结果
        动态规划:
            1. 定义函数 P(i, j): 从字符串第 i 个到第 j 个字符是否构成回文串
            2. 转移方程: P(i, j) = P(i + 1, j - 1) && Si == Sj
            3. 边界条件: 长度为 1 : P(i, i) = true; 长度为 2 : P(i, i + 1) = (Si == Si+1)
        ---
        时间复杂度: O(n^2) : 双层嵌套, 每层均从第一个字符遍历到最后一个字符
        空间复杂度: O(n^2) : i, j 构成 n * n数组
        '''

        # 初始化字符串总长度
        n = len(s)

        # 初始化函数
        dp = [[False] * n for i in range(n)]

        # 初始化结果
        ans = ""

        # 外层嵌套遍历 P(i, 0:n)
        for i in range(n):
            # 内层嵌套遍历 P(i + 1:n, j)
            for j in range(i, n):
                # 判断是否满足边界条件 1
                if j == i:
                    dp[i][j] = True

                # 判断是否满足边界条件 2
                elif j == i + 1:
                    # 判断相邻两个字符是否相同
                    if s[j] == s[i]:
                        dp[i][j] = True

                # 非边界条件, 转移方程生效
                else:
                    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]

