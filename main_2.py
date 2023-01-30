from random import randint as rd, choice as ch


# TODO ПЕРВЫМ ДЕЛОМ: Реализовать метод move_ships в классе GAMEPOLE

class Ship:
    """
    Класс Ship должен описывать корабли набором следующих параметров:
    x, y - координаты начала расположения корабля (целые числа);
    length - длина корабля (число палуб: целое значение: 1, 2, 3 или 4);
    tp - ориентация корабля (1 - горизонтальная; 2 - вертикальная).
    """

    #  TODO 1. При попадании в корабль (хотя бы одну его палубу), флаг _is_move устанавливается в False и перемещение корабля по игровому полю прекращается.
    #  TODO 2. Реализовать методы: 1.go; 2.is_out_pole
    #  TODO 3. С помощью магических методов __getitem__() и __setitem__() обеспечить доступ к коллекции _cells

    def __init__(self, length, tp=1, x=None, y=None):

        self._x, self._y = x, y
        self._y_STARTING = self._y
        self._x_STARTING = self._x
        self._length = length
        self._tp = tp
        self._is_move = True  # Возможно ли перемешение корабля
        self._cells = [1 for i in range(length)]  # 1 - попадания не было; 2 - попадание было
        self.is_on_game_pole = False
        self.size_of_gamepole = None

    def set_start_coords(self, x, y):
        """
        Установка начальных координат (запись значений в локальные атрибуты _x, _y)
        """
        if self.size_of_gamepole is None:
            self._x = x
            self._y = y
            self._y_STARTING = self._y
            self._x_STARTING = self._x
        else:
            if (self._tp == 1 and x + self._length > self.size_of_gamepole) or (
                self._tp == 2 and y + self._length > self.size_of_gamepole):
                raise ValueError('Объект выходит за границы игрового поля')
            else:
                if self._tp == 1:

                    self._x = tuple(range(x, self._length + x))
                    self._y = (y,)
                    self._y_STARTING = self._y[0]
                    self._x_STARTING = self._x[0]
                else:

                    self._x = (x,)
                    self._y = tuple(range(y, self._length + y))
                    self._y_STARTING = self._y[0]
                    self._x_STARTING = self._x[0]

    def get_start_coords(self):
        return self._x, self._y

    def move(self, go):
        if self._is_move:
            if not self.is_on_game_pole:
                if self._tp == 1:
                    self.set_start_coords(self._x + go, self._y)
                else:
                    self.set_start_coords(self._x, self._y + go)
            else:
                if self._tp == 1:
                    self.set_start_coords(self._x[0] + go, self._y[0])
                else:
                    self.set_start_coords(self._x[0], self._y + go[0])

    def is_collide(self, ship) -> bool:
        """Проверка на столкновение с другим кораблем ship"""
        if not self.is_on_game_pole:
            x, y = self._x, self._y
            for x1, y1 in (
            (x, y), (x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y), (x - 1, y + 1), (x, y + 1),
            (x + 1, y + 1)):
                if (x1, y1) == (ship._x, ship._y):
                    return True
            return False
        else:
            x, y = self._x[0], self._y[0]
            for x1, y1 in (
                (x, y), (x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y), (x - 1, y + 1), (x, y + 1),
                (x + 1, y + 1)):
                if (x1, y1) == (ship._x, ship._y):
                    return True
            return False

    def is_out_pole(self, size) -> bool:
        """Проверка на выход корабля за пределы игрового поля"""
        # self.size_of_gamepole = size
        # try:
        #     self.set_start_coords(self._x,self._y)
        #     if (all(i<=size-1 for i in  tuple(self._x)) and all(i<= size-1 for i in  tuple(self._y))) :
        #         return False
        # except:
        #     return True
        if self._tp == 1:
            if self._x_STARTING + self._length <= size and self._y_STARTING <= size:
                return False
        else:
            if self._x_STARTING <= size and self._y_STARTING + self._length <= size:
                return False
        return True

    def __getitem__(self, item):
        return self._cells[item]

    def __setitem__(self, key, value):
        self._cells[key] = value


class GamePole:
    # TODO 1. Реализовать метод move_ships
    # TODO 2. Переделать метод show

    def __init__(self, size=10):
        self._size = size
        self._ships = []  # Список кораблей на игровом поле
        self.current_game_field = [[0 for i in range(size)] for i in range(size)]

    def get_ships(self):
        return self._ships

    def get_pole(self):
        return tuple(tuple(i) for i in self.current_game_field)

    def adjacent_cell_is_free_check(self, cell_index):
        """Проверяет являются ли соседние клетки свободными"""
        x, y = cell_index[0], cell_index[1]
        for index1, index2 in (
            (x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y), (x - 1, y + 1), (x, y + 1),
            (x + 1, y + 1)):
            try:
                if self.current_game_field[index1][index2] != 0:
                    return False
            except IndexError:
                continue
        return True

    def init(self):
        n = 1
        for outer_num in range(4, 0, -1):
            self._ships.extend(Ship(outer_num, tp=rd(1, 2)) for i in range(n))
            n += 1
        for ship in self._ships:
            ship.size_of_gamepole = self._size
            while ship.is_on_game_pole != True:
                try:
                    x = rd(0, self._size - 1)
                    y = rd(0, self._size - 1)
                    if (ship._tp == 1 and x + ship._length > ship.size_of_gamepole) or (
                        ship._tp == 2 and y + ship._length > ship.size_of_gamepole):
                        raise ValueError('Объект выходит за границы игрового поля')
                    if ship._tp == 1:
                        ship._y_STARTING = x
                        ship._x_STARTING = y
                        x = tuple(range(x, ship._length + x))
                        y = (y,)
                    else:
                        ship._y_STARTING = x
                        ship._x_STARTING = y
                        x = (x,)
                        y = tuple(range(y, ship._length + y))

                    results = []
                    for x_check in x:
                        for y_check in y:
                            rez = self.adjacent_cell_is_free_check((x_check, y_check))
                            results.append(rez)
                    if all(i == True for i in results):
                        for i in x:
                            for j in y:
                                self.current_game_field[i][j] = ship._length
                        ship.set_start_coords(x[0], y[0])
                        ship.is_on_game_pole = True

                    else:
                        raise ValueError
                except ValueError:
                    continue

    def move_ships(self):
        for ship in self._ships:
            ship_before = ship
            go = ch([-1, 1])
            ship.move(go)
            if ship.is_out_pole(self._size):
                ship = ship_before

    def show(self):
        for i in self.current_game_field:
            for j in i:
                print(j, end=" ")
            print()


ship = Ship(2)
ship = Ship(2, 1)
ship = Ship(3, 2, 0, 0)

assert ship._length == 3 and ship._tp == 2 and ship._x == 0 and ship._y == 0, "неверные значения атрибутов объекта класса Ship"
assert ship._cells == [1, 1, 1], "неверный список _cells"
assert ship._is_move, "неверное значение атрибута _is_move"

ship.set_start_coords(1, 2)
assert ship._x == 1 and ship._y == 2, "неверно отработал метод set_start_coords()"
assert ship.get_start_coords() == (1, 2), "неверно отработал метод get_start_coords()"

ship.move(1)
s1 = Ship(4, 1, 0, 0)
s2 = Ship(3, 2, 0, 0)
s3 = Ship(3, 2, 0, 2)

assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 0)"
assert s1.is_collide(
    s3) == False, "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 2)"

s2 = Ship(3, 2, 1, 1)
assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 1, 1)"

s2 = Ship(3, 1, 8, 1)
assert s2.is_out_pole(10), "неверно работает метод is_out_pole() для корабля Ship(3, 1, 8, 1)"

s2 = Ship(3, 2, 1, 5)
assert s2.is_out_pole(10) == False, "неверно работает метод is_out_pole(10) для корабля Ship(3, 2, 1, 5)"

s2[0] = 2
assert s2[0] == 2, "неверно работает обращение ship[indx]"

p = GamePole(10)
p.init()
for nn in range(5):
    for s in p._ships:
        assert s.is_out_pole(10) == False, "корабли выходят за пределы игрового поля"

        for ship in p.get_ships():
            if s != ship:
                assert s.is_collide(ship) == False, "корабли на игровом поле соприкасаются"
    p.move_ships()

gp = p.get_pole()
assert type(gp) == tuple and type(gp[0]) == tuple, "метод get_pole должен возвращать двумерный кортеж"
assert len(gp) == 10 and len(gp[0]) == 10, "неверные размеры игрового поля, которое вернул метод get_pole"

pole_size_8 = GamePole(8)
pole_size_8.init()
