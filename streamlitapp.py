import streamlit as st
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Page setup
st.set_page_config(
    page_title="Student Performance Predictor",
    layout="centered",
    page_icon="🎓",
)

# Custom CSS styling
st.markdown("""
    <style>
        .main {
            background: linear-gradient(to right, #6a11cb, #2575fc);
            padding: 2rem;
            border-radius: 10px;
            color: white;
        }
        .stButton>button {
            background-color: #ffffff;
            color: #2575fc;
            font-weight: bold;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🎓 Student Performance Predictor")
st.markdown("### Predict the **Math Score** of a student based on input features")

# Form UI
with st.form("prediction_form"):
    gender = st.selectbox("Gender", ["male", "female"])
    ethnicity = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
    parental_level_of_education = st.selectbox("Parental Level of Education", [
        "associate's degree", "bachelor's degree", "high school", "master's degree", "some college", "some high school"
    ])
    lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])
    test_preparation_course = st.selectbox("Test Preparation Course", ["none", "completed"])
    reading_score = st.slider("Reading Score (out of 100)", 0, 100, 70)
    writing_score = st.slider("Writing Score (out of 100)", 0, 100, 70)

    submitted = st.form_submit_button("🔮 Predict Math Score")

if submitted:
    with st.spinner("Running prediction..."):
        data = CustomData(
            gender=gender,
            race_ethnicity=ethnicity,
            parental_level_of_education=parental_level_of_education,
            lunch=lunch,
            test_preparation_course=test_preparation_course,
            reading_score=reading_score,
            writing_score=writing_score
        )
        pred_df = data.get_data_as_data_frame()
        predictor = PredictPipeline()
        result = predictor.predict(pred_df)

    st.success(f"📊 Predicted Math Score: **{round(result[0], 2)}**")
