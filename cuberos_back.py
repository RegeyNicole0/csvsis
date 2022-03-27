import csv
import os
import sys

student_fields = ['Student ID Number', 'Name', 'Gender','Age', 'Year Level', 'Course']
class_file = f'{sys.path[0]}/default_file.csv'
 

def disp_std():
    global student_fields
    global class_file
    
    print("--- STUDENT RECORDS ---")
    if (os.path.exists(class_file)==True):
        with open(class_file, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                for item in row:
                    print(item, end="\t ")
                print("\n")
        
        input("Press any key to continue ")
    else: 
        print("No Class File exists, making a new class file...")
        return 0

def add_std():
    print("-------------------------")
    print("ADD STUDENT INFORMATION")
    print("-------------------------")
    global student_fields
    global class_file
    
    student_data = []
    for field in student_fields:
        value = input("Enter " + field + ": ")
        student_data.append(value)
    
    with open(class_file, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])
    
    print("Studen Information added to the Class")
    input("Press any key to continue ")
    return
    
def search_std():
    global student_fields
    global class_file
    
    print("--- Search Student ---")
    id_num = input("Enter Student ID no. to search: ")
    with open(class_file, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if id_num == row[0]:
                    print("----- STUDENT FOUND -----")
                    print("Student ID Number: ", row[0])
                    print("Name: ", row[1])
                    print("Gender: ", row[2])
                    print("Age: ", row[3])
                    print("Year Level: ", row[4])
                    print("Course: ", row[5])
                    break
        else:
            print("SNo Student found in the Class!!")
    input("Press any key to continue ")
    
def edit_std():
    global student_fields
    global class_file
    
    print("--- EDIT STUDENT INFORMATION---")
    id_num = input("Enter Student ID Number to update: ")
    index_student = None
    updated_data = []
    with open(class_file, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if id_num == row[0]:
                    index_student = counter
                    print("Student Found: At index ",index_student)
                    student_data = []
                    for field in student_fields:
                        value = input("Update " + field + ": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1
    
    
        # Check if the record is found or not
    if index_student is not None:
        with open(class_file, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("No Student found in the Class!!")
    
    input("Press any key to continue ")
    
    
def delete_std():
    global student_fields
    global class_file
    
    print("--- REMOVE A STUDENT IN THE CLASS ---")
    id_num = input("Enter Student ID no. to Remove: ")
    student_found = False
    updated_data = []
    with open(class_file, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if id_num != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True
    
    if student_found is True:
        with open(class_file, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("Student", id_num, "deleted successfully")
    else:
        print("No Student found in the Class!!")
    
    input("Press any key to continue ")
