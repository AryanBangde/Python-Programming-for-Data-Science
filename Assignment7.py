import matplotlib.pyplot as plt

# 1. Simple Datasets

# Line Plot: Study Hours
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
hours_studied = [1, 4, 3, 5, 6]

# Bar Chart: No of books read by 4 students
students = ["Alice", "Bob", "Charlie", "David"]
books_read = [4, 7, 2, 5]

# Histogram: Test scores of 10 students
test_scores = [ 51, 60, 63, 70, 72, 75, 78, 85, 88, 91, 95, 97]

# 2. Create a figure with 3 subplots side-by-side
fig, axes = plt.subplots(figsize=(12, 4), nrows=1, ncols=3)

fig.suptitle(
    "Student Data Visualizations",
    fontsize=14,
    fontweight="bold"
)

# 3. Line Plot: Study Progress
axes[0].plot(
    days,
    hours_studied,
    marker="o",
    color="blue",
    linewidth=2
)

axes[0].set_title("Line Plot: Study Hours")
axes[0].set_xlabel("Day of Week")
axes[0].set_ylabel("Hours Studied")
axes[0].grid(True)

# 4. Bar Chart: Books Read
axes[1].bar(
    students,
    books_read,
    color=["pink", "skyblue", "lightgreen", "orange"]
)

axes[1].set_title("Bar Chart: Books Read")
axes[1].set_xlabel("Students")
axes[1].set_ylabel("Number of Books")
axes[1].grid(True)

# 5. Histogram: Test Score Ranges
axes[2].hist(
    test_scores,
    bins=[50, 60, 70, 80, 90, 100],
    color="red",
    edgecolor="black"
)

axes[2].set_title("Histogram: Score Distribution")
axes[2].set_xlabel("Score Ranges")
axes[2].set_ylabel("Number of Students")
axes[2].grid(True)

# 6. Display the plots
plt.tight_layout()
plt.show()
