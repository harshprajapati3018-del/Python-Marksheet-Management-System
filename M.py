# 1. Recursion to give Grade
def get_percentage_Grade(percentage):
    if percentage >= 90:
        return "A+  (Excelent)"
    elif percentage >= 80:
        return "A (VERY GOOD)"
    elif percentage >= 70:
        return "B (VERY GOOD)"
    elif percentage >= 50:
        return "C (GOOD)"
    elif percentage >= 35:
        return "D (Pass)"
    else:
        return "FAIL"

def get_student_details():
    # Heading
    print("=" * 50)
    print(f"{'MARKS CALCULATION':^50}")
    print("=" * 50)

    # taking input from user
    student_name = input("Enter your name : ")
    Roll_number = input("Enter your roll number : ")
    student_class = input("Enter your class/Grade : ")
    
    print("-" * 50)
       
    
    subject_num = int(input("Enter Your Total Subject no.: "))

    # to convert all Subject with marks given from user
    Subject = {}

    # Loop for give inputs to user depanded on subjects no.
    for i in range(subject_num):
        print(f"\nsubject = {i + 1}")
        Subject_name = input(f"- Enter Your  Subject name: ")
        while True:
            try:
                marks = float(input("- Enter Obtained Marks: "))
                if 0 <= marks <= 100:
                    Subject[Subject_name] = marks
                    break
                else:
                    print("Invalid Marks")
            except:
                print("Invalid marks")
    # Calculation
    Total_Marks = subject_num * 100
    Marks = sum(Subject.values())
    percentage = (Marks / Total_Marks) * 100
    Grade = get_percentage_Grade(percentage)

    passed = all(marks >= 40 for marks in Subject.values())
    status = "PASS" if passed else "FAIL"
    
    # converting all outputs into Markshit
    print("=" * 50)
    print(f"{'MARKS CALCULATION':^50}")
    print("=" * 50)

    print(f"Student name : {student_name:<20} Roll No. : {Roll_number:<10} \nStudent Class : {student_class}")  

    print("-" * 50)
    print(f"{'Subject':<20} | {'Max Marks':<10} | {'Obtained':<10}")
    print("-" * 50)

    for Subject_name, marks in Subject.items():
        print(f"{Subject_name:<20} | {100:<10} | {marks:<10}")

    print("-" * 50)
    print(f"Total Marks Obtained : {Marks} / {Total_Marks}")
    print(f"Percentage           : {percentage}")
    print(f"Grade                : {Grade}")
    print(f"Result Status        : {status}")

    
    print("=" * 50)






# calling def function
get_student_details()
 