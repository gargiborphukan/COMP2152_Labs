#Question 4: Class Attendance (Sets - Uniqueness and Operations)
monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}
print(monday_class)
print(wednesday_class)
monday_class.add("Grace")
print(f"Monday class : {monday_class}")
print(f"Wednesday class : {wednesday_class}")
print(f"Both class : {monday_class & wednesday_class}") # Shift + 7
print(f"Attended either class : {monday_class | wednesday_class}")# | = pipe,shift + \
print(f"Only Monday class : {monday_class - wednesday_class}")
print(f"Only one class : {monday_class ^ wednesday_class}")  # ^ = caret 
all_students = monday_class | wednesday_class
print(f"Is Monday subset of all students : ",monday_class <= all_students) 