from random import randint as rd

# TODO ПЕРВЫМ ДЕЛОМ: РЕАЛИЗОВАТЬ РАССТАНОВКУ КОРАБЛЕЙ НА ПОЛЕ В КЛАССЕ GAMEPOLE

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

    def set_start_coords(self, x, y):
        """
        Установка начальных координат (запись значений в локальные атрибуты _x, _y)
        """
        self._x, self._y = x, y

    def get_start_coords(self):
        return self._x, self._y

    def move(self, go): ...

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

    def init(self):
        for num,point in enumerate(reversed(range(1,5)),1):
            self._ships.extend(Ship(num, tp=rd(1, 2)) for i in range(point))
        for ship in self._ships:
            while ship.is_on_game_pole != True:
                try:
                    ship.set_start_coords()

    def show(self):
        for i in a.current_game_field:
            for j in i:
                print(j, end=" ")
            print()

a = GamePole()
a.init()

# for i in a._ships:
#     print(i.__dict__)


