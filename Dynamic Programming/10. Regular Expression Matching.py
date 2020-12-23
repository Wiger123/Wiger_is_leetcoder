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
        动态规划:
            1. 定义函数 P(i, j):  s 字符串的前 i 位与 p 字符串的前 j 位是否可以匹配
            2. 转移方程:
                2.1. s[i]
            3. 边界条件:
        ---
        时间复杂度: O() :
        空间复杂度: O() :
        '''
