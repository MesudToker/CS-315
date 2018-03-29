import numpy as np
global adj_list

def adjacency_generator(file_name):
    data_file = open(file_name, 'r')

    data_file.readline()
    num_nodes = int(data_file.readline())

    s = data_file.readline()
    while (not "edges" in s):
        s = data_file.readline()

    for line in data_file:
        arr = [int(s) for s in line.split() if s.isdigit()]
        adj_list.append(arr[:2])

    matrix_a = np.matrix([[0]* num_nodes] * num_nodes)
    
    for elem in adj_list:
        matrix_a[elem[0], elem[1]] = 1
        matrix_a[elem[1], elem[0]] = 1


def num_paths(adj_list, m):
    num_nodes = len(adj_list)
    matrix_a = np.matrix([[0]* num_nodes] * num_nodes)
    
    for elem in adj_list:
        matrix_a[elem[0], elem[1]] = 1
        matrix_a[elem[1], elem[0]] = 1

    for i in range(0, m - 1):
        matrix_a = np.dot(matrix_a, matrix_a)

    print(matrix_a)
    
adj_list = []
adjacency_generator('input.txt')
num_paths(adj_list, 3)