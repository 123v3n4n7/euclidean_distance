Тестовое задание:
Даны два числа N и m, 500&lt;N≤1000, 10&lt;m≤50
Программа 1 (формирование исходных данных):
По переданным числам N и m заполнить текстовый файл vectors.csv, состоящий из N строк,
в каждой из которых m случайных чисел с плавающей точкой, каждое в диапазоне от -1 до +1,
разделённых запятыми.
Программа 2 (основное задание):
На вход подаётся файл vectors.csv, созданный Программой 1. Каждая строка файла
рассматривается как m-мерный вектор. Таким образом, получаем N векторов. Требуется
вычислить евклидово расстояние между всеми парами различных векторов этого списка, и найти
минимальное и максимальное расстояния, а также распределение расстояний.
Дополнительное требование по использованию памяти: недопустимо создавать
структуры данных размером более N x m элементов (больше, чем размер входного списка
векторов).
Результат выводится в виде:
 номера векторов пары с минимальным расстоянием, и значение этого расстояния;
 номера векторов пары с максимальным расстоянием, и значение этого расстояния;
 изображение гистограммы распределения расстояний с шагом 0.1.
