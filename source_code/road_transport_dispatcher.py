import random

from truck import *
from bus import *
from car import *

# Этот файл предназначен для методов, общих для всего дорожного транспорта.
#----------------------------------------------
# Словарь - диспетчер классов.
dispatch_dict = {'t': Truck, 'b': Bus, 'c': Car}

# Создает транспорт по переданным параметрам.
def create_road_transport(input):
    str_array = input.split(" ")
    # Проверка корректности введенного транспорта.
    try:
        assert int(str_array[1]) >= 1 and float(str_array[2]) >= 1 and int(str_array[3]) >= 1 and str_array[0] in dispatch_dict.keys()
    except:
        raise ValueError(input)
    # Создается новый экземпляр нужного класса.
    return dispatch_dict[str_array[0]](int(str_array[1]), float(str_array[2]), int(str_array[3]))

# Создает случайный транспорт (с реалистичными/нереалистичными параметрами).
def create_random_road_transport(realistic_random):
    selected_class = dispatch_dict[random.choice(['t', 'b', 'c'])]
    if realistic_random:
        return selected_class.create_realistic_random_instance()
    else:
        # В 3 питоне у int нет границ.
        left = 1
        right = 2147483647 # Это максимальное значение int32_t в C++. 
        return selected_class(random.randint(left, right), random.uniform(left, right), random.randint(left, right))

# Общий для всех классов метод.
def get_max_distance(transport):
    return transport.fuel_tank_capacity / (transport.fuel_consumption / 100.0)