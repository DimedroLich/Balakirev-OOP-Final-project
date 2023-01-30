from random import randint as rd,choice as ch
from ship_class import Ship
class GamePole:

    # TODO 2. Переделать метод show

    def __init__(self, size=10):
        self._size = size
        self._ships = []  # Список кораблей на игровом поле
        self.current_game_field = [[0 for i in range(size)] for i in range(size)]

    def get_ships(self):
        return self._ships

    def get_pole(self):
        return tuple(tuple(i) for i in self.current_game_field)

    def adjacent_cell_is_free_check(self, cell_index: tuple[int | int]) -> bool:
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
        for num, point in enumerate(reversed(range(1, 5)), 1):
            self._ships.extend(Ship(num, tp=rd(1, 2)) for i in range(point))
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
            go = ch([-1,1])
            ship.move(go)
            if ship.is_out_pole(self._size):
                ship = ship_before


    def show(self):
        for i in self.current_game_field:
            for j in i:
                print(j, end=" ")
            print()