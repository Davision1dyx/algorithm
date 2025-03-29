def back_track(state: State, choices: list[Choice], res: list[State]):
    '''回溯算法框架'''
    if is_solution(state):
        record_solution(state, res)
        return
    # 遍历所有选择
    for choice in choices:
        # 剪枝
        if is_valid(state, choice):
            # 尝试：做出选择，更新状态
            make_choice(state, choice)
            backtrack(state, choices, res)
            # 回退：撤销选择，恢复到之前的状态
            undo_choice(state, choice)
