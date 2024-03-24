def centimeters_to_kilometers(centimeters):
    return centimeters / 100000.0


def process_data(input_file, output_file):
    grade_data = {}

    with open(input_file, 'r') as f:
        num_participants = int(f.readline().strip())

        for _ in range(num_participants):
            line = f.readline().strip()
            grade, step_length, *step_counts = map(int, line.split())

            if all(step_counts):

                total_steps = sum(step_counts)
                total_distance = centimeters_to_kilometers(step_length * total_steps)

                if grade in grade_data:
                    grade_data[grade]['entries'] += 1
                    grade_data[grade]['distance'] += total_distance
                else:
                    grade_data[grade] = {'entries': 1, 'distance': total_distance}

    with open(output_file, 'w') as f:
        for grade, data in grade_data.items():
            data = grade_data.get(grade, {'entries': 0, 'distance': 0})
            f.write(f"{grade} {data['entries']} {data['distance']:.2f}\n")


process_data("u1.txt", "u1result.txt")
