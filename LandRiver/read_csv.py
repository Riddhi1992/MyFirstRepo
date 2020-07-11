import csv


def read():
    data = []
    csv_file = open("Task_Training_Data.csv", "r")
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
        data.append([line[0], line[1]])

    # print(data)
    return data


read()
