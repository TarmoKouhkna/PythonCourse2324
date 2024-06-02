import threading


def matrix_multiply(A, B, result, start_row, end_row):
    for i in range(start_row, end_row):
        for j in range(len(B[0])):
            result[i][j] = 0
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]


def parallel_matrix_multiply(A, B, num_threads=4):
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in the first matrix must equal the number of rows in the second matrix")

    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    threads = []
    rows_per_thread = len(A) // num_threads

    for i in range(num_threads):
        start_row = i * rows_per_thread
        end_row = start_row + rows_per_thread if i < num_threads - 1 else len(A)
        thread = threading.Thread(target=matrix_multiply, args=(A, B, result, start_row, end_row))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return result


if __name__ == "__main__":
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    B = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]

    result = parallel_matrix_multiply(A, B)
    for row in result:
        print(row)
