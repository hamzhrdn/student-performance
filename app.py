import streamlit as st
import joblib
import numpy as np
import pandas as pd
import os

# Config
st.set_page_config(
    page_title="Student Dropout Prediction",
    page_icon="🎓",
    layout="centered"
)

# Model
@st.cache_data
def load_model_and_scaler():
    """Loads the pre-trained model and scaler from the 'model' directory."""
    model_path = os.path.join('model', 'student_dropout_model.joblib')
    scaler_path = os.path.join('model', 'scaler.joblib')
    
    if not os.path.exists(model_path) or not os.path.exists(scaler_path):
        st.error("Model or scaler file not found. Please make sure 'student_dropout_model.joblib' and 'scaler.joblib' are in the 'model' subfolder.")
        return None, None
        
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    return model, scaler

model, scaler = load_model_and_scaler()
#Mapping Category
marital_status_map = {"Single": 1, "Married": 2, "Widowed": 3, "Divorced": 4, "Facto Union": 5, "Legally Separated": 6}

course_map = {
    "Biofuel Production Technologies": 33, "Animation and Multimedia Design": 171, "Social Service (evening attendance)": 8014,
    "Agronomy": 9003, "Communication Design": 9070, "Veterinary Nursing": 9085, "Informatics Engineering": 9119,
    "Equinculture": 9130, "Management": 9147, "Social Service": 9238, "Tourism": 9254, "Nursing": 9500,
    "Oral Hygiene": 9556, "Advertising and Marketing Management": 9670, "Journalism and Communication": 9773,
    "Basic Education": 9853, "Management (evening attendance)": 9991
}

application_mode_map = {
    "1st phase - general contingent": 1, "Ordinance No. 612/93": 2, "1st phase - special contingent (Azores Island)": 5,
    "Holders of other higher courses": 7, "Ordinance No. 854-B/99": 10, "International student (bachelor)": 15,
    "1st phase - special contingent (Madeira Island)": 16, "2nd phase - general contingent": 17, "3rd phase - general contingent": 18,
    "Ordinance No. 533-A/99, item b2) (Different Plan)": 26, "Ordinance No. 533-A/99, item b3 (Other Institution)": 27,
    "Over 23 years old": 39, "Transfer": 42, "Change of course": 43, "Technological specialization diploma holders": 44,
    "Change of institution/course": 51, "Short cycle diploma holders": 53, "Change of institution/course (International)": 57
}

prev_qualification_map = {
    "Secondary education": 1, "Higher education - bachelor's degree": 2, "Higher education - degree": 3,
    "Higher education - master's": 4, "Higher education - doctorate": 5, "Frequency of higher education": 6,
    "12th year of schooling - not completed": 9, "11th year of schooling - not completed": 10,
    "Other - 11th year of schooling": 12, "10th year of schooling": 14, "10th year of schooling - not completed": 15,
    "Basic education 3rd cycle (9th/10th/11th year) or equiv.": 19, "Basic education 2nd cycle (6th/7th/8th year) or equiv.": 38,
    "Technological specialization course": 39, "Higher education - degree (1st cycle)": 40,
    "Professional higher technical course": 42, "Higher education - master (2nd cycle)": 43
}

occupation_map = {
    "Student": 0, "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers": 1,
    "Specialists in Intellectual and Scientific Activities": 2, "Intermediate Level Technicians and Professions": 3,
    "Administrative staff": 4, "Personal Services, Security and Safety Workers and Sellers": 5,
    "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry": 6, "Skilled Workers in Industry, Construction and Craftsmen": 7,
    "Installation and Machine Operators and Assembly Workers": 8, "Unskilled Workers": 9, "Armed Forces Professions": 10,
    "Other Situation": 90, "(blank)": 99, "Health professionals": 122, "teachers": 123,
    "Specialists in information and communication technologies (ICT)": 125, "Intermediate level science and engineering technicians and professions": 131,
    "Technicians and professionals, of intermediate level of health": 132, "Intermediate level technicians from legal, social, sports, cultural and similar services": 134,
    "Office workers, secretaries in general and data processing operators": 141, "Data, accounting, statistical, financial services and registry-related operators": 143,
    "Other administrative support staff": 144, "personal service workers": 151, "sellers": 152, "Personal care workers and the like": 153,
    "Skilled construction workers and the like, except electricians": 171, "Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like": 173,
    "Workers in food processing, woodworking, clothing and other industries and crafts": 175, "cleaning workers": 191,
    "Unskilled workers in agriculture, animal production, fisheries and forestry": 192,
    "Unskilled workers in extractive industry, construction, manufacturing and transport": 193, "Meal preparation assistants": 194
}

default_values = {
    'Marital_status': 1.0, 'Application_mode': 17.0, 'Application_order': 1.0, 'Course': 9238.0,
    'Daytime_evening_attendance': 1.0, 'Previous_qualification': 1.0, 'Previous_qualification_grade': 133.1,
    'Nacionality': 1.0, 'Mothers_qualification': 19.0, 'Fathers_qualification': 19.0,
    'Mothers_occupation': 5.0, 'Fathers_occupation': 7.0, 'Admission_grade': 126.1, 'Displaced': 1.0,
    'Educational_special_needs': 0.0, 'Debtor': 0.0, 'Tuition_fees_up_to_date': 1.0, 'Gender': 0.0,
    'Scholarship_holder': 0.0, 'Age_at_enrollment': 20.0, 'International': 0.0,
    'Curricular_units_1st_sem_credited': 0.0, 'Curricular_units_1st_sem_enrolled': 6.0,
    'Curricular_units_1st_sem_evaluations': 8.0, 'Curricular_units_1st_sem_approved': 5.0,
    'Curricular_units_1st_sem_grade': 12.28, 'Curricular_units_1st_sem_without_evaluations': 0.0,
    'Curricular_units_2nd_sem_credited': 0.0, 'Curricular_units_2nd_sem_enrolled': 6.0,
    'Curricular_units_2nd_sem_evaluations': 8.0, 'Curricular_units_2nd_sem_approved': 5.0,
    'Curricular_units_2nd_sem_grade': 12.2, 'Curricular_units_2nd_sem_without_evaluations': 0.0,
    'Unemployment_rate': 11.1, 'Inflation_rate': 1.4, 'GDP': 0.32
}

# --- UI ---
if model and scaler:
    st.title("🎓 Student Dropout Prediction")
    st.markdown("Enter the student's information below to predict the likelihood of dropout.")

    # Student Profile
    st.header("Student Profile")
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age at Enrollment", min_value=17, max_value=70, value=20)
        marital_status_str = st.selectbox("Marital Status", list(marital_status_map.keys()), index=0)
        father_occupation_str = st.selectbox("Father's Occupation", list(occupation_map.keys()), index=list(occupation_map.keys()).index("Skilled Workers in Industry, Construction and Craftsmen"))

    with col2:
        scholarship_holder = st.selectbox("Scholarship Holder?", ("No", "Yes"), index=0)
        international = st.selectbox("International Student?", ("No", "Yes"), index=0)
        mother_occupation_str = st.selectbox("Mother's Occupation", list(occupation_map.keys()), index=list(occupation_map.keys()).index("Personal Services, Security and Safety Workers and Sellers"))

    # Academic Background
    st.header("Academic Background")
    col3, col4 = st.columns(2)
    with col3:
        course_str = st.selectbox("Course", list(course_map.keys()), index=list(course_map.keys()).index("Social Service"))
        prev_qualification_str = st.selectbox("Previous Qualification", list(prev_qualification_map.keys()), index=0)

    with col4:
        application_mode_str = st.selectbox("Application Mode", list(application_mode_map.keys()), index=list(application_mode_map.keys()).index("2nd phase - general contingent"))
        prev_qual_grade = st.number_input("Previous Qualification Grade", min_value=0.0, max_value=200.0, value=133.1)


    # Enrollment Status Section
    st.header("Current Enrollment Status")
    col5, col6 = st.columns(2)
    with col5:
        debtor = st.selectbox("Is the student a debtor?", ("No", "Yes"), index=0)
        tuition_up_to_date = st.selectbox("Tuition Fees Up to Date?", ("No", "Yes"), index=1)
        sem1_grade = st.number_input("1st Sem Grade (0-20)", min_value=0.0, max_value=20.0, value=12.28, format="%.2f")
        sem2_grade = st.number_input("2nd Sem Grade (0-20)", min_value=0.0, max_value=20.0, value=12.20, format="%.2f")

    with col6:
        sem1_enrolled = st.number_input("1st Sem Enrolled Units", min_value=0, max_value=26, value=6)
        sem2_enrolled = st.number_input("2nd Sem Enrolled Units", min_value=0, max_value=23, value=6)
        sem1_approved = st.number_input("1st Sem Approved Units", min_value=0, max_value=26, value=5)
        sem2_approved = st.number_input("2nd Sem Approved Units", min_value=0, max_value=23, value=5)
        

    # Prediction
    if st.button("Predict Dropout Possibility", type="primary"):
        features = default_values.copy()
        
        features['Age_at_enrollment'] = age
        features['Marital_status'] = marital_status_map[marital_status_str]
        features['Mothers_occupation'] = occupation_map[mother_occupation_str]
        features['Fathers_occupation'] = occupation_map[father_occupation_str]
        features['Scholarship_holder'] = 1 if scholarship_holder == "Yes" else 0
        features['International'] = 1 if international == "Yes" else 0
        
        features['Course'] = course_map[course_str]
        features['Application_mode'] = application_mode_map[application_mode_str]
        features['Previous_qualification'] = prev_qualification_map[prev_qualification_str]
        features['Previous_qualification_grade'] = prev_qual_grade
        
        features['Debtor'] = 1 if debtor == "Yes" else 0
        features['Tuition_fees_up_to_date'] = 1 if tuition_up_to_date == "Yes" else 0
        features['Curricular_units_1st_sem_enrolled'] = sem1_enrolled
        features['Curricular_units_2nd_sem_enrolled'] = sem2_enrolled
        features['Curricular_units_1st_sem_approved'] = sem1_approved
        features['Curricular_units_2nd_sem_approved'] = sem2_approved
        features['Curricular_units_1st_sem_grade'] = sem1_grade
        features['Curricular_units_2nd_sem_grade'] = sem2_grade

        feature_array = np.array([features[key] for key in default_values.keys()]).reshape(1, -1)

        scaled_features = scaler.transform(feature_array)
        prediction = model.predict(scaled_features)
        probability = model.predict_proba(scaled_features)
        
        st.subheader("Prediction Result")
        if prediction[0] == 1:
            st.error(f"High Possibility of Dropout ({probability[0][1]*100:.2f}%)")
        else:
            st.success(f"Low Possibility of Dropout ({probability[0][0]*100:.2f}%)")

        st.write("---")
        st.write(f"**Confidence Score:**")
        st.write(f"Probability of Graduating/Enrolling: **{probability[0][0]*100:.2f}%**")
        st.write(f"Probability of Dropping Out: **{probability[0][1]*100:.2f}%**")

else:
    st.error("Could not load the model. Please check the file paths and ensure the model files exist.")
    