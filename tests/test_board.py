import itertools

from tbraille.board import Board, Cell


def test_cell_bit():
    cell = Cell()
    assert cell.value == 0

    cell[0, 0] = 1
    assert cell[0, 0] == 1
    assert str(cell) == '⠁'

    cell[1, 1] = 1
    assert cell[1, 1] == 1
    assert str(cell) == '⠑'

    cell[1, 3] = 1
    assert cell[1, 3] == 1
    assert str(cell) == '⢑'


def test_board_bit():
    board = Board(10, 10)
    for x, y in itertools.product(range(10), range(10)):
        assert board[x, y] == 0

    for i in range(10):
        board[i, i] = 1
        assert board[i, i] == 1

    expected_result = '⠑⢄\n⠀⠀⠑⢄\n⠀⠀⠀⠀⠑'
    result = str(board)
    print(result)

    assert result == expected_result
