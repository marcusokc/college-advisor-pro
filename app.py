import streamlit as st

# App Title
st.title("College and Career Advisor")

# Introduction
st.write("""
Welcome to the College and Career Advisor! Fill out the form below to get personalized recommendations for schools, scholarships, and financial aid options.
""")

# Form
with st.form("user_form"):
    st.header("Tell Us About Yourself")
    name = st.text_input("Full Name", placeholder="Enter your name")
    email = st.text_input("Email Address", placeholder="Enter your email")
    gpa = st.text_input("GPA (on a 4.0 scale)", placeholder="E.g., 3.5")
    test_scores = st.text_input("SAT/ACT Score", placeholder="E.g., 1200 SAT or 25 ACT")
    household_income = st.selectbox(
        "Household Income Range",
        ["Select...", "Less than $30,000", "$30,000 - $60,000", "$60,000 - $100,000", "Over $100,000"]
    )
    education_level = st.selectbox(
        "Current Education Level",
        ["Select...", "High School", "Undergraduate", "Graduate", "Other"]
    )
    preferred_region = st.text_input("Preferred Location", placeholder="E.g., California, Midwest, etc.")
    interests = st.text_area("Academic or Career Interests", placeholder="E.g., engineering, healthcare, arts")
    extracurriculars = st.text_area("Extracurricular Activities", placeholder="E.g., sports, music, clubs")

    submitted = st.form_submit_button("Submit")

# Recommendations Section
if submitted:
    if all([name, email, gpa, test_scores, household_income, education_level, preferred_region, interests]):
        st.success(f"Thank you, {name}! Here are your personalized recommendations:")

        # Example Recommendations
        st.subheader("School Recommendations")
        if float(gpa) >= 3.5:
            st.write("🎓 **Reach Schools**: Stanford, MIT, Harvard")
            st.write("🎓 **Safety Schools**: University of [Your State], Local Community Colleges")
        else:
            st.write("🎓 **Start at a Community College**: Transfer to a 4-year program later.")

        st.subheader("Scholarships")
        st.write("💰 **Pell Grants**: Based on income.")
        st.write("💰 **Local Scholarships**: Contact your high school counselor.")

        st.subheader("Financial Aid Tips")
        st.write("✅ Complete the FAFSA early!")
        st.write("✅ Look into work-study programs.")

        st.info("For detailed recommendations, unlock premium features!")
    else:
        st.error("Please complete all fields to get your recommendations.")

file_path = "submissions.csv"

if submitted and name and email and interests and education_level != "Select...":
    # Check if the file exists
    if os.path.exists(file_path):
        existing_data = pd.read_csv(file_path)
    else:
        existing_data = pd.DataFrame(columns=["Name", "Email", "Interests", "Education Level"])

    # Append new submission
    new_data = pd.DataFrame([{
        "Name": name,
        "Email": email,
        "Interests": interests,
        "Education Level": education_level
    }])
    updated_data = pd.concat([existing_data, new_data], ignore_index=True)

    # Save back to CSV
    updated_data.to_csv(file_path, index=False)
    st.success("Your information has been saved!")
