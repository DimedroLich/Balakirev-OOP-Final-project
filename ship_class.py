
class Ship:
    """
    Класс Ship должен описывать корабли набором следующих параметров:
    x, y - координаты начала расположения корабля (целые числа);
    length - длина корабля (число палуб: целое значение: 1, 2, 3 или 4);
    tp - ориентация корабля (1 - горизонтальная; 2 - вертикальная).
    """

    #  TODO 1. При попадании в корабль (хотя бы одну его палубу), флаг _is_move устанавливается в False и перемещение корабля по игровому полю прекращается.
    #  TODO 2. Реализовать методы: 1.go; 2.is_out_pole

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
            if self._tp == 1:
                self.set_start_coords(self._x+go,self._y)
            else:
                self.set_start_coords(self._x,self._y+go)
    def is_collide(self, ship) -> bool:
        """Проверка на столкновение с другим кораблем ship"""
        x, y = self._x, self._y
        for x1,y1  in ((x, y),(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y), (x - 1, y + 1), (x, y + 1),
        (x + 1, y + 1)):
               if (x1,y1) == (ship._x, ship._y):
                   return True
        return False

    def is_out_pole(self,size) -> bool:
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
