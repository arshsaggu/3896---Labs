import time, random

def dict_timer(sample):
    if 1111111 in sample:
        return True
    else:
        return False


sample_dict = {}
for _ in range(1000000):
    key = random.randint(0, 1000000)
    value = random.randint(0, 1000000)
    sample_dict[key] = value

initial = time.perf_counter()
dict_timer(sample_dict)
final = time.perf_counter()

mean_time_in_microseconds = f"{(final - initial)*1_000_000:.6f}"

with open('new_file', 'a') as file:
    file.write(f"{mean_time_in_microseconds}\n")

with open('new_file', 'r') as f:
    lines = f.readlines()

if len(lines) == 15:
    numbers_for_mean = []
    for every_line in lines:
        new_line = float(every_line.strip())
        numbers_for_mean.append(new_line)
    mean_of_lines = sum(numbers_for_mean)/len(numbers_for_mean)
    with open('new_file_for_mean', 'a') as file:
        file.write(f"18. {mean_of_lines:.6f}\n")