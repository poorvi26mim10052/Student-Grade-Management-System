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
