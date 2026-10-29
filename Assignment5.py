import pandas as pd

# Read the CSV file
df = pd.read_csv("C:/Users/CC/Downloads/student_dataset_25.csv")

print("Original Employee Data:")
print(df)

# Sort by salary in ascending order
salary_ascending = df.sort_values(by="Salary", ascending=True)

print("\nEmployees sorted by Salary (Ascending):")
print(salary_ascending)

# Sort by salary in descending order
salary_descending = df.sort_values(by="Salary", ascending=False)

print("\nEmployees sorted by Salary (Descending):")
print(salary_descending)

# Sort by age
age_sorted = df.sort_values(by="Age", ascending=True)

print("\nEmployees sorted by Age:")
print(age_sorted)

# Sort alphabetically by department
department_sorted = df.sort_values(by="Department")

print("\nEmployees sorted by Department:")
print(department_sorted)

# Sort alphabetically by employee name
name_sorted = df.sort_values(by="Employee Full Name")

print("\nEmployees sorted by Employee Name:")
print(name_sorted)
