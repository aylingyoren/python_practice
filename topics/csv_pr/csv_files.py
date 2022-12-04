import csv

# Write CSV with DictWriter

# with open('students1.csv', 'w') as file:
#     headers_list = ["First name", "Last name", "Age"]
#     csv_writer = csv.DictWriter(file, fieldnames=headers_list)
#     csv_writer.writeheader()
#     csv_writer.writerow({"First name": "Aylin", "Last name": "Gyoren", "Age": 27})
#     csv_writer.writerow({"First name": "Margaret", "Last name": "Przewskich", "Age": 41})

# Open existing file and write from it

# with open(r"/Users/aylingyoren/Desktop/IT/Python/Apps/untitled/topics/csv/students.csv") as f:
#     csv_reader = csv.DictReader(f)
#     students_list = list(csv_reader)
#
# with open("students2.csv", "w") as f:
#     header_list = ["Name", "Surname"]
#     csv_writer = csv.DictWriter(f, fieldnames=header_list)
#     csv_writer.writeheader()
#     for student in students_list:
#         csv_writer.writerow({"Name": student["First name"], "Surname": student["Last name"]})

# Write CSV with (list) writer

# with open('students.csv', 'w') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(["First name", "Last name", "Age"])
#     csv_writer.writerow(["Aylin", "Gyoren", 27])
#     csv_writer.writerow(["Margaret", "Przewskich", 41])
#     csv_writer.writerows([["Vasya", "Pupkin", 35], ["Michael", "Jerou", 18]])   # ???????
#
# with open('students.csv') as file:
#     csv_reader = csv.reader(file)
#     next(csv_reader)
#     for student in csv_reader:
#         print(student)

# with open(r"/Users/aylingyoren/Desktop/IT/Python/Apps/untitled/topics/csv/cars.csv") as file:
#     csv_reader = csv.reader(file)
#     next(csv_reader)
#     make_model_list = []
#     for car in csv_reader:
#         make_model = [car[1], car[2]]
#         make_model_list.append(make_model)
#     print(make_model_list)

# with open("make_model.csv", "w") as f:
#     csv_writer = csv.writer(f)
#     for row in make_model_list:
#         csv_writer.writerow(row)

# Read CSV with (list) writer & DictReader

# with open("cars.csv") as file:
#     csv_reader = csv.reader(file)
#     next(csv_reader)
#     i = 1
#     for car in csv_reader:
#         print(f"{i}. Car: {car[1]} {car[2]}, year: {car[0]}, price: {car[4]}")
#         i += 1
#     cars_list = list(csv_reader)
#     print(cars_list)

# with open("cars.csv") as file:
#     csv_reader = csv.DictReader(file)
#     for car in csv_reader:
#         print(f"Car: {car['Make']} {car['Model']}, year: {car['Year']}, price: {car['Price']}")

# with open(r"/Users/aylingyoren/Desktop/IT/Python/Apps/untitled/topics/csv/cars1.csv") as file:
#     csv_reader = csv.DictReader(file, delimiter=";")
#     for car in csv_reader:
#         print(f"Car: {car['Make']} {car['Model']} is {car['Length']} meters")

# HW add_student()

# Создайте функцию add_student(), которая принимает в качестве параметров
# имя, фамилию и возраст и добавляет запись в файл students.csv.
# При необходимости воспользуйтесь поиском информации в интернете

# def add_student(name, surname, age):
#     with open("students.csv", "a") as file:
#         csv_writer = csv.writer(file)
#         csv_writer.writerow([name, surname, age])
#     print(f"{name} {surname} ({age}) successfully written")

# add_student("George", "Wasly", 26)
# add_student("Edward", "Cullen", 117)

# HW print_students()
def print_students():
    with open("students.csv") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for student in csv_reader:
            print(student)
            # print(f"{student[0]} {student[1]} ({student[2]})")

print_students()
