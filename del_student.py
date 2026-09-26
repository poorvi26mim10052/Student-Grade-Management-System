def delete_student():
  
    roll_no = input("Enter Roll Number to delete: ").replace(" ", "")
    if roll_no in students:
        removed = students.pop(roll_no)
        print(f"Success: Removed student {removed['name']}.\n")
    else:
        print("Error: Student roll number not found.\n")
