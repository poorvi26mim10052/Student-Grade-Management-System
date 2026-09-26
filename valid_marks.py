def is_valid_marks(marks_str):
   
    parts = marks_str.split('.')
   
    if len(parts) > 2:
        return False
    return all (part.isdigit() for part in parts if part)
