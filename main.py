from random import randint as rd


# TODO ПЕРВЫМ ДЕЛОМ: РЕАЛИЗОВАТЬ РАССТАНОВКУ КОРАБЛЕЙ НА ПОЛЕ В КЛАССЕ GAMEPOLE.

class Ship:
    """
    Класс Ship должен описывать корабли набором следующих параметров:
    x, y - координаты начала расположения корабля (целые числа);
    length - длина корабля (число палуб: целое значение: 1, 2, 3 или 4);
    tp - ориентация корабля (1 - горизонтальная; 2 - вертикальная).
    """

    #  TODO 1. При попадании в корабль (хотя бы одну его палубу), флаг _is_move устанавливается в False и перемещение корабля по игровому полю прекращается.
    #  TODO 2. Реализовать методы: 1.go; 2.is_collide; 3.is_out_pole
    #  TODO 3. С помощью магических методов __getitem__() и __setitem__() обеспечить доступ к коллекции _cells

    def __init__(self, length, tp=1, x=None, y=None):
        self._x, self._y = x, y
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
            if self._tp == 1:
                self._x = tuple(range(x, self._length + x))
                self._y = y
            else:
                self._x = x
                self._y = tuple(range(y, self._length + y))
        else:
            if (self._tp == 1 and x + self._length > self.size_of_gamepole) or (
                self._tp == 2 and y + self._length > self.size_of_gamepole):
                raise ValueError('Объект выходит за границы игрового поля')
            else:
                if self._tp == 1:
                    self._x = tuple(range(x, self._length + x))
                    self._y = (y,)
                else:
                    self._x = (x,)
                    self._y = tuple(range(y, self._length + y))

    def get_start_coords(self):
        return self._x, self._y

    def move(self, go):
        ...

    def is_collide(self, ship) -> bool:
        """Проверка на столкновение с другим кораблем ship"""

    def is_out_pole(size) -> bool:
        """Проверка на выход корабля за пределы игрового поля"""


class GamePole:
    # TODO 1. В методе init() расстановка кораблей по игровому полю со случайными координатами, чтобы они не соприкасались друг с другом в том числе по диагонали
    # TODO 2. Переделать метод show

    def __init__(self, size=10):
        self._size = size
        self._ships = []  # Список кораблей на игровом поле
        self.current_game_field = [[0 for i in range(size)] for i in range(size)]


    def adjacent_cell_is_free_check(self, cell_index: tuple[int | int]) -> bool:
        """Проверяет являются ли соседние клетки свободными"""
        x,y = cell_index[0],cell_index[1]
        for index1, index2 in ((x-1,y-1), (x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)):
            try:
                if self.current_game_field[index1][index2] != 0:
                    return False
            except IndexError:
                continue
        return True



    def init(self):
        for num, point in enumerate(reversed(range(1, 5)), 1):
            self._ships.extend(Ship(num, tp=rd(1, 2)) for i in range(point))
        for ship in self._ships:
            ship.size_of_gamepole = self._size
            while ship.is_on_game_pole != True:
                try:
                    x = rd(0, self._size - 1)
                    y = rd(0, self._size - 1)
                    ship.set_start_coords(x, y)
                    results = []
                    for x_check in ship._x:
                        for y_check in ship._y:
                            rez = self.adjacent_cell_is_free_check((x_check,y_check))
                            results.append(rez)
                    if all(i==True for i in results):
                        for i in ship._x:
                            for j in ship._y:
                                self.current_game_field[i][j] = ship._length
                        ship.is_on_game_pole = True
                        self.show()
                        print('****************')
                        print()
                        print('******************')
                    else:
                        raise ValueError
                except ValueError:
                    continue

    def show(self):
        for i in a.current_game_field:
            for j in i:
                print(j, end=" ")
            print()


a = GamePole()
a.init()
a.show()
# for i in a._ships:
#     print(i.__dict__)

# b = Ship(4,tp=2)
# b.size_of_gamepole = 10
# b.set_start_coords(6,6)
# print(b.__dict__)
