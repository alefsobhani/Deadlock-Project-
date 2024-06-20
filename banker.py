import numpy as np

def is_safe(available, max_matrix, allocation_matrix):
    num_processes, num_resources = max_matrix.shape
    need = max_matrix - allocation_matrix
    work = available.copy()
    finish = [False] * num_processes

    while True:
        allocated = False
        for i in range(num_processes):
            if not finish[i] and all(need[i] <= work):
                work += allocation_matrix[i]
                finish[i] = True
                allocated = True
                break
        if not allocated:
            break

    return all(finish)

available = np.array([3, 3, 2])
max_matrix = np.array([[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]])
allocation_matrix = np.array([[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]])

if is_safe(available, max_matrix, allocation_matrix):
    print("The system is in a safe state")
else:
    print("The system is not in a safe state")
