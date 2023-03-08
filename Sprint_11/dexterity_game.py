# ID 81913514

BOARD_SIZE = 4

def get_board():
    board = {}
    for _ in range(BOARD_SIZE):
        for number in list(input()):
            if number != '.':
                board[number] = board.get(number, 0) + 1
    return board

def get_score(max_keys, board):
    """B. Ловкость рук.
    Подсчет максимального количества баллов, которое смогут набрать
    игроки в игре «Тренажёр для скоростной печати».
    """
    return len(list(filter(lambda value: value <= max_keys, board.values())))

def main():
    max_keys = int(input()) * 2
    board = get_board()
    print(get_score(max_keys, board))

if __name__ == '__main__':
    main()
