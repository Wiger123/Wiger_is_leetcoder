class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        '''
        思路: 
        通过动态规划将 s 字符串的前 i 位与 p 字符串的前 j 位进行匹配, 最后通过判断 s, p 字符串最后一位是否匹配确定整个表达式是否可以匹配
        这里说明: "." 可以视作一个特殊字母, 可以将 "." 与字母一起考虑
        1. p[j] = abc: s[i] == p[j], 可以同时去掉两个字符, 考察 s 字符串的前 i - 1 位与 p 字符串的前 j - 1 位是否匹配
           p[j] = abc: s[i] != p[j], 直接判定为 False

        2. 记 "*" 表示 k 个字符
           2.1. 当 k = 0 时
                记作: P(i, j) = P(i, j - 2) s[i] != p[j - 1] 此时 "*" 表示零个字符

           2.2. 当 k >= 1 时
                p[j] = "*", p[j - 1] = abc: "*" 表示 0 个字符时, 考察 s 字符串的前 i 位与 p 字符串的前 j - 2 位是否匹配           转移方程是: P(i, j) = P(i, j - 2)
                p[j] = "*", p[j - 1] = abc: "*" 表示 1 个字符时, 考察 s 字符串的前 i - 1 位与 p 字符串的前 j - 2 位是否匹配       转移方程是: P(i, j) = P(i - 1, j - 2) s[i] == p[j - 1]
                p[j] = "*", p[j - 1] = abc: "*" 表示 2 个字符时, 考察 s 字符串的前 i - 2 位与 p 字符串的前 j - 2 位是否匹配       转移方程是: P(i, j) = P(i - 2, j - 2) s[i] == s[i - 1] == p[j - 1]
                ...
                p[j] = "*", p[j - 1] = abc: "*" 表示 k 个字符时, 考察 s 字符串的前 i - k 位与 p 字符串的前 j - 2 位是否匹配       转移方程是: P(i, j) = P(i - k, j - 2) s[i] == s[i - 1] == ... == s[i - k] == p[j - 1]
                这种写法极为复杂, 换个类似于马尔可夫的思路, "*" 表示 k 个字符时(k > 1), 且 s[i] == p[j - 1], 去掉 s 的第 i 个字符, 比较 s 的前 i - 1 个字符是否与 p 的前 j 个字符匹配, 这样转移方程仅仅与上一个字符的匹配状态相关
                记作: P(i, j) = P(i - 1, j) s[i] == p[j - 1] 此时 "*" 表示多个字符

        动态规划:
            1. 定义函数 P(i, j):  s 字符串的前 i 位与 p 字符串的前 j 位是否可以匹配
            2. 转移方程:
                2.1. p[j] == abc / ".": P(i, j) = P(i - 1, j - 1)                  matches(s[i], p[j])
                     p[j] == abc / ".": P(i, j) = False                            !matches(s[i], p[j])

                2.2. p[j] == "*": P(i, j) = P(i, j - 2)                            !matches(s[i], p[j - 1])                                                   此时 "*" 表示 0 个字符
                     p[j] == "*": P(i, j) = P(i - 1, j) or P(i, j - 2)             matches(s[i], p[j - 1])                                                    此时 "*" 表示 >= 1 个字符

            3. 边界条件: P(0, 0) = True
        ---
        时间复杂度: O(m * n) : m 和 n 分别是字符串 s 和 p 的长度
        空间复杂度: O(m * n) : 存储所有状态使用的空间
        ---
        难点:
        0. 在字符串前面空一格初始化!!!!!!!
        1. 转移方程 4 种情况比较复杂
        2. "." 应归类于字母一并考虑
        3. 转移方程 2.2 类似于马尔可夫的思路比较难想
        4. 转移方程 2.2 需要对 "*" 表示 0, 多个字符进行分别考虑, 1 个字符无需考虑
        5. dp 两个维度 + 1 便于计算
        '''

        # 判断 s 的第 i 个字符(s[i - 1])与 p 的第 j 个字符(p[j - 1])是否满足匹配条件
        def matches(i, j):
            '''
            i: s 的第 i 个字符
            j: p 的第 j 个字符
            '''
            
            # 当 i = 0 时, 没有单个字符可以匹配
            if i == 0:
                return False
            
            # 当 p[j - 1] 为 "." 时, 可以匹配一切非空字符
            if p[j - 1] == ".":
                return True
            
            # 其余情况只需判断 s[i - 1] 是否等于 p[j - 1]
            return s[i - 1] == p[j - 1]
            
        # 字符串长度
        m, n = len(s), len(p)
        
        # 初始化转移数组
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # 边界条件
        dp[0][0] = True
        
        # 外层循环: 对 s 字符串的前 0 - m 个字符进行匹配, 0 个字符表示 s 为空字符串
        # i: s 的第 i 个字符
        for i in range(m + 1):
            # 内层循环: 对 p 字符串的前 1 - n 个字符进行匹配, 当 p 也为空字符串时, dp[0][0] 即可表示, 直接返回 True, 且当 p 长度为 0 时, 显然无法匹配任何非空的字符串 s, 因此无需遍历 j = 0 的情况
            # j: p 的第 j 个字符
            for j in range(1, n + 1):
                # 判断 p 的第 j 个字符(p[j - 1])是否为 "*"
                if p[j - 1] == "*":
                    # 此时 "*" 可以表示 k 个字符
                    # 通过 s[i] 与 p[j - 1] 匹配判断 k 的实际数目
                    # k = 0: dp[i][j] = dp[i][j - 2] 即去掉 p 的 j - 1 和 j 两位, 对前面的字符进行匹配
                    # k > 0: dp[i][j] = dp[i - 1][j] 即去掉 s 的 i 位字符, 对前面的字符进行匹配
                    # 转移方程的传递关系为: dp[i][j - 2] -> dp[i][j] -> dp[i + 1][j] -> dp[i + 2][j] -> ... -> dp[i + k][j]
                    # 默认为匹配 0 个字符
                    dp[i][j] = dp[i][j - 2]
                    # 当满足匹配规则, 即匹配数目 > 0, 修正转移方程
                    if matches(i, j - 1):
                        # 考虑到上面的赋值 dp[i][j - 2] = True, 然而 dp[i - 1][j] = False, 这里需要用到 or 进行整体判断
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                        
                # p[j - 1] 为字母和 "."   
                else:
                    # 若当前字符匹配转移方程为: dp[i][j] = dp[i - 1][j - 1]
                    if matches(i, j):
                        dp[i][j] = dp[i - 1][j - 1]
                    # 其他情况为 False
                    else:
                        dp[i][j] = False
        
        # 返回最终结果
        return dp[m][n]
