from road_transport_dispatcher import *

#----------------------------------------------
# Метод, принимающий на вход мин-кучу, где корневой элемент может нарушать структуру.
# Изменяет мин-кучу так, чтобы она стала корректной.
# То есть опускает корневой элемент последовательными свопами на нужное место в дереве. 
def heapify(data, keys, heap_len, root_index):
	smallest = root_index
	left = root_index * 2 + 1
	right = root_index * 2 + 2

	if left < heap_len and keys[left] < keys[smallest]:
		smallest = left
	if right < heap_len and keys[right] < keys[smallest]:
		smallest = right

	if root_index != smallest:
		keys[root_index], keys[smallest] = keys[smallest], keys[root_index]
		data[root_index], data[smallest] = data[smallest], data[root_index]
		heapify(data, keys, heap_len, smallest)


# Сортирует объекты в контейнере методов пирамидальной сортировки.
def heap_sort(container):
	keys = [get_max_distance(transport) for transport in container]
	
	# Первоначальное создание мин-кучи.
	for i in range(len(container) // 2 - 1, -1, -1):
		heapify(container, keys, len(container), i)

	# Создание отсортированного массива.
	for i in range(len(container) - 1, -1, -1):
		container[0], container[i] = container[i], container[0]
		keys[0], keys[i] = keys[i], keys[0]
		heapify(container, keys, i, 0)

# Проверяет, верно ли отсортирован транспорт в контейнере.
def is_sorted_by_descending_order(container):
	keys = [get_max_distance(container[i]) for i in range(len(container))]
	return all(keys[i] >= keys[i + 1] for i in range(len(keys) - 1))