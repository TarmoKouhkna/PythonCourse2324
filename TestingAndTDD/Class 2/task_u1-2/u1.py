def process_data(input_file, output_file):
    grade_data = {}

    with open(input_file, 'r') as f:
        num_participants = int(f.readline().strip())

        for _ in range(num_participants):
            grade, step_length, *step_counts = map(int, f.readline().split())

            if all(step_counts):
                total_distance = step_length * sum(step_counts) / 100000.0

                grade_data[grade] = grade_data.get(grade, {'entries': 0, 'distance': 0})
                grade_data[grade]['entries'] += 1
                grade_data[grade]['distance'] += total_distance

    with open(output_file, 'w') as f:
        for grade, data in grade_data.items():
            f.write(f"{grade} {data['entries']} {data['distance']:.2f}\n")


process_data("u1.txt", "u1result.txt")
