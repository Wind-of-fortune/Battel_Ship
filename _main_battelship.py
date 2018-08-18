
import essential_functions_without_class


class ShipMaker:

    board_list = [['~' for j in range(11)] for i in range(11)]
    s_new = []
    coords_new = ''

    def __init__(self,ship_size,text):
        self.ship_size = ship_size
        self.text = text
        ShipMaker.input_and_checking_ships(self)

    def printing_board(self):  # printing board
        print('       Your board')
        a = self.board_list
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


    def input_and_checking_ships(self):  # проверка на ошибки пользовательского ввода и обращение к функции создания кораблей
        num = self.ship_size

        try:
            coord = input('Введите координаты {}палубного корабля (в формате - "A1,A2,A3,A4"): \n '.format(self.text))
            self.coords_new = coord
            if num == 4:
                if len(self.coords_new) < 11 or len(self.coords_new) > 15:
                    print('вы ошиблись при вводе! попробуйте снова!')
                    return ShipMaker.input_and_checking_ships(self)

                a = coord
                a = a.replace('10', '1')
                if len(set(a)) != 6:
                    print('Вы сплющили ваш корабль, как так??')
                    return ShipMaker.input_and_checking_ships(self)

            if num == 3:
                if len(self.coords_new) < 8 or len(self.coords_new) > 11:
                    print('вы ошиблись при вводе! попробуйте снова!')
                    return ShipMaker.input_and_checking_ships(self)

                a = coord
                a = a.replace('10', '1')
                if len(set(a)) != 5:
                    print('Вы сплющили ваш корабль, как так??')
                    return ShipMaker.input_and_checking_ships(self)

            if num == 2:
                if len(self.coords_new) < 5 or len(self.coords_new) > 7:
                    print('вы ошиблись при вводе! попробуйте снова!')
                    return ShipMaker.input_and_checking_ships(self)

                a = coord
                a = a.replace('10', '1')
                if len(set(a)) != 4:
                    print('Вы сплющили ваш корабль, как так??')
                    return ShipMaker.input_and_checking_ships(self)

            if num == 1:
                if len(self.coords_new) < 2 or len(self.coords_new) > 3:
                    print('вы ошиблись при вводе! попробуйте снова!')
                    return ShipMaker.input_and_checking_ships(self)
        except:
            print(
                'Что-то пошло не так, скорее всего вы ошиблись при вводе координат или нарушили формат записи, попробуйте еще раз:')
            ShipMaker.input_and_checking_ships(self)

        try:
            ShipMaker.ships_coords_to_board(self)
        except:
            print(
                'Что-то пошло не так, скорее всего вы ошиблись при вводе координат или нарушили формат записи, попробуйте еще раз:')
            ShipMaker.input_and_checking_ships(self)



    def ships_coords_to_board(self):  # transform user input (ship coordinats) to the board field
        board = self.board_list
        coords = self.coords_new

        s = coords.split(',')
        letter_to_numbers_dict = dict(
            zip(['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        for i in range(len(s)):
            s[i] = list(s[i])

        for i in range(len(s)):
            if len(s[i]) > 2:
                s[i][-2] = s[i][-2] + s[i][-1]
                s[i].pop(-1)

        for key, val in letter_to_numbers_dict.items():
            for i in range(len(s)):
                if s[i][0] == key:
                    s[i][0] = val

        for i in range(len(s)):
            for j in range(len(s[i])):
                s[i][j] = int(s[i][j])

        self.s_new = s
        ShipMaker.cheking_ships_for_non_separating(self)
        ShipMaker.ship_zone(self)

        for m in range(len(s)):
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if i == s[m][0] and j == s[m][1]:
                        board[j][i] = '0'
        board = self.board_list
        ShipMaker.printing_board(self)
        return self.board_list





    def cheking_ships_for_non_separating(self):  # проверка кораблей на целостность(чтобы четырехпалубный корабль например не был разбросан по всему полю и небыл завернут зигзагом)
        a = set()
        b = set()
        for i in range(len(self.s_new)):
            a.add(self.s_new[i][0])
            b.add(self.s_new[i][1])
        a = list(a)
        b = list(b)
        if len(a) != 1 and len(b) != 1:
            print('Ваш корабль разлетелся на куски, придется выставить новый...')
            raise TypeError
        if len(a) == 1 and len(b) != 1:
            b.sort()
            for i in range(1, len(b)):
                if b[i] - b[i - 1] != 1:
                    print('Ваш корабль разлетелся на куски, придется выставить новый...')
                    raise TypeError

        if len(b) == 1 and len(a) != 1:
            a.sort()
            for i in range(1, len(a)):
                if a[i] - a[i - 1] != 1:
                    print('Ваш корабль разлетелся на куски, придется выставить новый...')
                    raise TypeError

    def ship_zone(self):  # проверка на соприкасание с другими кораблями
        for m in range(len(self.s_new)):
            for i in range(len(self.board_list)):
                for j in range(len(self.board_list[i])):
                    if i == self.s_new[m][0] and j == self.s_new[m][1]:
                        if i < 10 and j < 10 and i > 0 and j > 0:
                            if self.board_list[j][i] == '0' or self.board_list[j + 1][i] == '0' or self.board_list[j - 1][i] == '0' or \
                                    self.board_list[j][i + 1] == '0' or self.board_list[j][i - 1] == '0' or self.board_list[j + 1][
                                i + 1] == '0' or self.board_list[j - 1][i - 1] == '0' or self.board_list[j + 1][i - 1] == '0' or \
                                    self.board_list[j - 1][i + 1] == '0':
                                print('Столкновение, нельзя располагать корабли так близко друг к другу')
                                raise TypeError
                        if i > 9 and j != 10:
                            if self.board_list[j][i] == '0' or self.board_list[j + 1][i] == '0' or self.board_list[j - 1][
                                i - 1] == '0' or self.board_list[j + 1][i - 1] == '0':
                                print('Столкновение, нельзя располагать корабли так близко друг к другу')
                                raise TypeError
                        if j > 9 and i != 10:
                            if self.board_list[j][i] == '0' or self.board_list[j][i + 1] == '0' or self.board_list[j - 1][
                                i - 1] == '0' or self.board_list[j - 1][i + 1] == '0' or self.board_list[j][i - 1] == '0':
                                print('Столкновение, нельзя располагать корабли так близко друг к другу')
                                raise TypeError


class ShipMakerPlaerTwo(ShipMaker):
    board_list = [['~' for j in range(11)] for i in range(11)]
    s_new = []
    coords_new = ''



class EnemyShips:

    board_enemy_list = [['~' for j in range(11)] for i in range(11)]

    def printing_enemy_board(self):  # printing board
        print('       Enemy board')
        a = self.board_enemy_list
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

class EnemyShipsPlayerTwo(EnemyShips):

    board_enemy_list = [['~' for j in range(11)] for i in range(11)]



class Shoot(EnemyShips, ShipMakerPlaerTwo):

    viktory = 0
    win = 0

    def __init__(self,shoot_coord):
        self.shoot = shoot_coord
        Shoot.shoot(self)

    def shoot(self):
        s = self.shoot.split(',')
        letter_to_numbers_dict = dict(
            zip(['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        for i in range(len(s)):
            s[i] = list(s[i]) #ПРОБЛЕМА В ЦИФРЕ 10!!!!

        if len(s[0]) > 2: #костыль
            s[0][1] = 10
            s[0].pop(-1)

        for key, val in letter_to_numbers_dict.items():
            for i in range(len(s)):
                if s[i][0] == key:
                    s[i][0] = val

        for i in range(len(s)):
            for j in range(len(s[i])):
                s[i][j] = int(s[i][j])

        for m in range(len(s)):
            for i in range(len(ShipMakerPlaerTwo.board_list)):
                for j in range(len(ShipMakerPlaerTwo.board_list[i])):
                    if i == s[m][0] and j == s[m][1]:
                        if ShipMakerPlaerTwo.board_list[j][i] != '0':
                            ShipMakerPlaerTwo.board_list[j][i] = '*'
                            EnemyShips.board_enemy_list[j][i] = '*'
                            print()
                            print('!!Мимо!!')
                        else:
                            ShipMakerPlaerTwo.board_list[j][i] = 'X'
                            EnemyShips.board_enemy_list[j][i] = 'X'
                            print()
                            print('!!Попадание!!')

        for i in range(len(ShipMakerPlaerTwo.board_list)): ###cheking_viktory
            for j in range(len(ShipMakerPlaerTwo.board_list[i])):
                if ShipMakerPlaerTwo.board_list[i][j] == '0':
                    Shoot.viktory += 1

        EnemyShips.printing_enemy_board(self)

        if Shoot.viktory == 0:
            Shoot.win = 1
            return Shoot.win

        Shoot.viktory = 0

        return ShipMakerPlaerTwo.board_list, EnemyShips.board_enemy_list


class Shoot_player2 (EnemyShipsPlayerTwo,ShipMaker):

    viktory = 0
    win = 0

    def __init__(self,shoot_coord):
        self.shoot = shoot_coord
        Shoot_player2.shoot(self)

    def shoot(self):
        s = self.shoot.split(',')
        letter_to_numbers_dict = dict(
            zip(['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        for i in range(len(s)):
            s[i] = list(s[i])

        if len(s[0]) > 2: #костыль
            s[0][1] = 10
            s[0].pop(-1)

        for key, val in letter_to_numbers_dict.items():
            for i in range(len(s)):
                if s[i][0] == key:
                    s[i][0] = val

        for i in range(len(s)):
            for j in range(len(s[i])):
                s[i][j] = int(s[i][j])

        for m in range(len(s)):
            for i in range(len(ShipMaker.board_list)):
                for j in range(len(ShipMaker.board_list[i])):
                    if i == s[m][0] and j == s[m][1]:
                        if ShipMaker.board_list[j][i] != '0':
                            ShipMaker.board_list[j][i] = '*'
                            EnemyShipsPlayerTwo.board_enemy_list[j][i] = '*'
                            print()
                            print('!!Мимо!!')
                        else:
                            ShipMaker.board_list[j][i] = 'X'
                            EnemyShipsPlayerTwo.board_enemy_list[j][i] = 'X'
                            print()
                            print('!!Попадание!!')


        for i in range(len(ShipMaker.board_list)):  ###cheking_viktory
            for j in range(len(ShipMaker.board_list[i])):
                if ShipMaker.board_list[i][j] == '0':
                    Shoot_player2.viktory += 1

        EnemyShipsPlayerTwo.printing_enemy_board(self)

        if Shoot_player2.viktory == 0:
            Shoot_player2.win = 1
            return Shoot_player2.win

        Shoot_player2.viktory = 0

        return ShipMaker.board_list, EnemyShipsPlayerTwo.board_enemy_list



#######main-code########

print('Игра рассчитана на двоих человек')

player_one_name = input('Введите имя первого игрока: ')
player_two_name = input('Введите имя второго игрока: ')

print('Первым ходит игрок - {}'.format(player_one_name))
print('Разместите свои корабли!')

# Создаем экземпляры кораблей
p1_ship_40 = ShipMaker(4,'четырех')
p1_ship_31 = ShipMaker(3,'трех')
p1_ship_32 = ShipMaker(3,'трех')
p1_ship_21 = ShipMaker(2,'двух')
p1_ship_22 = ShipMaker(2,'двух')
p1_ship_23 = ShipMaker(2,'двух')
p1_ship_11 = ShipMaker(1,'одно')
p1_ship_12 = ShipMaker(1,'одно')
p1_ship_13 = ShipMaker(1,'одно')
p1_ship_14 = ShipMaker(1,'одно')

eship_p1 = EnemyShips()
eship_p1.printing_enemy_board()

print('Теперь игрок - {} расставляет свои корабли'.format(player_two_name))
print('Разместите свои корабли!')

# Создаем экземпляры кораблей
p2_ship_40 = ShipMakerPlaerTwo(4,'четырех')
p2_ship_31 = ShipMakerPlaerTwo(3,'трех')
p2_ship_32 = ShipMakerPlaerTwo(3,'трех')
p2_ship_21 = ShipMakerPlaerTwo(2,'двух')
p2_ship_22 = ShipMakerPlaerTwo(2,'двух')
p2_ship_23 = ShipMakerPlaerTwo(2,'двух')
p2_ship_11 = ShipMakerPlaerTwo(1,'одно')
p2_ship_12 = ShipMakerPlaerTwo(1,'одно')
p2_ship_13 = ShipMakerPlaerTwo(1,'одно')
p2_ship_14 = ShipMakerPlaerTwo(1,'одно')

eship_p2 = EnemyShipsPlayerTwo()
eship_p2.printing_enemy_board()

error_checker = 0


for i in range(99):

    print('ходит игрок {}'.format(player_one_name))

    while error_checker == 0 :
        try:
            shoot = Shoot(input('Введите координаты для стрельбы : '))
            error_checker = 1
        except:
            print('Вы ошиблись при вводе!')

    error_checker = 0

    if Shoot.win == 1:
        print()
        print('!!!Поздравляем, вы победили!!!')
        break

    essential_functions_without_class.printing_board(ShipMaker.board_list)

    print('ходит игрок {}'.format(player_two_name))

    while error_checker == 0 :
        try:
             shoot2 = Shoot_player2(input('Введите координаты для стрельбы : '))
        except:
            print('Вы ошиблись при вводе!')

    error_checker = 0

    if Shoot_player2.win == 1:
        print()
        print('!!!Поздравляем, вы победили!!!')
        break

    essential_functions_without_class.printing_board(ShipMakerPlaerTwo.board_list)


