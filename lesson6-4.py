class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f"Машина {self.name} цвета {self.color} со скоростью {self.speed} км/ч, является полицейской {self.is_police}")

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"{self.name} остановилась")

    def turn(self, direction):
        print(f"{self.name} повернула {'налево' if direction == 0 else 'направо'}")

    def show_speed(self):
        print(f"Скорость автомобиля {self.name} - {self.speed} км/ч")

class TownCar(Car):
    def show_speed(self):
        return f"Скорость автомобиля {self.name} - {self.speed}. Превышение скорости." if self.speed > 60 else f"Скорость автомобиля {self.name} составляет {self.speed} км/ч."


class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        return f"Скорость автомобиля {self.name} - {self.speed}. Превышение скорости." if self.speed > 40 else f"Скорость автомобиля {self.name} составляет {self.speed} км/ч."


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


towncar1 = TownCar("Mazda", "black", 100)
towncar1.go()
print(towncar1.show_speed())
towncar1.stop()
print()

policecar1 = PoliceCar("VW Polo", "white", 70)
policecar1.go()
print(policecar1.show_speed())
policecar1.turn(1)
policecar1.stop()
print()

