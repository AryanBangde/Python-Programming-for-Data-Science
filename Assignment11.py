
import pandas as pd
import time

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Start execution timer
start_time = time.perf_counter()

# 1. Create dataset
data = {
    'Age_group': ['Young', 'Middle', 'Senior', 'Young',
                  'Middle', 'Senior', 'Young', 'Middle'],
    'Income': ['High', 'Low', 'Medium', 'Medium',
               'High', 'Low', 'Low', 'High'],
    'Student': ['No', 'No', 'No', 'Yes',
                'Yes', 'Yes', 'No', 'Yes'],
    'Purchased': ['No', 'No', 'Yes', 'Yes',
                  'Yes', 'No', 'No', 'Yes']
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

# 2. Separate input and output
X = df.drop(columns=['Purchased'])
Y = df['Purchased']

# 3. Split data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y,
    test_size=0.25,
    random_state=42,
    stratify=Y
)

# 4. Select categorical features
categorical_features = ['Age_group', 'Income', 'Student']

# 5. Apply One-Hot Encoding
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'),
         categorical_features)
    ]
)

# 6. Create the machine learning pipeline
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression())
])

# 7. Train the model
model_pipeline.fit(X_train, Y_train)

# 8. Predict test data
Y_pred = model_pipeline.predict(X_test)

# 9. Evaluate model
print("\nActual Values:", list(Y_test))
print("Predicted Values:", list(Y_pred))

print("\nAccuracy:", accuracy_score(Y_test, Y_pred))

print("\nClassification Report:\n")
print(classification_report(
    Y_test, Y_pred, zero_division=0
))

# 10. Calculate execution time
end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"\nExecution Time: {execution_time:.6f} seconds")
print(f"Execution Time: {execution_time * 1000:.3f} milliseconds")
