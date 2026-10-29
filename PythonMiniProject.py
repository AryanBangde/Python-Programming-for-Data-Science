# USED CAR PRICE PREDICTION MINI PROJECT
# Python Programming for Data Science

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# 1. Create a sample car dataset
np.random.seed(42)
n = 300

data = pd.DataFrame({
    "Year": np.random.randint(2012, 2026, n),
    "Kilometers_Driven": np.random.randint(5000, 180000, n),
    "Fuel_Type": np.random.choice(
        ["Petrol", "Diesel", "CNG"], n
    ),
    "Transmission": np.random.choice(
        ["Manual", "Automatic"], n
    ),
    "Owner": np.random.randint(1, 4, n),
    "Brand": np.random.choice(
        ["Maruti", "Hyundai", "Tata", "Honda", "Toyota"], n
    )
})

# Generate sample prices for demonstration
age = 2026 - data["Year"]

brand_prices = {
    "Maruti": 650000,
    "Hyundai": 800000,
    "Tata": 750000,
    "Honda": 900000,
    "Toyota": 1200000
}

data["Price"] = (
    data["Brand"].map(brand_prices)
    - age * 35000
    - data["Kilometers_Driven"] * 1.5
    - (data["Owner"] - 1) * 40000
    + np.where(data["Fuel_Type"] == "Diesel", 30000, 0)
    + np.where(data["Transmission"] == "Automatic", 50000, 0)
    + np.random.normal(0, 40000, n)
).clip(lower=100000).round(0)

print("\n===== USED CAR PRICE PREDICTION =====")

# 2. Display the dataset
print("\nFirst 5 records:")
print(data.head())

print("\nDataset information:")
print(data.info())

# 3. Data preprocessing
print("\nMissing values:")
print(data.isnull().sum())

data = data.drop_duplicates()
data = data.dropna()

# 4. Data visualization
plt.figure(figsize=(8, 5))
plt.hist(data["Price"], bins=20, edgecolor="black")
plt.title("Used Car Price Distribution")
plt.xlabel("Car Price (INR)")
plt.ylabel("Number of Cars")
plt.tight_layout()
plt.savefig("car_price_distribution.png")
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(data["Year"], data["Price"])
plt.title("Car Year vs Price")
plt.xlabel("Manufacturing Year")
plt.ylabel("Car Price (INR)")
plt.tight_layout()
plt.savefig("year_vs_price.png")
plt.show()

# 5. Prepare data for machine learning
X = data.drop("Price", axis=1)
y = data["Price"]

# Convert text categories into numeric columns
X = pd.get_dummies(X, columns=[
    "Fuel_Type", "Transmission", "Brand"
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

# 6. Train the prediction model
model = RandomForestRegressor(
    n_estimators=100, random_state=42
)
model.fit(X_train, y_train)

# 7. Test model performance
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
score = r2_score(y_test, predictions)

print("\n===== MODEL PERFORMANCE =====")
print(f"Mean Absolute Error: Rs. {mae:,.2f}")
print(f"R2 Score: {score:.3f}")

# 8. Predict price for a car entered by the user
print("\n===== ENTER CAR DETAILS =====")

year = int(input("Manufacturing year (2012-2025): "))
km = float(input("Kilometers driven: "))
fuel = input("Fuel type (Petrol/Diesel/CNG): ").strip().title()
transmission = input(
    "Transmission (Manual/Automatic): "
).strip().title()
owner = int(input("Number of previous owners: "))
brand = input(
    "Brand (Maruti/Hyundai/Tata/Honda/Toyota): "
).strip().title()

if year < 1900 or year > 2026:
    raise ValueError("Please enter a valid manufacturing year.")

if km < 0 or owner < 1:
    raise ValueError("Kilometers must be non-negative and owner count at least 1.")

if fuel not in ["Petrol", "Diesel", "Cng"]:
    raise ValueError("Invalid fuel type.")

if transmission not in ["Manual", "Automatic"]:
    raise ValueError("Invalid transmission.")

if brand not in ["Maruti", "Hyundai", "Tata", "Honda", "Toyota"]:
    raise ValueError("Brand not in the sample dataset.")

car = pd.DataFrame([{
    "Year": year,
    "Kilometers_Driven": km,
    "Fuel_Type": fuel,
    "Transmission": transmission,
    "Owner": owner,
    "Brand": brand
}])

# Apply the same encoding used during training
car = pd.get_dummies(car, columns=[
    "Fuel_Type", "Transmission", "Brand"
])
car = car.reindex(columns=X.columns, fill_value=0)

estimated_price = model.predict(car)[0]

print("\n===== PREDICTED CAR PRICE =====")
print(f"Estimated price: Rs. {estimated_price:,.0f}")
print("\nNote: This is an educational estimate based on sample data.")
print("It is not an actual market valuation.")
print("\nProject completed successfully!")
