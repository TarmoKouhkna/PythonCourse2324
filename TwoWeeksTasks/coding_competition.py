# Read data from the file
with open('coding_competition.txt', 'r') as file:
    lines = file.readlines()

# Extract the relevant information
num_participants = int(lines[0])
max_time_per_task = list(map(int, lines[1].split()))
max_points_per_task = list(map(int, lines[2].split()))
participants_data = [line.strip().split() for line in lines[3:]]

# Calculate points for each participant
participants_points = []
for participant in participants_data:
    points = 0
    for i, time in enumerate(participant[1:]):
        if time != '0':
            points += max_points_per_task[i]
    participants_points.append((participant[0], points))

# Find the most points collected and list participants
max_points = max([points for name, points in participants_points])
participants_with_max_points = [index for index, (name, points) in enumerate(participants_points) if points == max_points]
participants_with_max_points.sort(key=lambda x: participants_points[x][1], reverse=True)

# Output the expected result
print(max_points)
for index in participants_with_max_points:
    print(participants_points[index][0], ' '.join(participants_data[index][1:]))
    