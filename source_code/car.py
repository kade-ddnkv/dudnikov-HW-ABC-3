import random

#----------------------------------------------
# Класс-машина.
class Car:
    # Стандартный конструктор.
    def __init__(self, fuel_tank_capacity, fuel_consumption, max_speed):
        self.fuel_tank_capacity = fuel_tank_capacity
        self.fuel_consumption = fuel_consumption
        self.max_speed = max_speed

    # Создает машину со случаными реалистичными параметрами.
    def create_realistic_random_instance():
        fuel_tank_capacity = random.randint(50, 90)
        fuel_consumption = random.uniform(5, 9)
        max_speed = random.randint(160, 190)
        return Car(fuel_tank_capacity, fuel_consumption, max_speed)
