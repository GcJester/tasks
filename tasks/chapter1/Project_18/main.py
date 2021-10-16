"""Объем цилиндра может быть рассчитан путем умножения площади круга, лежащего в его основе, на высоту.
Напишите программу, в которой пользователь будет задавать радиус цилиндра и его высоту, а в ответ получать
его объем, округленный до одного знака после запятой."""

from math import pi

rad_cyl = float(input("Введите радиус цилиндра: "))
height_cyl = float(input("Введите высоту цилиндра: "))

volume_cyl = pi * rad_cyl ** 2 * height_cyl

print(f"Объём цилиндра равен: {volume_cyl:.1f} литров.")

