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
        max_ans = ""
        
        # 初始化最大长度, 随时记录用于减少初始化结果替换次数
        max_len = 0
        
        # 计算顺序应该是: (0,0) -> (1,1) -> (2,2) -> (3,3) -> (n-1,n-1) -> (0,1) -> (1,2) -> (2,3) -> (n-2,n-1) -> ... -> (0,n-2) -> (1,n-1) -> (0,n-1)
        # 如果用图像显示出来, 大致是通过来回的折线访问了半个三角形
        # 外层循环: 结束位置减去起始位置从 0 到 n - 1, 长度等于该数值 + 1
        for l in range(n):
            # 内层循环: 起始横坐标从 0 到 n - l - 1
            for i in range(n - l - 1):
                # 判断是否满足边界条件 1
                if l == 0:
                    dp[i][i + l] = True
                    # 跳过本次循环
                    continue
                    
                # 判断是否满足边界条件 2
                if l == 1:
                    # 判断相邻两个字符是否相同
                    if s[i] == s[i + l]:
                        dp[i][i + l] = True
                    # 跳过本次循环
                    continue

                # 非边界条件, 转移方程生效
                dp[i][i + l] = dp[i + 1][i + l - 1] and s[i] == s[i + l - 1]
                
                # 判断当前长度是否替换最大长度
                if dp[i][i + l] and l > max_len:
                    max_ans = s[i:i + l + 1]
                    max_len = l
        
        # 返回最终结果
        return max_ans
