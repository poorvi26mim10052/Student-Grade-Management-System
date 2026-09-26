def calculate_percentage():
    subject_marks = {}
    for subject in SUBJECTS:
        while True:
            marks_input = input(f"Enter Marks for {subject} (0-100): ").replace(" ", "")  

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
