def solution(keyinput, board):
    site = [0,0]
    max_row = board[0] // 2
    min_row = (board[0] // 2)*(-1)
    max_col = board[1] //2
    min_col = (board[1]//2)*(-1)
    for i in keyinput:
        if i == 'up':
            site[1] = site[1]+1
            if site[1] > max_col:
                site[1] = max_col
        elif i == 'down':
            site[1] = site[1]-1
            if site[1] < min_col:
                site[1] = min_col
        elif i == 'right':
            site[0] = site[0]+1
            if site[0] > max_row:
                site[0] = max_row
        elif i == 'left':
            site[0] = site[0]-1
            if site[0] < min_row:
                site[0] = min_row
    return site
