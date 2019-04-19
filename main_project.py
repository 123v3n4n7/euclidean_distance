import csv
from scipy.spatial import distance
import matplotlib.pyplot as plt


def csv_reader():
    with open('vectors.csv', 'r') as file:
        vector_matrix = []
        reader = csv.reader(file)
        for line in reader:
            line_vector = []
            for i in line:
                line_vector.append(float(i))
            vector_matrix.append(line_vector)
        return vector_matrix


def euclidean_distance(vector_array):
    mx = vector_array
    distances = []
    for i in range(len(mx)):
        for j in range(i+1, len(mx)):
            distances.append(distance.euclidean(mx[i], mx[j]))
    max_dist = max(distances)
    min_dist = min(distances)
    hist_maker(distances)
    return max_dist, min_dist


def hist_maker(mx):
    bins = []
    x = float(0)
    for i in range(len(mx)):
        x += 0.1
        bins.append(round(x, 1))
    plt.hist(mx, bins, histtype='bar')
    plt.ylabel('Частота')
    plt.xlabel('Шаг')
    plt.xticks(bins)
    plt.show()
    #plt.savefig('graph.svg')


if __name__ == "__main__":
    matrix = csv_reader()
    max_distance, min_distance = euclidean_distance(matrix)
    print(max_distance, min_distance)
