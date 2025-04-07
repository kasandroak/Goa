class Car:
    def __init__(self, make, model, year, color):
        self.make, self.model, self.year, self.color = make, model, year, color

    def start_engine(self): return f"{self.make} {self.model}-ის ძრავა მუშაობს."
    def stop_engine(self): return f"{self.make} {self.model}-ის ძრავა გაჩერებულია."


class Person:
    total_people = 0

    def __init__(self, name, age, occupation):
        self.name, self.age, self.occupation = name, age, occupation
        Person.total_people += 1

    def introduce(self): return f"გამარჯობა, მე {self.name} ვარ, {self.age} წლის."
    def celebrate_birthday(self): self.age += 1; return f"{self.name} დაბადების დღეს გილოცავთ! ახლა {self.age} წლისაა."


# Testing Car class
car1 = Car("Toyota", "Corolla", 2020, "წითელი")
car2 = Car("Honda", "Civic", 2022, "ლურჯი")
print("Car objects:")
for car in [car1, car2]:
    print(f"{car.make} {car.model}: {car.start_engine()} - {car.stop_engine()}")

# Testing Person class
person1 = Person("გიო", 30, "ინჟინერი")
person2 = Person("მარიამი", 28, "მასწავლებელი")
print("\nPerson objects:")
for person in [person1, person2]:
    print(person.introduce(), person.celebrate_birthday(), f"ჯამში: {Person.total_people} ადამიანი")
