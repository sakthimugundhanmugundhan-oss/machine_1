from sklearn.linear_model import LinearRegression

# House area in square feet
X = [
    [500],
    [700],
    [900],
    [1100],
    [1300],
    [1500],
    [1700],
    [2000]
]

# House price in lakhs
y = [20, 28, 36, 44, 52, 60, 68, 80]

# Create the Machine Learning model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Get house area from user
area = float(input("Enter house area in sq.ft: "))

# Predict house price
prediction = model.predict([[area]])

print("Predicted House Price:", round(prediction[0], 2), "Lakhs")
