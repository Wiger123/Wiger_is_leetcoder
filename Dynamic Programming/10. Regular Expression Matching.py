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
        2. p[j] = "*", p[j - 1] = abc: "*" 表示 0 个字符时, 考察 s 字符串的前 i 位与 p 字符串的前 j - 2 位是否匹配           转移方程是: P(i, j) = P(i, j - 2)
           p[j] = "*", p[j - 1] = abc: "*" 表示 1 个字符时, 考察 s 字符串的前 i - 1 位与 p 字符串的前 j - 2 位是否匹配       转移方程是: P(i, j) = P(i - 1, j - 2) s[i] == p[j - 1]
           p[j] = "*", p[j - 1] = abc: "*" 表示 2 个字符时, 考察 s 字符串的前 i - 2 位与 p 字符串的前 j - 2 位是否匹配       转移方程是: P(i, j) = P(i - 2, j - 2) s[i] == s[i - 1] == p[j - 1]
           ...
           p[j] = "*", p[j - 1] = abc: "*" 表示 k 个字符时, 考察 s 字符串的前 i - k 位与 p 字符串的前 j - 2 位是否匹配       转移方程是: P(i, j) = P(i - k, j - 2) s[i] == s[i - 1] == ... == s[i - k] == p[j - 1]
           这种写法极为复杂, 换个类似于马尔可夫的思路, "*" 表示 k 个字符时(k > 0), 且 s[i] == p[j - 1], 去掉 s 的第 i 个字符, 比较 s 的前 i - 1 个字符是否与 p 的前 j 个字符匹配, 这样转移方程仅仅与上一个字符的匹配状态相关
           记作: P(i, j) = P(i - 1, j) 且 s[i] == p[j - 1]
           考虑到 "*" 表示 0 个字符, P(i, j) = P(i, j - 2) 此时 s[i] == p[j - 1] 和 s[i] != p[j - 1] 均可满足
        3. 匹配函数: 当 s[i] == "." 或 s[i] == p[j]
        动态规划:
            1. 定义函数 P(i, j):  s 字符串的前 i 位与 p 字符串的前 j 位是否可以匹配
            2. 转移方程:
                2.1. p[j] == abc / ".": P(i, j) = P(i - 1, j - 1)                  matches(s[i], p[j])
                     p[j] == abc / ".": P(i, j) = False                            !matches(s[i], p[j])
                2.2. p[j] == "*": P(i, j) = P(i - 1, j) or P(i, j - 2)             matches(s[i], p[j])
                     p[j] == "*": P(i, j) = P(i, j - 2)                            !matches(s[i], p[j])
            3. 边界条件: 无
        ---
        时间复杂度: O(m * n) : m 和 n 分别是字符串 s 和 p 的长度
        空间复杂度: O(m * n) : 存储所有状态使用的空间
        ---
        难点:
        1. 转移方程 4 种情况比较复杂
        2. "." 应归类于字母一并考虑
        3. 转移方程 2.2 类似于马尔可夫的思路比较难想
        '''

        # 判断是否匹配
        def matches(i, j):
            # p[j] 为字母
            if s[i] == p[j]:
                return True

            # p[j] 为 "."
            if p[j] == ".":
                return True

            # p[j] 为 "*" 或 s[i] != p[j]
            return False

        # 字符串长度
        m, n = len(s), len(p)

        # 初始化函数
        dp = [[False] * n for i in range(m)]

        # 外层循环: 遍历字符串 s
        for i in range(m):
            # 内层循环: 遍历字符串 p
            for j in range(n):
                # 判断 p[j] 是否为 "*"
                if p[j] != "*":
                    # 判断 s[i] 与 p[j] 是否匹配
                    if matches(i, j):
                        print("下午继续写")

