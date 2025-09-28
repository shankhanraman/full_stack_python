class Chaicup:
    size = 50 # ml

    def describe(self):
        return f"A {self.size} ml chai cup"

cup = Chaicup()
print(cup.describe())
# print(Chaicup.describe()) it will led to error as it does not knwo who is calling
print(Chaicup.describe(cup))

cup_two = Chaicup()
cup_two.size = 100
# print(cup_two.describe())
print(Chaicup.describe(cup_two))