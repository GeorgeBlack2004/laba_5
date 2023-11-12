import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

x = np.array([3.567, -5])
a_values = (-5, -2.5, 0, 2.5, 5, 7.5, 10)
y_values = np.sin(x/3) + 1.2*np.asarray(a_values)

print("Аргументы (x):", x)
print("Значения функции (f(x)):", y_values)

max_value = np.max(y_values)
min_value = np.min(y_values)
mean_value = np.mean(y_values)
num_elements = len(y_values)

if num_elements % 2 == 0:
    y_values_sorted = np.sort(y_values)[::-1]
else:
    y_values_sorted = np.sort(y_values)

plt.figure(figsize=(10, 6))

plt.plot(a_values, y_values, marker='o', linestyle='-', label='f(x) = sin(x/3) + 1.2a')
plt.xlabel('Значение a')
plt.ylabel('f(x)')
plt.title('Изменение значений функции f(x)')
plt.legend()
plt.grid(True)

plt.axhline(y=mean_value, color='r', linestyle='--', label=f'Среднее ({mean_value:.2f})', linewidth=2)
plt.legend()

plt.show()

print("Наибольшее значение функции:", max_value)
print("Наименьшее значение функции:", min_value)
print("Среднее значение функции:", mean_value)
print("Количество элементов в массиве:", num_elements)
print("Отсортированный массив значений функции:", y_values_sorted)
