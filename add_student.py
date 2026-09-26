def add_student():
    
    roll_no = input("Enter Roll Number: ").replace(" ", "")
    
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
