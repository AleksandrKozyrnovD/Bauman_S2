import os

#processing data
def process_data(array: list):
    lenght = len(array)
    array.sort()
    average = sum(array) / len(array)
    if lenght == 1:
        median = array[0]
    else:
        median = array[lenght // 2 + lenght % 2]
    quartil1 = array[lenght // 4]
    quartil3 = array[(lenght // 4) * 3]

    return average, array[0], quartil1, median, quartil3, array[lenght - 1]


DATASETS = "../dataset/"
for directory in os.listdir(DATASETS):
    if directory != "processed_data":
        for subdirectory in os.listdir(f"{DATASETS}{directory}"):
            proc_data = []
            for file in os.listdir(f"{DATASETS}{directory}/{subdirectory}"):
                    if ".txt" in file:
                        with open(f"{DATASETS}{directory}/{subdirectory}/{file}", 'r') as data:
                            array_of_data = [int(rows.rstrip()) for rows in data]
                        # print(file)
                        proc_data.append([int(file[:-4]), process_data(array_of_data)])
                        # print(proc_data)

            proc_data = sorted(proc_data, key=lambda x: x[0])
            # print(proc_data)
            with open(f"{DATASETS}processed_data/{directory}_{subdirectory}.txt", 'w') as outputfile:
                for proc in proc_data:
                    #Write column of size of the input data
                    outputfile.write("".join(str(proc[0])) + " ")
                    #Write columns with these:
                    #average, minimum, lowerquartile, median, upperquartile, maximum
                    outputfile.write(" ".join(map(str, proc[1])) + "\n")