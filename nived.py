import streamlit as st

# Custom CSS to remove button borders and change text color to black
st.markdown("""
    <style>
    .stButton button {
        background-color: transparent;
        color: black;  /* Set text color to black */
        border: none;
        font-size: 1.2rem;
        text-align: left;
        padding: 0.5rem;
        transition: color 0.3s ease, background-color 0.3s ease;
        display: block;
        width: 100%;
    }
    .stButton button:hover {
        background-color: #4b4b4b;
        color: white;  /* Change text color to white on hover */
        cursor: pointer;
    }
    .stButton button:focus {
        outline: none;
    }
    .sidebar .sidebar-content h2 {
        color: #ff4b4b;
        padding-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
def nav_menu():
    st.sidebar.markdown("<h2>PROFILE</h2>", unsafe_allow_html=True)
    about_clicked = st.sidebar.button("About")
    education_clicked = st.sidebar.button("Education")
    skills_clicked = st.sidebar.button("Experience and Additional Skills")
    contact_clicked = st.sidebar.button("Contact Me")
    
    st.sidebar.markdown("<h2>PROJECTS</h2>", unsafe_allow_html=True)
    youtube_clicked = st.sidebar.button("YouTube Sentiment Analysis")
    anonymization_clicked = st.sidebar.button("Text Data Anonymization")
    movie_prediction_clicked = st.sidebar.button("Movie Revenue Prediction")
    fraud_detection_clicked = st.sidebar.button("Credit Card Fraud Detection")
    spotify_prediction_clicked = st.sidebar.button("Spotify Song Genre Prediction")
    crypto_prediction_clicked = st.sidebar.button("Crypto Prediction")
    movie_recommendation_clicked = st.sidebar.button("Movie Recommendation System")
    glasgow_city_clicked = st.sidebar.button("Real-Time View of Glasgow City Centre")
    alcohol_analysis_clicked = st.sidebar.button("An Analysis of Alcohol-Related Callouts' Burden on Ambulance Waiting Times")
    syncorg_optimization_clicked = st.sidebar.button("Data Management & Workflow Optimization for SyncOrg")

    # Return the selected page
    if about_clicked:
        return "About"
    elif education_clicked:
        return "Education"
    elif skills_clicked:
        return "Skills"
    elif contact_clicked:
        return "Contact"
    elif youtube_clicked:
        return "YouTube"
    elif anonymization_clicked:
        return "Anonymization"
    elif movie_prediction_clicked:
        return "Movie"
    elif fraud_detection_clicked:
        return "Fraud"
    elif spotify_prediction_clicked:
        return "Spotify"
    elif crypto_prediction_clicked:
        return "Crypto"
    elif movie_recommendation_clicked:
        return "Movie Rec"
    elif glasgow_city_clicked:
        return "Glasgow"
    elif alcohol_analysis_clicked:
        return "Alcohol"
    elif syncorg_optimization_clicked:
        return "SyncOrg"
    else:
        return "About"  # Default page

# Display content based on the selected page
selected_page = nav_menu()

if selected_page == "About":
    st.title("Hey there! I’m Nived.")
    st.write("""
Iam a passionate **Data Scientist** who thrives on turning raw data into meaningful insights. For me, data isn’t just numbers on a screen—it’s a tool to shape decisions, drive innovation, and solve real-world problems. Whether I’m building **predictive models**, tackling **machine learning challenges**, or exploring **NLP**, I’m always looking for new ways to push the boundaries of what data can do.

My work spans across multiple domains. I’ve developed solutions for **healthcare data anonymization** to ensure privacy compliance, built **credit card fraud detection models**, and even created a **Real-Time YouTube Comment Sentiment Analysis web app** that provides instant insights into audience sentiment. Lately, I’ve been diving into **cloud deployment** with **AWS**, scaling projects to make them more efficient and accessible.

While I thrive in environments where **creativity meets logic**, life isn’t all about data! When I’m not immersed in my projects, you’ll find me out for a run, hitting the gym, or cooking up something new in the kitchen. I’m also a huge fan of **movies** and **video games**, which help me recharge after solving complex data problems.

In short, I’m always curious, always learning, and always ready for the next exciting challenge. Whether it’s predicting trends or breaking down complex problems, I’m eager to dive in and get to work.

Feel free to use the navigation on the left to check out my latest projects and learn more about me!

Nived Raj
""")


elif selected_page == "Education":
    st.title("Education")
    st.markdown("""

    - **Master’s in Data Analytics (Distinction)**  
      *University of Strathclyde* | September 2021 – September 2022  

    - **Bachelor of Technology in Computer Science and Engineering (First Class)**  
      *Kerala Technological University* | 2016 – 2020  
    *CGPA: 8.83*

    - **Higher Secondary Education in Computer Science (94%)**  
      *KTCT Higher Secondary School* | 2014 – 2016  

    - **10th Grade, Central Board of Secondary Education (CGPA: 10)**  
      *Sree Gokulam School* | 2013 – 2014  
    """)


elif selected_page == "Skills":
    st.title("Experience and Additional Skills")
    st.write("NLP, Machine Learning, Cloud Deployment.")

elif selected_page == "Contact":
    st.title("Contact Me")
    st.write("[LinkedIn](https://www.linkedin.com/in/nivedraj)")

elif selected_page == "YouTube":
    st.title("YouTube Comment Sentiment Analysis")
    st.write("Analyzing YouTube comments to determine the overall sentiment.")

elif selected_page == "Anonymization":
    st.title("Text Data Anonymization for Health Records")
    st.write("Ensuring compliance with GDPR by anonymizing sensitive health data.")
    st.markdown("""
    <iframe src="https://1drv.ms/p/c/b1cefbb29bc4dda5/IQQ7jcn1gTJOTrP2Ig5UYBypARWDeSgpVqDo8jWyVG06240?em=2&amp;wdAr=1.7777777777777777" 
    width="714px" height="432px" frameborder="0">This is an embedded <a target="_blank" href="https://office.com">Microsoft Office</a> presentation, powered by <a target="_blank" href="https://office.com/webapps">Office</a>.
    </iframe>
    """, unsafe_allow_html=True)

elif selected_page == "Movie":
    st.title("Movie Revenue Prediction")
    st.write("Predicting movie revenue based on various features.")

elif selected_page == "Fraud":
    st.title("Credit Card Fraud Detection")
    st.write("A machine learning model designed to detect fraudulent credit card transactions.")

elif selected_page == "Spotify":
    st.title("Spotify Song Genre Prediction")
    st.write("Predicting the genre of Spotify songs using machine learning models.")

elif selected_page == "Crypto":
    st.title("Crypto Prediction")
    st.write("Predicting cryptocurrency market trends using LSTM and sentiment analysis.")

elif selected_page == "Movie Rec":
    st.title("Movie Recommendation System")
    st.write("A recommender system to suggest movies based on user preferences.")

elif selected_page == "Glasgow":
    st.title("Real-Time View of Glasgow City Centre")
    st.write("A real-time dashboard for monitoring activity in Glasgow city center.")

elif selected_page == "Alcohol":
    st.title("An Analysis of Alcohol-Related Callouts' Burden on Ambulance Waiting Times")
    st.write("An analysis of the impact of alcohol-related incidents on ambulance response times.")

elif selected_page == "SyncOrg":
    st.title("Data Management & Workflow Optimization for SyncOrg")
    st.write("Optimizing data management and workflows for SyncOrg.")
