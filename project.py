#Project for python essential course  #Student grade management system
import valid_marks
import calculate_grade
import del_student
import add_student
import calculate_percentage
students= {}

SUBJECTS = ['Math', 'Science', 'English']

def is_valid_marks(marks_str):
   
    parts = marks_str.split('.')
   
    if len(parts) > 2:
        return False
    return all (part.isdigit() for part in parts if part)


def calculate_percentage():
    subject_marks = {}
    for subject in SUBJECTS:
        while True:
            marks_input = input(f"Enter Marks for {subject} (0-100): ").strip() 

            if not is_valid_marks(marks_input):
                print("Error: Invalid input. Please enter a valid number.")
                continue
            
            marks = float(marks_input)
            if marks < 0 or marks > 100:
                print("Error: Marks must be between 0 and 100.")
                continue
                
            subject_marks[subject] = marks
            break
    total_marks = sum(subject_marks.values())
    max_possible_marks = len(subject_marks) * 100
    percentage = (total_marks / max_possible_marks) *100

    return percentage, subject_marks

def calculate_grade(percentage):

    if percentage >= 90: 
        return 'S'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70: 
        return 'B'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 50: 
        return 'D'
    else: 
        return 'F'

def add_student():
    
    roll_no = input("Enter Roll Number: ").strip()
    
    if roll_no == "":
        print("Error: Roll number cannot be empty!\n")
        return
        
    if roll_no in students:
        print("Error: Student with this roll number already exists!\n")
        return
    
    name = " ".join(input("Enter Student Name: ").split())
    
    if name == "":
        print("Error: Student name cannot be empty!\n")
        return

    percentage, subject_marks = calculate_percentage()
    grade = calculate_grade(percentage)
    
    students[roll_no] = {
        'name': name, 
        'marks': subject_marks, 
        'percentage': percentage, 
        'grade': grade
    }
    print(f"Success: Student {name} added successfully!\n")

def view_students():
   
    if not students:
        print("No student records found.\n")
        return
        
    print("\n" + "=" * 30)
    print("       STUDENT RECORDS       ")
    print("=" * 30)

    for roll_no, info in students.items():
        
        name = info['name']
        marks = info['marks']
        percentage = info['percentage']
        grade = info['grade']

        formatted_marks = ", ".join(f"{sub}: {score}" for sub, score in marks.items())
        
        print(f"Roll No    : {roll_no}")
        print(f"Name       : {name}")
        print(f"Marks      : {formatted_marks}")
        print(f"Percentage : {percentage:.2f}%")
        print(f"Grade      : {grade}")
        print("-" * 30)
    print()
def delete_student():
  
    roll_no = input("Enter Roll Number to delete: ").strip()
    if roll_no in students:
        removed = students.pop(roll_no)
        print(f"Success: Removed student {removed['name']}.\n")
    else:
        print("Error: Student roll number not found.\n")

def main_menu():
  
    while True:
        print("=== Student Management Menu ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Delete Student")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ").strip()
        print()
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice! Please select an option between 1 and 4.\n")

if __name__ == "__main__":
    main_menu()



  

  
  
                
