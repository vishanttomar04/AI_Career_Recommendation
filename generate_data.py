import pandas as pd
import random

random.seed(42)

career_profiles = {
    "Software Engineer": [3, 3, 2, 2, 3, 3, 1],
    "Data Scientist": [3, 3, 2, 1, 3, 3, 1],
    "AI Engineer": [3, 3, 1, 2, 3, 3, 1],
    "Web Developer": [2, 3, 2, 3, 2, 2, 1],
    "Cyber Security Analyst": [3, 3, 1, 1, 3, 3, 1],
    "UI UX Designer": [1, 1, 2, 3, 2, 2, 1],
    "Graphic Designer": [1, 1, 2, 3, 1, 1, 1],
    "Marketing Manager": [2, 1, 3, 3, 2, 2, 3],
    "Business Analyst": [3, 2, 3, 1, 3, 3, 3],
    "Financial Analyst": [3, 1, 2, 1, 3, 3, 2]
}

interest_map = {
    "Software Engineer": "Technology",
    "Data Scientist": "Technology",
    "AI Engineer": "Technology",
    "Web Developer": "Technology",
    "Cyber Security Analyst": "Technology",
    "UI UX Designer": "Creative",
    "Graphic Designer": "Creative",
    "Marketing Manager": "Business",
    "Business Analyst": "Business",
    "Financial Analyst": "Finance"
}

levels = {
    1: "Low",
    2: "Medium",
    3: "High"
}

rows = []

for career, profile in career_profiles.items():

    for _ in range(100):

        values = []

        for level in profile:
            variation = random.choice([-1, 0, 0, 0, 1])
            new_level = max(1, min(3, level + variation))
            values.append(levels[new_level])

        rows.append([
            values[0],  # Math
            values[1],  # Programming
            values[2],  # Communication
            values[3],  # Creativity
            values[4],  # Problem Solving
            values[5],  # Analytical Thinking
            values[6],  # Leadership
            interest_map[career],
            career
        ])

columns = [
    "Math",
    "Programming",
    "Communication",
    "Creativity",
    "Problem_Solving",
    "Analytical_Thinking",
    "Leadership",
    "Interest",
    "Career"
]

df = pd.DataFrame(rows, columns=columns)

df.to_csv("career_data.csv", index=False)

print("Improved dataset created successfully!")
print("Total rows:", len(df))
print("Total careers:", df["Career"].nunique())