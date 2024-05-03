class Calculator:
    def add(self, num_1, num_2):
        return num_1 + num_2
    def minus(self, num_1, num_2):
        return num_1 - num_2
    def divide(self, num_1, num_2):
        if num_2==0:
            return "Eror! can not devide by 0"
        return num_1/num_2
    def multiply(self, num_1,  num_2):
        return num_1 * num_2

calculating = Calculator()

# Addition
print("method add:", calculating.add(13, 5))

# Subtraction
print("method minus:", calculating.minus(14, 21))

# Multiplication
print("method Multiplication:", calculating.multiply(6, 7))

# Division
print("method Division:", calculating.divide(20, 0))
