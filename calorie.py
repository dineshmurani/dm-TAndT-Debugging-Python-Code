print("Program has started".title())

class Calorie:

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        result = 10 * self.weight + 6.5 * self.height + 5 * age - 5 - self.temperature * 10
        return result

    def get_kj(self):
        kcal = self.calculate()
        return kcal * 4.184

    def kj_to_file(self):
        filepath = "calories.txt"
        with open(filepath, 'w') as file: file.write(self.get_kj())



calorie = Calorie(175, 70, 33, 30)
calories = calorie.kj_to_file()
