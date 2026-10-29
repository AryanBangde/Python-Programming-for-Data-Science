import pandas as pd
df =pd.read_csv("C:/Users/CC/Downloads/employee_data_2.csv")
print(df)

print("="*60)
print("5. missimg values check")
print("=" *60)
missing_data = df.isnull().sum()
print(missing_data[missing_data>0]if missing_data.sum()>0 else "No missing values found.")
print("\n")
print("="*60)
print("6. DUPICATE ROWS CHECK")
print("="*60)
print(f"Number of duplicate numbers")
print("="*60)
print("7.NUMERICAL SUMMARY STATISTICS")
print("="*60)
print(df.describe(include=['object','category']),"\n")
print("=" * 60)
print("8. CATEGORICAL SUMMARY STATISTICS")
print("=" * 60)
print(df.describe(include=['object', 'category']), "\n")
print("=" * 60)
print("9. VALUE COUNTS FOR CATEGORICAL COLUMNS")
print("=" * 60)
categorical_cols = df.select_dtypes(include=['object', 'category']).columns
for col in categorical_cols:
    print(f"--- {col} ---")
    print(df[col].value_counts(), "\n")
print("=" * 60)
print("10. ADDITIONAL NUMERIC METRICS")
print("=" * 60)
numeric_cols = df.select_dtypes(include=['number']).columns
metrics_df = pd.DataFrame({
'Mean': df[numeric_cols].mean(),
'Median': df[numeric_cols].median(),
'Variance': df[numeric_cols].var(),
'Skewness': df[numeric_cols].skew()
})
print(metrics_df)
