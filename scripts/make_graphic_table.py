from math import sqrt
import os


def get_average_by_size(type, size, optimisation):
    with open(f"../dataset/processed_data/{type}_{optimisation}.txt", 'r') as f:
        while True:
            line = f.readline()
            if line:
                line = list(line.split(" "))
                if line[0] == size:
                    return float(line[1])
            else:
                break

def calculate_error_avg(type, size, optimisation):
    average = get_average_by_size(type, size, optimisation)
    s_sq = 0.0
    count = 0
    with open(f"../dataset/{type}/{optimisation}/{size}.txt", 'r') as f:
        while True:
            line = f.readline()
            if line:
                line = float(line)
                s_sq += (line - average)**2
                count += 1
            else:
                break
    s_sq /= (count - 1)
    s = sqrt(s_sq)
    std_err = s / (sqrt(count))
    rse = std_err / average * 100
    return rse

def get_config(file):
    config = []
    count = 0
    with open(file, 'r') as f:
        while True:
            line = f.readline().rstrip()
            if line:
                config.append([])
                config[count] = tuple(line.split(" "))
                count += 1
            else:
                break
    return config


config = get_config("./config.txt")

# print(config)
optimisations = config[0]
types = config[1]
sizes = config[3]
# print(sizes)
for type in types:
    for optimisation in optimisations:
        print(type, optimisation)
        with open(f"../dataset/processed_data/{type}_{optimisation}_tablica.txt", 'w') as f:
            for size in sizes:
                print(size)
                f.write(f"{size} {get_average_by_size(type, size, optimisation)} {calculate_error_avg(type, size, optimisation)}\n")