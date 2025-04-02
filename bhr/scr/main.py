from typing import List, Dict, Self

#EXAMPLE
#(.)(.)

#TYPE HERE
class Position3D:
    coordinate_x: int = 0
    coordinate_y: int = 0
    coordinate_z: int = 0

    def __init__(self, x, y, z):
        self.coordinate_x=x
        self.coordinate_y=y
        self.coordinate_z=z
    
    def __repr__(self):
        return f'x={self.coordinate_x}; y={self.coordinate_y}; z={self.coordinate_z};'

#No Boobs 4 u
class edge3D:
    pass


if __name__ == '__main__': #Проверяет запущен ли файл с кодом пользователем. Если нет, не исполняется.
    point = Position3D(x=22, y=55, z=10)
    
    print(point.coordinate_z)

    


















    #biiiiiiiiiiiiig boobs
    #( . )( . )