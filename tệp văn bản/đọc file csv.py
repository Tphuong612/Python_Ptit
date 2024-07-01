import csv

#cách 1 dung hàm csv.reader()
with open(r"tệp văn bản\test.csv", "r") as csv_file1:
    csv_reader = csv.reader(csv_file1)
    for row in csv_reader:
        # if row[0] == "Parker":
        #     print(*row)
        print(row)
            
#cách 2 dùng hàm csv.dictReader()
with open(r"tệp văn bản\test.csv", "r") as csv_file2:
    csv_reader2 = csv.DictReader(csv_file2)
    for row in csv_reader2:
        # if row['name'] == "Parker":
        #     print(*row.values())
        #     break
        print(row)
