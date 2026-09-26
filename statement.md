Student-Grade-Management-System – Project Statement
1. Problem Statement

Managing student academic records manually can be time-consuming and may lead to errors when calculating marks, percentages, and grades.

The Student-Grade-Management-System is developed to provide a simple and efficient way to manage student academic information through a console-based Python application.

The system allows users to enter student details such as roll number and name, record marks for Math, Science, and English, automatically calculate the student's percentage, and assign a grade based on the calculated percentage.

The application also provides functionality to view all stored student records and delete records using the student's roll number.

The main goal of the project is to reduce manual calculation and provide a structured way to manage basic student academic records.

2. Scope of the Project

The scope of this project is to provide basic student academic record management using a Python console application.

The project includes:

Adding new student records.

Storing the student's roll number and name.

Recording marks for Math, Science, and English.

Validating marks to ensure they are between 0 and 100.

Preventing duplicate roll numbers.

Calculating the student's total marks and percentage.

Automatically assigning a grade based on the percentage.

Viewing all available student records.

Deleting a student using their roll number.

Handling invalid menu choices and incorrect user input.

Current limitations:

Student data is stored temporarily in memory.

Data is lost when the application is closed.

The system currently supports only three subjects.

The project does not use a database or permanent file storage.

The application is console-based and does not provide a graphical user interface.

Existing student records cannot currently be edited.

The project can be extended in the future by adding database storage, search functionality, record editing, additional subjects, and a graphical user interface.

3. Target Users

The Student-Grade-Management-System is designed primarily for users who need a simple system for managing basic student academic records.

Primary Target Users

Teachers – to record and review students' marks and grades.

School or College Staff – to maintain basic student academic information.

Students – to understand and view their academic performance when records are entered into the system.

Beginners learning Python – to understand how a simple management system can be developed using Python.

Educational Use

The project can also be used as a learning project for students studying programming and software development. It demonstrates practical applications of:

Functions

Dictionaries

Lists

Loops

Conditional statements

Input validation

Data processing

Basic mathematical calculations

4. High-Level Features
4.1 Add Student

The system allows users to create a new student record by entering:

Roll number

Student name

Math marks

Science marks

English marks

The system prevents the addition of a student if the roll number already exists.

4.2 Marks Validation

The system checks that entered marks are valid and fall within the range:

0 to 100


Invalid marks are rejected and the user is asked to enter the marks again.

4.3 Automatic Percentage Calculation

The application automatically calculates the student's percentage from the marks entered for all three subjects.

For example:

Math    = 80
Science = 90
English = 70


The total marks are:

240 / 300


The percentage is:

80%

4.4 Automatic Grade Calculation

The system assigns a grade based on the calculated percentage:

Percentage	Grade
90–100	S
80–89.99	A
70–79.99	B
60–69.99	C
50–59.99	D
Below 50	F
4.5 View All Students

Users can view all stored student records.

Each record displays:

Roll number

Student name

Marks for each subject

Percentage

Grade

4.6 Delete Student

Users can delete a student record by entering the student's roll number.

If the roll number is found, the corresponding student record is removed.

If the roll number does not exist, an error message is displayed.

4.7 Duplicate Record Prevention

The system checks whether a roll number already exists before adding a new student.

This prevents duplicate student records from being created.

4.8 Menu-Based Interface

The application provides a simple menu with four options:

=== Student Management Menu ===
1. Add Student
2. View All Students
3. Delete Student
4. Exit


The user can repeatedly perform operations until the Exit option is selected.

5. Project Objective
 
   The main objective of the project is to create a simple, user-friendly console application that can manage basic student academic records while demonstrating fundamental Python programming concepts.

   The system aims to make student record management easier by automating percentage and grade calculations and providing simple options for adding, viewing, and deleting student records.

The main objective of the project is to create a simple, user-friendly console application that can manage basic student academic records while demonstrating fundamental Python programming concepts.

The system aims to make student record management easier by automating percentage and grade calculations and providing simple options for adding, viewing, and deleting student records.
