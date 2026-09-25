students= {}

SUBJECTS = ['Math', 'Science', 'English']

def is_valid_marks(marks_str):
    clean_str = marks_str.replace('.', '', 1)
    if clean_str.isdigit() and marks_str.count('.') <= 1:
        return True
    return False

def calculate_percentage():
    subject_marks = {}
    for subject in SUBJECTS:
        while True:
            marks_input = input(f"Enter Marks for {subject} (0-100): ").replace(" ", "")  

            for subject in SUBJECTS:
                    while True:
                        marks_input = input(f"Enter Marks for {subject} (0-100): ").replace(" ", "")
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
        return 'A+'
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






  

  
  
                
