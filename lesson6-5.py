class Stationery:
    def __init__(self, title, draw):
        self.title = title
        self.draw = draw

    def go(self):
        print(f"{self.draw} старт зарисовки")

class Pen(Stationery):
    def go(self):
        print(f"{self.title} нарисован(а) {self.draw}  ручкой")

class Pencil(Stationery):
    def go(self):
        print(f"{self.title} нарисован(а) {self.draw} карандашом")

class Handle(Stationery):
    def go(self):
        print(f"{self.title} нарисован(а) {self.draw} маркером")

work1 = Pen("Картина", "черной")
work1.go()

work2 = Pencil("Портрет", "простым")
work2.go()

work3 = Handle("Обложка", "зеленым")
work3.go()




