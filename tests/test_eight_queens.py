from src.eight_queens import solve_n_queens

def test_n_queens_solution_count():
    assert len(solve_n_queens(1)) == 1
    assert len(solve_n_queens(4)) == 2
    assert len(solve_n_queens(8)) == 92