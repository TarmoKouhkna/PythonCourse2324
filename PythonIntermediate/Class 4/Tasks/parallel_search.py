import multiprocessing


# Define the function to search for the target value in a chunk of data
def search_chunk(chunk, target, offset, result_queue):
    found_indices = []
    for i, value in enumerate(chunk):
        if value == target:
            found_indices.append(i + offset)
    result_queue.put(found_indices)


# Define the main function for parallel search
def parallel_search(data, target, num_processes=4):
    # Divide the data into chunks
    chunk_size = len(data) // num_processes
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    # Create a multiprocessing Queue to collect results from processes
    result_queue = multiprocessing.Queue()

    # Create processes for searching each chunk
    processes = []
    for i, chunk in enumerate(chunks):
        process = multiprocessing.Process(target=search_chunk, args=(chunk, target, i * chunk_size, result_queue))
        processes.append(process)
        process.start()

    # Join processes
    for process in processes:
        process.join()

    # Collect results from the queue
    found_indices = []
    while not result_queue.empty():
        found_indices.extend(result_queue.get())

    return found_indices


if __name__ == "__main__":
    # Example usage with a dataset where the target value appears multiple times
    data = [1, 2, 3, 7, 5, 7, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    target = 7
    found_indices = parallel_search(data, target)
    print("Indices where target value is found:", found_indices)
