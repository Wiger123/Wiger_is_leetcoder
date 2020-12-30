class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        '''
        思路:
        dp_max[i]: 以 nums[i] 结尾的最大子数组和
        dp_min[i]: 以 nums[i] 结尾的最小子数组和
        由于所有数的和相同, 计算跨越数组边界的子数组最大值, 等同于计算不跨越数组边界子数组的最小值
        ---
        转移方程:
        dp_max[i] = max(nums[i], nums[i] + dp_max[i - 1])
        dp_min[i] = min(nums[i], nums[i] + dp_min[i - 1])
        ---
        边界条件:
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]
        ---
        时间复杂度: O(n) : 遍历一次数组, 即可完成所有计算
        空间复杂度: O(n) : 只需建立两个个大小为 n 的空间
        ---
        难点: 
        1. 等效转换: 计算跨越数组边界的子数组最大值, 等同于计算不跨越数组边界子数组的最小值
        2. 边界情况: dp_min[n - 1] 的子数组有可能包含了所有数组元素, 这种情况下取其补集是空数组, 因此要避免所有元素同时被选
        '''
        # 数组为空或长度为一直接返回
        if not A:
            return 0
        
        if len(A) == 1:
            return A[0]
    
        # 初始化
        n = len(A)
        dp_max = [0] * n
        dp_min = [0] * n
        dp_max[0] = A[0]
        dp_min[0] = A[0]
        sum_all = A[0]

        # 遍历数组
        for i in range(1, n):
            # 最大与最小子数组转移方程
            dp_max[i] = max(A[i], A[i] + dp_max[i - 1])
            dp_min[i] = min(A[i], A[i] + dp_min[i - 1])

            # 全数组之和
            sum_all += A[i]
        
        # dp_min[n - 1]: 以 A[n - 1] 结尾的最小子序列, 这种时候不需要跨越数字, 因此该位没有意义, 这里无需参与考虑
        # 返回结果
        return max(max(dp_max), sum_all - min(dp_min[:n-1]))
