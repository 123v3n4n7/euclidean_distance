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
    t = []
    for i in range(len(mx)):
        for j in range(i+1, len(mx)):
            distances.append(distance.euclidean(mx[i], mx[j]))
            t.append([i, j])
    max_dist = max(distances)
    min_dist = min(distances)
    para_min = t[distances.index(min(distances))][0], t[distances.index(min(distances))][1]
    para_max = t[distances.index(max(distances))][0], t[distances.index(max(distances))][1]
    # print(para_min, para_max)
    #print(distance.euclidean(mx[para_min[0]], mx[para_min[1]]))
    # print(distance.euclidean(mx[para_max[0]], mx[para_max[1]]))
    hist_maker(distances)
    return (max_dist, para_max), (min_dist, para_min)


def hist_maker(mx):
    bins = []
    x = float(0)
    for i in range(int(round(max(mx))*10)):
        bins.append(round(x, 1))
        x += 0.1
    plt.yticks()
    plt.xticks()
    plt.ylabel('Частота')
    plt.xlabel('Шаг')
    plt.hist(mx, bins=bins, color='red')
    plt.show()
    #plt.savefig('graph.svg')
    #print(max(mx))


if __name__ == "__main__":
    matrix = csv_reader()
    max_distance, min_distance = euclidean_distance(matrix)
    print(max_distance, min_distance)
