class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        思路: 
        dp[i]: 以 s[i] 结尾的最长有效括号对
        只有 ")" 的位置 dp[i] 会增加, 返回最后数组中最大的 dp[i] 即可
        ---
        转移方程:
        1. s[i] = ")" s[i - 1] = "(": dp[i] = dp[i - 2] + 2
        2. s[i] = ")" s[i - 1] = ")" s[i - dp[i - 1] - 1] = "(": dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
        Exp: ( ) ( ( ) )
        Ind: 0 1 2 3 4 5
        dp : 0 2 0 0 2 ?
        计算 dp[5], 不仅仅要考虑 dp[4] + 2, 还需要考虑 dp[1]
        dp[1] = dp[4 - dp[4] - 1]: 从 s[4] 回退至以 s[4] 结尾的最长有效括号对起始位置, 再退一个, 判断是否为与 s[5] 配对的 "(", 判断成功则再向前退一个, 将前面的有效括号对也加上
        ---
        边界条件:
        dp[0] = 0
        ---
        时间复杂度: O(n) : 只需遍历一次字符串
        空间复杂度: O(n) : 只需建立一个与字符串长度相同的数组
        ---
        难点:
        '''
        # 字符串长度
        n = len(s)

        # 对于长度为 0 的字符串直接返回 0
        if n == 0:
            return 0
       
        # 初始化转移矩阵
        dp = [0] * n
        
        # 遍历整个字符串
        for i in range(n):
            # ")" 作为有效括号对结束标志
            if s[i] == ")":
                # 前一个符号不存在
                if i == 0:
                    continue

                # 前一个符号为 "("
                elif s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
            
                # 前一个符号为 ")"
                else:
                    # 判断 s[i - dp[i - 1] - 1] 是否为存在
                    if i - dp[i - 1] == 0:
                        continue
                    # 判断 s[i - dp[i - 1] - 1] 是否为 "("
                    elif s[i - dp[i - 1] - 1] == "(":
                        dp[i] = dp[i - 1] + 2
                        #  再判断 "(" 前是否仍有有效括号对
                        if i - dp[i - 1] - 1 == 0:
                            continue
                        # 若前面仍有有效括号
                        else:
                            # 加上前方有效括号
                            dp[i] += dp[i - dp[i - 1] - 2]
                            
        # 返回最终结果
        return max(dp)
