from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        state = []
        choices = nums
        res = []
        selected = []
        self.back_track(state, choices, selected, res)
        return res

    def back_track(self, state: list[int], choices: list[int], selected: list[int], res: list[list[int]]):
        if len(state) == len(choices):
            res.append(list(state))
        for choice in choices:
            if choice in selected:
                continue
            state.append(choice)
            selected.append(choice)
            self.back_track(state, choices, selected, res)
            state.pop()
            selected.pop()