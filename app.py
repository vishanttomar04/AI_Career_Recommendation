import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
st.set_page_config(
    page_title="AI Career Recommendation System",
    page_icon="🎓",
    layout="centered"
)
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

X = data[feature_columns]
y = data["Career"]

model = DecisionTreeClassifier(
    random_state=42,
    max_depth=8,
    min_samples_split=5
)

model.fit(X, y)

st.title("🎓 AI Career Recommendation System")
st.divider()

st.write(
    "Discover the career path that best matches your skills, interests, and strengths using Machine Learning."
)
st.subheader("📊 Your Skills")

math = st.selectbox("Math Level", ["Low", "Medium", "High"])

programming = st.selectbox(
    "Programming Level", ["Low", "Medium", "High"]
)

communication = st.selectbox(
    "Communication Level", ["Low", "Medium", "High"]
)

creativity = st.selectbox(
    "Creativity Level", ["Low", "Medium", "High"]
)

problem_solving = st.selectbox(
    "Problem Solving Level", ["Low", "Medium", "High"]
)

analytical_thinking = st.selectbox(
    "Analytical Thinking Level", ["Low", "Medium", "High"]
)

leadership = st.selectbox(
    "Leadership Level", ["Low", "Medium", "High"]
)
st.subheader("🎯 Your Career Interest")
interest = st.selectbox(
    "Your Interest",
    ["Technology", "Business", "Creative", "Finance"]
)

if st.button("🚀 Recommend My Career", use_container_width=True):
    st.subheader("🤖 AI Recommendation")

    input_data = [[
        level_mapping[math],
        level_mapping[programming],
        level_mapping[communication],
        level_mapping[creativity],
        level_mapping[problem_solving],
        level_mapping[analytical_thinking],
        level_mapping[leadership],
        interest_mapping[interest]
    ]]

    prediction = model.predict(input_data)

    career = prediction[0]

st.success(f"🎯 Recommended Career: {career}")

reasons = []

if programming == "High":
    reasons.append("Strong programming skills")

if math == "High":
    reasons.append("Strong mathematical skills")

if problem_solving == "High":
    reasons.append("Good problem-solving ability")

if analytical_thinking == "High":
    reasons.append("Strong analytical thinking")

if leadership == "High":
    reasons.append("Good leadership skills")

if creativity == "High":
    reasons.append("Good creativity")

if communication == "High":
    reasons.append("Strong communication skills")

if interest == "Technology":
    reasons.append("Strong interest in technology")

if reasons:
    st.info("💡 Why is this career recommended?")
    for reason in reasons:
        st.write("• " + reason)
