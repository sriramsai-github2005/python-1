class Number:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def add(self):
        return self.number1 + self.number2

num = Number(12, 15)
addition = num.add()
print(addition)




