# -*- coding utf-8 -*- #
import itertools
from typing import List


class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        s, maxs = 0, 0
        for a in itertools.chain(arr, k > 1 and arr or ()):
            s = a if s < 0 else s + a  # 连续和
            if s > maxs:
                maxs = s  # 最大连续和
        if k <= 2:
            return maxs  # 两个周期以内之间返回最大连续和
        # 否则返回可能加上的多周期和
        return (max(sum(arr), 0) * (k - 2) + maxs) % 1000000007


if __name__ == '__main__':
    s = Solution()
    print(s.kConcatenationMaxSum([1, 2], 3))
    print(s.kConcatenationMaxSum([1, -2, 1], 5))
    print(s.kConcatenationMaxSum([-1, -2], 7))
    print(s.kConcatenationMaxSum([2, -1, -2, 4], 7))
    print(s.kConcatenationMaxSum([2, -1, 4, 2, -2, 4], 7))
    print(s.kConcatenationMaxSum([2, -2, 4, 2, -1, 4], 7))
