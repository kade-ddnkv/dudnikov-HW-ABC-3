import sys
import string
import time

from error_messages import *
from road_transport_dispatcher import *
from heap_sorting import *

# Записывает информацию из контейнера в файл.
def write_to_file(container, ofile):
    headers = ['TYPE', 'MAX_DISTANCE', 'FUEL_CAP', 'FUEL_CONS', 'ADDITIONAL_INFO']
    # Устанавливаются форматы строк для вывода в виде таблицы.
    header_format = "{:<7}{:<16}{:<14}{:<14}{:<34}"
    row_format = "{:<7}{:<16.2f}{:<14}{:<14.2f}{:<20}{:<14}"
    ofile.write(f'Total objects in container: {len(container)}\n')
    ofile.write(header_format.format(*headers))
    ofile.write('\n')
    for transport in container:
        # Вывод данных траснорта (некоторые данные получаются через рефлексию).
        ofile.write(row_format.format(
            type(transport).__name__.lower(),       # тип транспорта
            get_max_distance(transport),            # максимальная дистанция
            transport.fuel_tank_capacity,           # объем топливного бака
            transport.fuel_consumption,             # расход топлива
            list(transport.__dict__.keys())[2],     # название доп. информации
            list(transport.__dict__.values())[2]))  # значение доп. информации
        ofile.write('\n')

# Записывает в файл заголовок, обрамленный горизонтальными линиями.
def write_title(title, ofile):
    ofile.write('-' * 85 + '\n')
    ofile.write(f'{title}\n')
    ofile.write('-' * 85 + '\n')

# Главный управляющий метод - main.
#----------------------------------------------
if __name__ == '__main__':
    if len(sys.argv) < 3:
        help()
        exit()

    start_of_reading_time = time.time()
    
    # Считывание данных из файла.
    if sys.argv[1] == '-f':
        # При считывании из файла при некорректных данных программа выбрасывает исключение ValueError. 
        # Внутри исключения указана строка, на которой произошла ошибка.
        try:
            input_file_name = sys.argv[2]
            output_file_name = sys.argv[3]
            ifile = open(input_file_name, "r")
            container = [create_road_transport(x.replace("\n", "")) for x in ifile.readlines()]
        except ValueError as exc:
            print('Some value in input file is incorrect (for example, is not a number or is less than 1).')
            print(f'Check line "{exc}"')
            ifile.close()
            exit()
        except:
            print('Unexpected exception handled. Check input file.')
            ifile.close()
            exit()

    # Автоматическая генерация данных.
    elif sys.argv[1] == '-r':
        container = []
        if not (sys.argv[2].isdigit() and int(sys.argv[2]) >= 1 and int(sys.argv[2]) <= 10000):
            err_message_incorrect_number()
            exit()
        if sys.argv[3] not in ['1', '0']:
            err_message_incorrect_realistic_random()
            exit()
        for i in range(int(sys.argv[2])):
            container.append(create_random_road_transport(sys.argv[3] == '1'))
        output_file_name = sys.argv[4]

    # Иначе команда запуска программы некорректна.
    else:
        err_message_incorrect_command()
        exit()

    print('==> Start')
    print(f'--- Read/generate time: {time.time() - start_of_reading_time :.3f} seconds ---')

    start_of_sorting_time = time.time()
    
    # Запись информации в файл, сортировка и снова запись.
    ofile = open(output_file_name, 'w')
    write_title('Entered data', ofile)
    write_to_file(container, ofile)
    write_title('After heap sort', ofile)
    heap_sort(container)
    ofile.write(f'Is correctly sorted: {"YES" if is_sorted_by_descending_order(container) else "NO"}\n')
    write_to_file(container, ofile)
    ofile.close()

    print(f'--- Sort and print time: {time.time() - start_of_sorting_time :.3f} seconds ---')
    print('==> Finish')

    print(type(container[0]))
    print(type(dispatch_dict['t']))
    print(type(ofile))
    print(type(1 == 2))
