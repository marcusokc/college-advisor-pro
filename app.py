import streamlit as st

# App Title
st.title("College Advisor Pro")
st.write("Welcome! Fill out the form below to get personalized recommendations.")

# Form for User Input
with st.form("user_form"):
    name = st.text_input("Full Name", placeholder="Enter your name")
    email = st.text_input("Email Address", placeholder="Enter your email")
    interests = st.text_area("What are your academic or career interests?", placeholder="E.g., engineering, healthcare, arts")
    education_level = st.selectbox(
        "Current Education Level",
        ["Select...", "High School", "Undergraduate", "Graduate", "Other"]
    )
    
    # Submit Button
    submitted = st.form_submit_button("Submit")

# Show Results
if submitted:
    if name and email and interests and education_level != "Select...":
        st.success(f"Thank you, {name}! Here are your recommendations:")
        # Example of generating results
        if "engineering" in interests.lower():
            st.write("🔧 **Recommendation**: Explore programs in mechanical or software engineering.")
        elif "healthcare" in interests.lower():
            st.write("🩺 **Recommendation**: Consider nursing, pre-med, or public health studies.")
        elif "arts" in interests.lower():
            st.write("🎨 **Recommendation**: Look into graphic design, fine arts, or performing arts programs.")
        else:
            st.write("📚 **Recommendation**: Explore general education and career exploration programs.")

        st.write("For more detailed guidance, check out our premium features below!")
    else:
        st.error("Please complete all fields before submitting.")

# Premium Features Section
st.header("Unlock Premium Features")
st.write("Get access to personalized college and career planning tools, exclusive resources, and expert advice.")

if st.button("Upgrade to Premium"):
    st.write("Redirecting you to the payment page...")
    # Link to payment (replace with your payment gateway URL)
    st.markdown("[Click here to pay](https://your-payment-link.com)")
