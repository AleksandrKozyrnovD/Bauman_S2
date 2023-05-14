import os
from math import log

values = []
lines = []
with open("../dataset/processed_data/1_O2_1.txt", 'r') as f:
    while True:
        line = f.readline()
        if line:
            lines.append(list(map(float, line.split(" ")))[:2])
        else:
            break


for i in range(len(lines) - 1):
    values.append((log(lines[i + 1][1]) - log(lines[i][1])) / (log(lines[i + 1][0]) - log(lines[i][0])))

print(len(lines), len(values))
with open("../dataset/processed_data/collected_table_data.txt", 'w') as f:
    for i in range(len(lines) - 1):
        f.write(" ".join(map(str, lines[i])) + " " + str(values[i]) +  "\n")  