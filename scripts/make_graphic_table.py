from math import sqrt
import os


def get_average_by_size(type, size, optimisation, case):
    with open(f"../dataset/processed_data/{type}_{optimisation}_{case}.txt", 'r') as f:
        while True:
            line = f.readline()
            if line:
                line = list(line.split(" "))
                if line[0] == size:
                    return float(line[1])
            else:
                break

def calculate_error_avg(type, size, optimisation, case):
    average = get_average_by_size(type, size, optimisation, case)
    s_sq = 0.0
    count = 0
    with open(f"../dataset/{type}/{optimisation}/{size}_{case}.txt", 'r') as f:
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
optimisations = config[0]
types = config[1]
cases = config[2]
sizes = config[4]

for case in cases:
    for type in types:
        for optimisation in optimisations:
            with open(f"../dataset/processed_data/{type}_{optimisation}_{case}_tablica.txt", 'w') as f:
                for size in sizes:
                        f.write(f"{size} {get_average_by_size(type, size, optimisation, case)} {calculate_error_avg(type, size, optimisation, case)}\n")