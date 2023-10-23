import streamlit as st
import webbrowser

# Run the app
if __name__ == "__main__":
    st.set_page_config(page_title="Data Science Portfolio", page_icon="✅")


# Page Title
st.title("My Data Science Portfolio")

# Create a sidebar for navigation
selected_page = st.sidebar.selectbox("Select Page", ["Home", "Projects"])

if selected_page == "Home":
    # Add personal information on the Home page
    st.sidebar.image("pf.jpg", use_column_width=True)

    st.sidebar.title("Personal Information")
    st.sidebar.write("Name &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: <strong>Hammad Farooq</strong>", unsafe_allow_html=True)


    st.sidebar.write("Email &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: hammadfarooq413@gmail.com")
    st.sidebar.write("LinkedIn: [My LinkedIn Profile](https://www.linkedin.com/in/hammadfarooq413/)")
    st.sidebar.write("GitHub &nbsp;&nbsp;&nbsp;: [My GitHub Profile](https://github.com/hammadfarooq413)")
    st.sidebar.write("Contact &nbsp;&nbsp;:&nbsp; +92 308 0018238")


    # Create a section for the Home page
    st.header("About Me")

    # Add a brief introduction about yourself
    st.write("""<p style="text-align: justify;">I am a passionate data scientist with expertise in machine learning, deep learning, data analysis, and data visualization. My goal is to leverage data to solve complex problems and deliver actionable insights.</p>
    """, unsafe_allow_html=True)




   






    # Mention your skills
    st.subheader("Skills")
    st.write(" - Machine Learning")
    st.write(" - Deep Learning")
    st.write(" - Data Analysis")
    st.write(" - Data Visualization")
    st.write(" - Python Programming")
    st.write(" - OOP(Object Oriented Programming)")


           # Mention your educational background
    st.subheader("Education")
    # st.write(" - July 2023 - December 2023")
    st.write("- July 2023 - December 2023 \n- Corvit Systems  [ Artificial Intelligence ]")
    st.write("- 2019-2013 \n- University Of Education  [ Bachelor of Information Technology ]")


elif selected_page == "Projects":
    # Create a section for the Projects page
    st.header("Projects")

    # Project 1
    st.subheader("Project 1: Loan Approval Prediction using ML Model")
    st.write("I created a Loan Approval Prediction Model using machine learning. This model helps determine if someone qualifies for a loan. By analyzing data like credit history, income, and employment status, it predicts whether a loan should be approved or not. This project showcases my skill in using advanced technology to assist financial institutions in making better lending decisions, reducing risk, and simplifying the loan approval process.")
    if st.button("View Project", key="project1_button"):
        webbrowser.open_new_tab("https://github.com/hammadfarooq413/LoanApprovalPredictionUsingML")

    # Project 2
    st.subheader("Project 2: Data Analysis Using Python")
    st.write("I used Python libraries like Pandas and Matplotlib to find important information from dataset.I carefully organized and examined the data, using Pandas to clean and reformat it, getting it ready for a detailed analysis. I used Matplotlib to make attractive charts and graphs that not only showed important patterns and trends but also made the data easy to understand.")
    if st.button("View Project" , key="project2_button"):
        webbrowser.open_new_tab("https://github.com/hammadfarooq413/DataAnalysisUsingPython")

    # Add more projects as needed
