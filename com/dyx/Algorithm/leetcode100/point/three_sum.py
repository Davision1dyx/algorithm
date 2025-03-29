class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            target = nums[i]
            if i > 0 and target == nums[i-1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[j] + nums[k] < -target:
                    j += 1
                elif nums[j] + nums[k] > -target:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
        return res

nums1 = [-1,0,1,2,-1,-4]
nums2 = [0,1,1]
nums3 = [0,0,0]
s = Solution()
print(s.threeSum(nums1))
print(s.threeSum(nums2))
print(s.threeSum(nums3))