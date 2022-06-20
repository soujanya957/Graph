import csv

x_data = []
y_data = []

print('hello')
with open("data.txt", "r") as file:
    csv_reader = csv.reader(file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            x = row[0]
            y = row[1]
            print(x,y)
            line_count += 1
        else:
            x_data.append(row[0])
            y_data.append(row[1])
            print(f"{row[0]}, {row[1]}")
            line_count += 1
    print("num of lines: ", line_count)
    print(x_data)
    print(y_data)