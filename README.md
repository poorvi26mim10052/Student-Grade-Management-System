#Student-Grade-Management-System
1. Project Title

Student-Grade-Management-System

2. Overview of the Project

The Student-Grade-Management-System is a Python-based console application used to manage student academic records.

The application allows the user to add student details such as roll number, student name, and marks in Math, Science, and English. Based on the entered marks, the program automatically calculates the student's percentage and assigns a grade.

The application also provides options to view all student records and delete a student using their roll number.

Student information is stored using a Python dictionary while the program is running. No external database or file storage is used in the current version.

How the System Works

The user selects an option from the main menu.

The user can add a new student.

Marks are entered for Math, Science, and English.

The program validates that marks are between 0 and 100.

The percentage is calculated automatically.

A grade is assigned based on the percentage.

The student record is stored in the students dictionary.

The user can view or delete student records.

The program continues until the user selects Exit.

3. Features
3.1 Add Student

The application allows the user to add a new student by entering:

Roll number

Student name

Math marks

Science marks

English marks

The system does not allow duplicate roll numbers.

3.2 Marks Validation

Marks are checked to ensure that they are within the range:

0 - 100


If the user enters a value outside this range, the program displays an error and asks for the marks again.

3.3 Percentage Calculation

The system automatically calculates the student's percentage using the marks obtained in all three subjects.

For example:

Math    = 80
Science = 90
English = 70


Total marks:

80 + 90 + 70 = 240


Percentage:

240 / 300 × 100 = 80%

3.4 Grade Calculation

The program assigns grades according to the following grading system:

Percentage	Grade
90–100	S
80–89.99	A
70–79.99	B
60–69.99	C
50–59.99	D
Below 50	F
3.5 View All Students

The user can view all stored student records.

The displayed information includes:

Roll number

Student name

Marks for each subject

Percentage

Grade

3.6 Delete Student

The user can delete an existing student by entering their roll number.

If the roll number does not exist, an error message is displayed.

3.7 Input Handling

The program handles several invalid inputs, including:

Empty roll number

Empty student name

Duplicate roll number

Marks below 0

Marks above 100

Invalid menu option

Invalid marks format

3.8 Menu-Based Interface

The program provides a simple console menu:

=== Student Management Menu ===
1. Add Student
2. View All Students
3. Delete Student
4. Exit

4. Technologies / Tools Used
Programming Language

Python 3

Python Concepts Used

The project uses the following Python concepts:

Variables

Lists

Dictionaries

Functions

for loops

while loops

if-elif-else statements

String methods

User input using input()

Dictionary methods such as items() and pop()

Formatted strings (f-strings)

Basic mathematical calculations

Input validation

Libraries

No external Python libraries are required.

The project uses only Python's built-in functionality.

Recommended Development Tools

The program can be written and executed using:

Visual Studio Code

PyCharm

Python IDLE

Any text editor with Python support

Command Prompt / Terminal

5. Installation and Run Instructions
Step 1: Install Python

Make sure Python 3 is installed on your computer.

You can check the installed Python version using:

python --version


If your system uses python3, use:

python3 --version


The command should display the installed Python version.

Step 2: Create the Project Folder

Create a folder for the project, for example:

Student-Grade-Management-Systemm

Step 3: Save the Python File

Save the provided Python code inside the folder with a .py extension.

For example:

project.py


The project structure should look like:

Student-Grade-Management-System
│
├──project.py
└── README.md
└── add_student.py
└── calculate_grade.py
└── calculate_percentage.py
└── del_student.py
└── valid_marks.py
└── statement.md 

Step 4: Open the Terminal

Open Command Prompt or Terminal and navigate to the project folder.

For example:

cd Student-Grade-Management-System

Step 5: Run the Program

Run the following command:

python project.py


If your computer uses python3, run:

python3 project.py

Step 6: Use the Application

After running the program, the main menu will be displayed:

=== Student Management Menu ===
1. Add Student
2. View All Students
3. Delete Student
4. Exit


Enter 1, 2, 3, or 4 according to the operation you want to perform.

6. Instructions for Testing

The following test cases can be used to verify that the program works correctly.

Test Case 1: Add a Student Successfully

Select option:

1


Enter:

Enter Roll Number: 101
Enter Student Name: Rahul Sharma
Enter Marks for Math (0-100): 85
Enter Marks for Science (0-100): 90
Enter Marks for English (0-100): 80


Expected result:

Success: Student Rahul Sharma added successfully!


The calculated percentage should be:

85.00%


The calculated grade should be:

A

Test Case 2: View Student Records

Select:

2


Expected output should contain information similar to:

==============================
       STUDENT RECORDS
==============================
Roll No    : 101
Name       : Rahul Sharma
Marks      : Math: 85.0, Science: 90.0, English: 80.0
Percentage : 85.00%
Grade      : A
------------------------------


This confirms that the student record has been stored correctly.

Test Case 3: Add Student With Duplicate Roll Number

Try adding another student using an existing roll number:

Enter Roll Number: 101


Expected result:

Error: Student with this roll number already exists!


The existing student record should not be overwritten.

Test Case 4: Enter Marks Above 100

While adding a student, enter:

Enter Marks for Math (0-100): 105


Expected result:

Error: Marks must be between 0 and 100.


The program should ask for the Math marks again.

Test Case 5: Enter Negative Marks

Enter:

Enter Marks for Math (0-100): -10


Expected result:

Error: Marks must be between 0 and 100.


The program should ask for the marks again.

Test Case 6: Invalid Marks Input

Enter a non-numeric value:

Enter Marks for Math (0-100): abc


Expected result:

Error: Invalid input. Please enter a valid number.


The program should ask for the marks again.

Test Case 7: Empty Roll Number

Select Add Student and leave the roll number empty:

Enter Roll Number:


Expected result:

Error: Roll number cannot be empty!


The student should not be added.

Test Case 8: Empty Student Name

Enter a valid roll number but leave the name empty:

Enter Roll Number: 102
Enter Student Name:


Expected result:

Error: Student name cannot be empty!


The student should not be added.

Test Case 9: Delete an Existing Student

Select:

3


Then enter:

Enter Roll Number to delete: 101


Expected result:

Success: Removed student Rahul Sharma.


After deleting the student, select option 2 again.

The deleted student should no longer appear in the records.

Test Case 10: Delete a Non-Existing Student

Select:

3


Then enter a roll number that does not exist:

Enter Roll Number to delete: 999


Expected result:

Error: Student roll number not found.

Test Case 11: Invalid Menu Option

Enter an option that is not available:

Select an option (1-4): 7


Expected result:

Invalid choice! Please select an option between 1 and 4.


The main menu should be displayed again.

Test Case 12: Exit the Application

Select:

4


Expected result:

Exiting system. Goodbye!


The program should terminate normally.

7. Testing Checklist
Test	Expected Result	Status
Add valid student	Student added successfully	☐
View students	Student information displayed	☐
Duplicate roll number	Error displayed	☐
Marks greater than 100	Error displayed	☐
Negative marks	Error displayed	☐
Invalid marks	Error displayed	☐
Empty roll number	Error displayed	☐
Empty name	Error displayed	☐
Delete existing student	Student deleted	☐
Delete non-existing student	Error displayed	☐
Invalid menu option	Error displayed	☐
Exit program	Program terminates	☐


8. Conclusion

The Student Management System is a simple Python console application for managing student academic records. It provides functionality for adding, viewing, and deleting students while automatically calculating percentages and grades.

The project demonstrates fundamental Python programming concepts and provides a foundation for developing a more advanced student management application in the future.
