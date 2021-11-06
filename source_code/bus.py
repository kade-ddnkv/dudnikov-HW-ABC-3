import random

#----------------------------------------------
# Класс-автобус.
class Bus:
    # Стандартный конструктор.
    def __init__(self, fuel_tank_capacity, fuel_consumption, passenger_capacity):
        self.fuel_tank_capacity = fuel_tank_capacity
        self.fuel_consumption = fuel_consumption
        self.passenger_capacity = passenger_capacity

    # Создает автобус со случаными реалистичными параметрами.
    def create_realistic_random_instance():
        fuel_tank_capacity = random.randint(150, 300)
        fuel_consumption = random.uniform(18, 35)
        passenger_capacity = random.randint(10, 80)
        return Bus(fuel_tank_capacity, fuel_consumption, passenger_capacity)
