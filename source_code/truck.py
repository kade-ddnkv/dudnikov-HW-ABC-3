import random

#----------------------------------------------
# Класс-грузовик.
class Truck:
    # Стандартный конструктор.
    def __init__(self, fuel_tank_capacity, fuel_consumption, load_capacity):
        self.fuel_tank_capacity = fuel_tank_capacity
        self.fuel_consumption = fuel_consumption
        self.load_capacity = load_capacity

    # Создает грузовик со случаными реалистичными параметрами.
    def create_realistic_random_instance():
        fuel_tank_capacity = random.randint(150, 300)
        fuel_consumption = random.uniform(20, 45)
        load_capacity = random.randint(3500, 6000)
        return Truck(fuel_tank_capacity, fuel_consumption, load_capacity)
