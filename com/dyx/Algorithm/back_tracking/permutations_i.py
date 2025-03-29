'''输入一个整数数组，其中不包含重复元素，返回所有可能的排列。'''
def permutations_i(nums: list[int]):
    res = []
    backtrack(state=[], choices=nums, selected = [False] * len(nums), res=res)

