def check_move_for_figure(figure: str, delta_x: int, delta_y: int, unique_case: bool) -> bool: 

    move_rook = delta_x * delta_y == 0
    move_bishop = abs(delta_x) == abs(delta_y)

    if figure == 'pawn':
        return (delta_y == 1 or delta_y == 2 and unique_case) and delta_x == 0

    if figure == 'rook':
        return move_rook
    
    if figure == 'knight':
        return abs(delta_x) + abs(delta_y) == 3 and delta_x * delta_y != 0

    if figure == 'bishop':
        return move_bishop

    if figure == 'queen':
        return move_rook or move_bishop

    if figure == 'king':
        return abs(delta_x) <= 1 and abs(delta_y) <= 1


data = input().upper().split(sep = '-')
figure = input()

unique_case = int(data[0][1]) == 2

delta_x = ord(data[1][0]) - ord(data[0][0])
delta_y = int(data[1][1]) - int(data[0][1])

print('correct' if check_move_for_figure(figure, delta_x, delta_y, unique_case) else 'uncorrect')
