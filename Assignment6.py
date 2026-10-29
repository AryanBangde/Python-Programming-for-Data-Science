
import pandas as pd

# Create a sample dataset
data = {
    'Department': ['IT', 'HR', 'IT', 'Sales', 'HR', 'Sales'],
    'Employee': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Riya', 'Karan'],
    'Salary': [40000, 30000, 50000, 35000, 32000, 45000],
    'Age': [25, 28, 30, 26, 29, 32]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Group data by Department
print("\nEmployees grouped by Department:")
print(df.groupby('Department')['Employee'].apply(list))

# Calculate average salary department-wise
print("\nAverage Salary by Department:")
print(df.groupby('Department')['Salary'].mean())

# Calculate total salary department-wise
print("\nTotal Salary by Department:")
print(df.groupby('Department')['Salary'].sum())

# Perform multiple aggregation operations
print("\nDepartment-wise Summary:")
summary = df.groupby('Department').agg({
    'Salary': ['sum', 'mean', 'max'],
    'Age': 'mean',
    'Employee': 'count'
})

print(summary)

