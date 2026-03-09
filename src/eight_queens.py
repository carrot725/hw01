def is_valid(board, row, col):
    """判断在(row, col)位置放置皇后是否合法"""
    # 检查列
    for i in range(row):
        if board[i] == col:
            return False
    # 检查对角线
    for i in range(row):
        if abs(row - i) == abs(col - board[i]):
            return False
    return True

def solve_n_queens(n):
    """求解n皇后问题，返回所有解的列表"""
    solutions = []
    board = [-1] * n  # board[i] 表示第i行皇后所在列

    def backtrack(row):
        if row == n:
            solutions.append(board.copy())
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # 回溯

    backtrack(0)
    return solutions

if __name__ == "__main__":
    # 测试8皇后
    solutions = solve_n_queens(8)
    print(f"8皇后问题共有 {len(solutions)} 个解")
    input("按回车键关闭窗口...")  # 新增的暂停代码