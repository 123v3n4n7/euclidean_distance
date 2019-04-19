import csv
import numpy
import random


def write_csv(matrix):
    with open('vectors.csv', 'a') as file:
        writer = csv.writer(file)
        for vector in matrix:
            writer.writerow(vector)


def data_maker():
    # n = random.randint(500, 1000)
    # m = random.randint(10, 50)
    n = 20
    m = 10
    vectors_array = numpy.random.uniform(-1, 1, (n, m))
    return vectors_array


if __name__ == "__main__":
    vector_matrix = data_maker()
    with open('vectors.csv', 'w+') as f:
        line = f.readline()
        if len(line) > 0:
            f.truncate()
    write_csv(vector_matrix)
