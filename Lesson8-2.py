class Division:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def divide(a, b):
        try:
            return (a / b)
        except:
            return (f"Error")


div = Division(10, 100)
print(Division.divide(6, 2))
print(Division.divide(1, 0.1))
print(div.divide(5, 0))