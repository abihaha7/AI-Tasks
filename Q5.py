class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"🚗 Vehicle: {self.brand} {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

class SportsCar(Car):
    def __init__(self, brand, model, doors, top_speed):
        super().__init__(brand, model, doors)
        self.top_speed = top_speed

# Example Usage
sportscar = SportsCar("Ferrari", "F8", 2, 340)
sportscar.display_info()
