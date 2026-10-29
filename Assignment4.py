import pandas as pd
df =pd.read_csv("c:/Users/CC/Downloads/employee.csv")
print(df)

data = {
    "Employee ID": [
        101, 102, 103, 104, 105, 106, 101, 102, 107, 108,
        109, 110, 111, 112, 113
    ],

    "Full Name": [
        "Rahul Sharma",
        "Priya Patel",
        "Amit Kumar",
        "Sneha Joshi",
        "Vikas Singh",
        "Neha Deshmukh",
        "Rahul Sharma",      # Duplicate record
        "Priya Patel",      # Duplicate record
        "Rohit Patil",
        None,               # Null value
        "Karan Mehta",
        "Anjali Shah",
        "Amit Kumar",       # Duplicate name
        "Pooja Verma",
        "Sameer Khan"
    ],

    "Age": [
        25, 29, 32, None, 28, 35, 25, 29, None, 31,
        27, 30, 32, 26, None
    ],

    "Employee Salary": [
        45000, 52000, 48000, 55000, None, 60000,
        45000, 52000, 51000, None, 47000, 58000,
        48000, 42000, 65000
    ],

    "Department": [
        "IT", "HR", "Finance", "IT", "Sales", "HR",
        "IT", "HR", None, "Finance", "Sales", "IT",
        "Finance", "Marketing", None
    ],

    "Email": [
        "rahul@gmail.com",
        "priya@gmail.com",
        "amit@gmail.com",
        None,
        "vikas@gmail.com",
        "neha@gmail.com",
        "rahul@gmail.com",       # Duplicate
        "priya@gmail.com",       # Duplicate
        "rohit@gmail.com",
        None,
        "karan@gmail.com",
        "anjali@gmail.com",
        "amit@gmail.com",        # Duplicate
        "pooja@gmail.com",
        "sameer@gmail.com"
    ],

    "City": [
        "Pune", "Mumbai", "Nashik", "Pune", None, "Mumbai",
        "Pune", "Mumbai", "Nashik", None, "Pune", "Mumbai",
        "Nashik", "Pune", None
    ],

    "Joining Date": [
        "2022-01-15",
        "2021-06-20",
        "2020-03-10",
        None,
        "2023-02-18",
        "2019-11-25",
        "2022-01-15",       # Duplicate
        "2021-06-20",       # Duplicate
        "2023-08-12",
        None,
        "2022-09-01",
        "2021-12-15",
        "2020-03-10",       # Duplicate
        "2024-01-20",
        "2023-05-10"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save as CSV
df.to_csv("employee_data.csv", index=False)

print("CSV file created successfully!")
print(df)


# Count null values
print("Null values in Age:")
print(df["Age"].isnull().sum())

print("Null values in Employee Salary:")
print(df["Employee Salary"].isnull().sum())

# Calculate mean and fill null values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Employee Salary"] = df["Employee Salary"].fillna(
    df["Employee Salary"].mean()
)

print("\nData after filling null values:")
print(df[["Age", "Employee Salary"]])

# Split Full Name using space
df[["Name", "Surname"]] = df["Full Name"].str.split(" ", n=1, expand=True)

# Arrange columns in the desired order
df = df[
    ["Employee ID", "Name", "Surname", "Age",
     "Employee Salary", "Department", "Email",
     "City", "Joining Date"]
]

print(df)
