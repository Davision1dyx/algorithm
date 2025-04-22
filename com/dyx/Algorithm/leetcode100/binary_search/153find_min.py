'''
已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
若旋转 7 次，则可以得到 [0,1,2,4,5,6,7]
注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。

给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。

你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
'''


class Solution:
    # 分析一下：
    # 1）元素值 互不相同。 原数组为升序。 寻找最小元素。 复杂度O(log n)
    # 寻找最小元素 -》 寻找a[n-1] > a[n] 的元素，如果不存在，则a[0]为最小。 x错误分析，其实二分查找，最右侧的数即可，因为最右侧的数只可能是大于或等于目标
    # 2） 是否直接使用O(log n)的排序算法也可以？ 是可以

    #快排
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        i, j = 0, n - 1
        self.quick_sort(nums, i, j)
        return nums[0]

    def quick_sort(self, nums:list[int], left: int, right: int):
        i = left
        j = right
        n = j - i + 1
        a = nums[left]
        if n == 1:
            return
        while i < j:
            while i<j and nums[j] >= a:
                j -= 1
            while i<j and nums[i] <= a:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i], nums[left] = nums[left], nums[i]
        if i - 1 >= 0:
            self.quick_sort(nums, 0, i - 1)
        if i + 1 <= n - 1:
            self.quick_sort(nums, i + 1, n - 1)

s = Solution()
nums1=[3,4,5,1,2]
nums2=[4,5,6,7,0,1,2]
nums3=[11,13,15,17]
print(s.findMin(nums1))
print(s.findMin(nums2))
print(s.findMin(nums3))