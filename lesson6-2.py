
class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def roads(self):
        #print(f'Масса асфальта {self._length * self._width * 25 * 5 / 1000} тонн')
        return f"{self._length * self._width * 25 * 5 / 1000} тонн"

#road1 = Road(5000, 20)
road1 = Road(int(input('Введите длину: ')), int(input('Введите ширину: ')))
print(road1.roads())