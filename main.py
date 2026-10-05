import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

# Load dataset
data = pd.read_csv("career_data.csv")

# Convert text values into numbers
encoder = LabelEncoder()

columns = [
    "Math",
    "Programming",
    "Communication",
    "Creativity",
    "Problem_Solving",
    "Interest",
    "Career"
]

for column in columns:
    data[column] = encoder.fit_transform(data[column])

# Separate input and output
X = data.drop("Career", axis=1)
y = data["Career"]

# Create and train ML model
model = DecisionTreeClassifier()
model.fit(X, y)
# Take student input
print("\nEnter your details:")

math = input("Math level (Low/Medium/High): ")
programming = input("Programming level (Low/Medium/High): ")
communication = input("Communication level (Low/Medium/High): ")
creativity = input("Creativity level (Low/Medium/High): ")
problem_solving = input("Problem Solving level (Low/Medium/High): ")
interest = input("Interest (Technology/Business/Creative/Finance): ")

# Convert input into numbers
input_data = pd.DataFrame([[
    math,
    programming,
    communication,
    creativity,
    problem_solving,
    interest
]], columns=X.columns)

for column in input_data.columns:
    input_data[column] = encoder.fit_transform(
        pd.concat([data[column].astype(str), input_data[column].astype(str)])
    )[-1:]

# Predict career
prediction = model.predict(input_data)

print("\nRecommended Career:", prediction[0])

print("ML model trained successfully!")