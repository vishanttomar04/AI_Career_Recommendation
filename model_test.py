import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("career_data.csv")

feature_columns = [
    "Math",
    "Programming",
    "Communication",
    "Creativity",
    "Problem_Solving",
    "Analytical_Thinking",
    "Leadership",
    "Interest"
]

level_mapping = {
    "Low": 0,
    "Medium": 1,
    "High": 2
}

for column in feature_columns[:7]:
    data[column] = data[column].map(level_mapping)

interest_mapping = {
    "Technology": 0,
    "Business": 1,
    "Creative": 2,
    "Finance": 3
}

data["Interest"] = data["Interest"].map(interest_mapping)

career_encoder = LabelEncoder()
data["Career"] = career_encoder.fit_transform(data["Career"])

X = data[feature_columns]
y = data["Career"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = DecisionTreeClassifier(
    random_state=42,
    max_depth=8,
    min_samples_split=5
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Model trained successfully!")
print("Testing samples:", len(X_test))
print("Model Accuracy:", round(accuracy * 100, 2), "%")