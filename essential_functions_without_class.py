
def printing_board(a):  # printing board
    print('       Your board')
    for i in range(len(a)):
        if i == 1:
            print('', i, a[i][j - 10], a[i][j - 9], a[i][j - 8], a[i][j - 7], a[i][j - 6], a[i][j - 5], a[i][j - 4],
                  a[i][j - 3], a[i][j - 2], a[i][j - 1])
        if 10 > i > 1:
            print('', i, a[i][j - 9], a[i][j - 8], a[i][j - 7], a[i][j - 6], a[i][j - 5], a[i][j - 4], a[i][j - 3],
                  a[i][j - 2], a[i][j - 1], a[i][j])
        if i >= 10:
            print(i, a[i][j - 9], a[i][j - 8], a[i][j - 7], a[i][j - 6], a[i][j - 5], a[i][j - 4], a[i][j - 3],
                  a[i][j - 2], a[i][j - 1], a[i][j])
        for j in range(0, len(a[i])):
            if i == 0 and j == 0:
                print(' - А Б В Г Д Е Ж З И К')
                break

