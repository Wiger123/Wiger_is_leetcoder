class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        '''
        思路: 
        dp[i]: 第 i 个信封可以包含的信封数目(包括第 i 个信封本身)
        w 从小到大排序, 由于这种情况遍历时 w 可能相同, 逐个判断 w, h 较为麻烦, 故在 w 从小到大的基础上, h 从大到小排序, j < i, 只要出现 h[j][1] > h[i][1], 要么 i 和 j 的宽度相同, 无法嵌套, 要么 j 的宽度比 i 小, 但是高度比 i 大, 仍然无法嵌套, 从而减少了一层对宽度的判断
        例如: [[2, 2], [3, 7], [3, 5], [3, 3], [5, 5], [6, 8], [6, 2]]
        外层遍历: e[i]: e[1] -> e[n - 1]
        内层遍历: e[j]: e[0] -> e[i - 1]
        宽度相等: if e[j][0] == e[i][0]: continue
        宽度高度大于: if e[j][0] < e[i][0] and e[j][1] < e[i][1]: dp[j] = max(dp[i], dp[j] + 1)
        ---
        动态规划:
        ---
        时间复杂度: O(n ^ 2) : 内外两层遍历
        空间复杂度: O(n) : 存储 dp 数组使用空间
        ---
        难点:
        1. 对 w 进行从小到大排序后, 巧妙对 h 进行从大到小再排序
        '''
        # 信封大小
        n=len(envelopes)
        
        # 空信封直接返回 0
        if n == 0:
            return 0

        # 数组排序
        envelopes.sort(key=lambda x:(x[0], -x[1]))

        # 初始化转移数组
        dp = [1] * n

        # 随时记录最大值
        ans = 1

        # 外层遍历
        for i in range(1, n):
            # 内层循环
            for j in range(i):
                # 判断高度是否满足, 无需判断宽度, 只要高度不满足, envelopes[j][0] <= envelopes[i][0], 无法嵌套
                if envelopes[j][1] < envelopes[i][1]:
                    # 两者均满足的情况下, 根据信封层数关系决定结果
                    dp[i] = max(dp[i], dp[j] + 1)
                
            # 最大值更新
            ans = max(dp[i], ans)
        
        # 返回信封层数最大值
        return ans
