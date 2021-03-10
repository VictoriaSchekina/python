class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"
    def get_total_income(self):
        return f"{sum(self._income.values())}"


manager = Position("Ivan", "Petrov", "Pastry chef", 100000, 10000)
print(manager.get_full_name())
print(manager.position)
print(manager.get_total_income())

print("**************")

manager = Position("Oleg", "Ivanov", "Chef", 200000, 20000)
print(manager.get_full_name())
print(manager.position)
print(manager.get_total_income())
