import os

#processing data
def process_data(array: list):
    lenght = len(array)
    array.sort()
    average = sum(array) / len(array)
    median = array[lenght // 2 + lenght % 2]
    quartil1 = array[lenght // 4]
    quartil3 = array[(lenght // 4) * 3]

    return average, array[0], quartil1, median, quartil3, array[lenght - 1]


DATASETS = "../dataset/"
for directory in os.listdir(DATASETS):
    if directory != "processed_data":
        for subdirectory in os.listdir(DATASETS + directory):
            for sort_types in ["1", "2"]:
                proc_data = []
                for file in os.listdir(DATASETS + directory + "/" + subdirectory):
                    if "_" + sort_types in file: 
                        with open(DATASETS + directory + "/" + subdirectory + "/" + file, 'r') as data:
                            array_of_data = [int(rows.rstrip()) for rows in data]
                        proc_data.append([int(file[:-6]), process_data(array_of_data)])
                        # print(proc_data)

                proc_data = sorted(proc_data, key=lambda x: x[0])
                # print(proc_data)
                with open(DATASETS + "processed_data/" + directory + "_" + subdirectory + "_" + sort_types + ".txt", 'w') as outputfile:
                    for proc in proc_data:
                        outputfile.write("".join(str(proc[0]))+ " ")
                        outputfile.write(" ".join(map(str, proc[1])) + "\n")