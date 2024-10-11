from collections import deque


course_ids = [701, 702,703, 704,705, 706,707, 708,709, 710,711, 712,713, 714,715, 716,717, 718,719, 720]

course_details = { 
    701: {"CourseName": "Data Structures", "Instructor": "Prof. Smith", "SeatsAvailable": 30, "EnrolledStudents": []},
    702: {"CourseName": "Algorithms", "Instructor": "Prof. Johnson", "SeatsAvailable": 25, "EnrolledStudents": []},
    703: {"CourseName": "English", "Instructor": "Prof. Assoumpta", "SeatsAvailable": 45, "EnrolledStudents": []},
    704: {"CourseName": "Kiswahili", "Instructor": "Prof. James", "SeatsAvailable": 55, "EnrolledStudents": []},
    705: {"CourseName": "French", "Instructor": "Prof. Serge", "SeatsAvailable": 20, "EnrolledStudents": []},
    706: {"CourseName": "Statistics", "Instructor": "Prof. Caleb", "SeatsAvailable": 15, "EnrolledStudents": []},
    707: {"CourseName": "System Engineering", "Instructor": "Prof. John", "SeatsAvailable": 16, "EnrolledStudents": []},
    708: {"CourseName": "Database", "Instructor": "Prof. Peterson", "SeatsAvailable": 24, "EnrolledStudents": []},
    709: {"CourseName": "Business functions", "Instructor": "Prof. Wilson", "SeatsAvailable": 60, "EnrolledStudents": []},
    710: {"CourseName": "Kinyarwanda", "Instructor": "Prof. Edson", "SeatsAvailable": 90, "EnrolledStudents": []},
    711: {"CourseName": "Economics", "Instructor": "Prof. Emason", "SeatsAvailable": 50, "EnrolledStudents": []},
    712: {"CourseName": "Accounting", "Instructor": "Prof. Allan", "SeatsAvailable": 40, "EnrolledStudents": []},
    713: {"CourseName": "Political Science", "Instructor": "Prof. Eric", "SeatsAvailable": 35, "EnrolledStudents": []},
    714: {"CourseName": "Logistics", "Instructor": "Prof. Kevin", "SeatsAvailable": 10, "EnrolledStudents": []},
    715: {"CourseName": "Business Management", "Instructor": "Prof. Felicite", "SeatsAvailable": 39, "EnrolledStudents": []},
    716: {"CourseName": "Javascript", "Instructor": "Prof. Kenny", "SeatsAvailable": 70, "EnrolledStudents": []},
    717: {"CourseName": "C++ Programming", "Instructor": "Prof. Jean", "SeatsAvailable": 95, "EnrolledStudents": []},
    718: {"CourseName": "ICT", "Instructor": "Prof. Patrick", "SeatsAvailable": 80, "EnrolledStudents": []},
    719: {"CourseName": "Math", "Instructor": "Prof. Ivan", "SeatsAvailable": 100, "EnrolledStudents": []},
    720: {"CourseName": "Scientific work", "Instructor": "Prof. Queen", "SeatsAvailable": 67, "EnrolledStudents": []}
}


undo_stack = []

registration_queue = deque()  


def display_courses():
    print("{:<10} {:<20} {:<15} {:<15}".format("CourseID", "CourseName", "Instructor", "SeatsAvailable"))
    print("-" * 60)

    for course_id in course_ids:
        details = course_details[course_id]
        print("{:<10} {:<20} {:<15} {:<15}".format(
            course_id, details["CourseName"], details["Instructor"], details["SeatsAvailable"]))
    print()


def display_enrolled_students(course_id):
    if course_id in course_details:
        enrolled_students = course_details[course_id]["EnrolledStudents"]
        print(f"Enrolled students in {course_details[course_id]['CourseName']}:")
        print("{:<15}".format("Student Name"))
        print("-" * 12)

        for student in enrolled_students:
            print(f"- {student}")
        if not enrolled_students:
            print("No students enrolled yet.")
    else:
        print("Invalid course ID.")
    print()


def enroll_student(student_name, course_id):
    if course_id in course_details and course_details[course_id]["SeatsAvailable"] > 0:
        course_details[course_id]["EnrolledStudents"].append(student_name)
        course_details[course_id]["SeatsAvailable"] -= 1
        undo_stack.append((student_name, course_id))  
        print(f"{student_name} enrolled in {course_details[course_id]['CourseName']}.")
    else:
        print(f"Unable to enroll {student_name}. No seats available or invalid course ID.")
    print()

def undo_last_enrollment():
    if undo_stack:
        student_name, course_id = undo_stack.pop()
        course_details[course_id]["EnrolledStudents"].remove(student_name)
        course_details[course_id]["SeatsAvailable"] += 1
        print(f"Undo enrollment: {student_name} removed from {course_details[course_id]['CourseName']}.")
    else:
        print("No enrollments to undo.")
    print()

def add_to_registration_queue(student_name):
    registration_queue.append(student_name)
    print(f"{student_name} added to registration queue.")
    print()

def confirm_registration(course_id):
    if registration_queue:
        student_name = registration_queue.popleft()
        enroll_student(student_name, course_id)
    else:
        print("No students in the registration queue.")
    print()


def main():
    while True:
        print("\nMenu: ")
        print("1. Enroll in a course")
        print("2. Undo last enrollment")
        print("3. Add a student on registration queue")
        print("4. Enroll student in registration queue")
        print("5. Display all courses")
        print("6. Display students enrolled in a course.")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            student_name = input("Enter student name: ")
            course = int(input("Enter course ID to enroll: "))
            print()
            enroll_student(student_name, course)

        elif choice == '2':
            undo_last_enrollment()

        elif choice == '3':
            student_name = input("Enter student name to add on a registration queue: ")
            print()
            add_to_registration_queue(student_name)

        elif choice == '4':
            course_id = int(input("Enter course ID to enroll a student from queue: "))
            print()
            confirm_registration(course_id)

        elif choice == '5':
            display_courses()

        elif choice == '6':
            course_id = int(input("Enter course ID to display students enrolled: "))
            print()
            display_enrolled_students(course_id)
            

        elif choice == '7':
            break

        else:
            print("Invalid option. Please try again.")



enroll_student("Alice", 701)  
enroll_student("Bob", 702)    
enroll_student("James", 701)    
enroll_student("John", 702)    
enroll_student("Claude", 702)    
enroll_student("Jack", 701)    
enroll_student("Paul", 701)    
enroll_student("Peter", 701)    
enroll_student("Smith", 702)    
enroll_student("Wilson", 702) 
enroll_student("allan", 703)    
enroll_student("claudien", 704)    
enroll_student("Jackline", 705)    
enroll_student("Pauline", 706)    
enroll_student("Peterine", 707)    
enroll_student("Smithson", 708)    
enroll_student("Wiliam", 709) 

enroll_student("Anice", 711)  
enroll_student("Bobby", 712)    
enroll_student("Jameson", 711)    
enroll_student("Johnath", 712)    
enroll_student("Claudine", 709)    
enroll_student("Jackson", 715)    
enroll_student("Pauline", 711)    
enroll_student("Peterburg", 711)    
enroll_student("Smith Wills", 720)    
enroll_student("Willy", 712) 
enroll_student("Hallan", 713)    
enroll_student("claudien", 714)    
enroll_student("Jacky", 715)    
enroll_student("Hanna", 716)    
enroll_student("Clack", 717)    
enroll_student("Doe", 718)    
enroll_student("Olive", 719) 


main()






# print()
# print()