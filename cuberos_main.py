"""
        ASSIGNMENT IN CCC15
Create a Simple STUDENT INFORMATION SYSTEM that:
    - Display list of students
    - Add new students
    - Edit student
    - Delete a student
    - Search a student by id number

REGGIE NICOLE C. CUBEROS            2020-0596
"""
import cuberos_back as cb

if __name__ == '__main__':

    print(""" 
  ------------------------------------------------------
 |======================================================| 
 |========  SIMPLE STUDENT INFORMATION SYSTEM	========|
 |======================================================|
  ------------------------------------------------------
  """)
    print("PRESS 1 : TO DISPLAY STUDENT LIST")
    print("PRESS 2 : TO ADD A NEW STUDENT")
    print("PRESS 3 : TO SEARCH FOR A STUDENT")
    print("PRESS 4 : TO UPDATE STUDENT INFORMATION")
    print("PRESS 5 : TO REMOVE A STUDENT")
    print("PRESS 6 : TO EXIT")

    run=True
    while run:
        choice=int(input("ENTER YOUR CHOICE : "))
        if choice == 1:
            cb.disp_std()
        elif choice == 2:
            cb.add_std()
        elif choice == 3:
            cb.search_std()
        elif choice == 4:
            cb.edit_std()
        elif choice == 5:
            cb.delete_std()
        elif choice == 6:
            print("-------------------------------")
            print(" THANK YOU FOR USING THE SYSTEM ")
            print("-------------------------------")
            run = False
        else:
            print("PLEASE CHOOSE CORRECT OPTION FROM THE FOLLOWING.")
            print("\n")
    
    