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
    skills_clicked = st.sidebar.button("Experience and Skills")
    contact_clicked = st.sidebar.button("Contact Me")
    
    st.sidebar.markdown("<h2>PROJECTS</h2>", unsafe_allow_html=True)
    youtube_clicked = st.sidebar.button("Real-Time YouTube Sentiment Analytics")
    anonymization_clicked = st.sidebar.button("Text Data Anonymization for Healthcare")
    movie_prediction_clicked = st.sidebar.button("Boxoffice Prediction")
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
    st.write("""
    I’ve always believed that strong foundations lead to greater heights, and my academic journey reflects that. Graduating with **Distinction** in my Master’s in Data Analytics and achieving **First Class** honors in my Computer Science Engineering degree, I’ve consistently pushed the boundaries of learning. From excelling in foundational subjects during my 10th grade (CGPA: 10) to mastering advanced data science concepts at the University of Strathclyde, my academic record speaks to my dedication and proficiency in the field.
    """)

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
    st.title("Experience and Skills")
    st.write("### Skills")
    st.write("From machine learning to cloud deployment, these are the core tools I rely on to deliver impactful data-driven solutions.")
    # Custom CSS for card styling
    st.markdown("""
        <style>
        .skill-card {
            background-color: #f0f0f5;
            border: 1px solid #e1e1eb;
            padding: 20px;
            margin: 10px;
            border-radius: 8px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        .skill-title {
            font-size: 1.2em;
            font-weight: bold;
            margin-bottom: 10px;
            color: #4b4b4b;
        }
        </style>
    """, unsafe_allow_html=True)

    # Function to create a skill card
    def skill_card(title, content):
        st.markdown(f"""
        <div class="skill-card">
            <div class="skill-title">{title}</div>
            <div>{content}</div>
        </div>
        """, unsafe_allow_html=True)

    # Skill categories with content
    skills = {
        "Programming Languages": "Python (NumPy, Pandas, Scikit-learn, Matplotlib, Seaborn), SQL (MySQL), R (Tidyverse), C++, HTML/CSS",
        "Data Science & Machine Learning": "Supervised & Unsupervised Learning, Feature Engineering, Model Deployment, Hyperparameter Tuning, Cross-Validation, Imbalanced Data Techniques (SMOTE, Undersampling), XGBoost, LightGBM, Random Forest, Logistic Regression, KNN, LSTM, Time Series Analysis",
        "Data Analytics & Visualization": "Tableau, Power BI (Dashboard Design, ETL, Data Modeling, Power Query, DAX), Altair, Excel (Advanced Formulas, Pivot Tables, VBA)",
        "Cloud & DevOps": "AWS (EC2, S3), Streamlit, Git, GitHub",
        "Natural Language Processing (NLP)": "spaCy, NLTK, Bigrams, Sentiment Analysis, Named Entity Recognition (NER), Custom Dictionaries, Word Clouds",
        "Databases": "SQL (MySQL), NoSQL (MongoDB basics)",
        "Artificial Intelligence & Deep Learning": "Neural Networks, LSTM, Time Series Forecasting, Sentiment Analysis",
        "Mathematics & Statistics": "Probability, Statistics, Hypothesis Testing, Optimization for Analytics",
        "Soft Skills": "Stakeholder Communication, Cross-functional Collaboration, Team Leadership, Presentations, Mentoring & Training"
    }

    # Display skills as cards in multiple columns
    cols = st.columns(2)
    i = 0
    for title, content in skills.items():
        with cols[i % 2]:
            skill_card(title, content)
        i += 1

    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write("---")
    st.write("### Professional Experience")
    st.write("""

    **Data Science & Machine Learning Intern** | Sep 2020 – Dec 2020  
    **Zesty Beanz Technologies**, Trivandrum, India  
    - Completed a 4-month internship focused on the full data science lifecycle, honing skills in **data preprocessing**, **feature engineering**, and **model evaluation**.  
    - Participated in hands-on machine learning workshops, mastering both **foundational** and **advanced techniques**, which culminated in self-directed projects that demonstrated real-world problem-solving abilities.  
    - Developed a deep understanding of **supervised learning** and **data-driven insights** under the mentorship of experienced industry professionals, laying a strong foundation for future data science work.  

    **Junior Data Analyst (Part-Time)** | Oct 2019 – May 2020  
    **HiTech Spare Parts Centre**, Trivandrum, India  
    - Utilized **Power BI** for end-to-end **ETL processes**, data modeling, and building **interactive dashboards** to track key business metrics such as spare part sales, stock, and inventory levels.  
    - Conducted **inventory trend analysis** using Excel, providing crucial insights to support and optimize daily operations.  
    - Spearheaded training sessions on Excel and Power BI, empowering the team to leverage data for improved decision-making and operational efficiency.  

    **Computer Science Tutor** | Mar 2020 – Jul 2020  
    **Campuzon**, Trivandrum, India  
    - Taught **Python, SQL**, and core computer science concepts to over 100 undergraduate students, delivering hands-on, practical lessons.  
    - Led workshops and personalized support sessions, adapting teaching methods to diverse learning styles and ensuring a deeper understanding of programming fundamentals.  
    - Demonstrated leadership by managing a team of tutors, ensuring consistent teaching quality, and enhancing the department's ability to support student learning outcomes.  
    - Played a pivotal role in creating an engaging and collaborative learning environment, boosting student confidence in mastering programming languages and problem-solving techniques.
    """)



elif selected_page == "Contact":
    st.title("Contact Me")
    st.write("Email: nived2033@gmail.com")
    st.write("Phone: +44 7824819279")
    st.write("[LinkedIn](www.linkedin.com/in/nived-raj-2033da)")
    

elif selected_page == "YouTube":
    # Custom CSS for tag-style words
    # Custom CSS for inline tag-style words
    st.markdown("""
        <style>
        .tag {
            display: inline-block;
            padding: 5px 10px;
            margin: 5px;
            background-color: #f0f0f5;
            border-radius: 6px;
            border: 1px solid #ccc;
            font-size: 14px;
            color: #333;
            font-weight: bold;
        }
        .tag-container {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Project Description
    st.write("""
    # Real-Time YouTube Comment Sentiment Analytics Dashboard

    This interactive dashboard is designed for marketing, advertising, and development teams to gain real-time insights into audience reactions on YouTube. Whether it’s a new movie trailer or a game reveal, this tool delivers actionable data to help teams understand how audiences engage, what excites them, and where the key moments lie.

    ### Tools & Technologies
    """)

    # Display tags inline
    st.markdown("""
    <div class="tag-container">
        <div class="tag">Python</div>
        <div class="tag">Dash</div>
        <div class="tag">AWS (EC2)</div>
        <div class="tag">YouTube API</div>
        <div class="tag">Interactive Dashboard</div>
        <div class="tag">Friendly UI</div>
        <div class="tag">NLP</div>
        <div class="tag">NLTK</div>
        <div class="tag">Topic Extraction</div>
        <div class="tag">Sentiment Analysis</div>
        <div class="tag">Live API Integration</div>
        <div class="tag">Custom Algorithm</div>
        <div class="tag">Emoji Sentiment Extraction</div>
    </div>
    """, unsafe_allow_html=True)

    # Continue with Project Description
    st.write("""
    ### Project Overview
    The dashboard provides an intuitive interface for analyzing YouTube comments on videos, especially **trailers and reviews**. It allows users to search for a video by keyword and retrieve real-time comments. From there, the dashboard breaks down **audience sentiment**, **key discussion points**, and the most **engaging moments** of the video. This makes it especially useful for media and advertising teams who want to understand what resonates most with their target audience.

    ### Key Features

    #### 1. Interactive Time-Bucket Popularity Chart
    A unique feature that analyzes the most discussed 10-second intervals of a video. Each bar in the chart represents a time segment, and by clicking on it, users can dive into the most liked comments during that interval. This reveals what parts of the video generated the most discussion—whether it’s a dramatic reveal or a controversial moment.

    #### 2. Custom Sentiment Analysis
    The backbone of the dashboard is a custom-built sentiment analyzer that avoids spams, off topic comments - and calcualtes sentiment scores per comment. It is then used to caclulate the overall sentiment score - giving weight to comments per likes which gives comments most people agree on, more say in the final sentment score. Using this, the positive to negative proportion is calculated - and the scores are shown in a doughnut chart - which also assign a verdict like **“High Hype”** or **“Mostly Negative”** to the video.  I also integrated **emoji sentiment extraction** becuase emojies these days carry a lot of important sentiment that users express, adding another layer of depth to understand nuanced audience reactions.

    #### 3. Interactive Word Clouds
    These **NLP-based word clouds** break down the most common phrases used in comments with **positive**, **negative**, and **overall** sentiments. This allows users to quickly see recurring themes in the audience’s feedback. The result is a visual representation of the conversation happening around a video.

    #### 4. Bigram Topic Extraction
    Using advanced NLP techniques, I extracted the top 20 topics from the comments. Each topic is plotted in an interactive chart. When users click on a topic, they can view the most liked and replied comments discussing that theme. This provides deeper insight into what specific parts of the video audience members are reacting to the most.

    ### Impact
    The dashboard gives marketing teams a clear view of how their content is performing and what audiences are buzzing about. By analyzing audience engagement in real time, companies can fine-tune their messaging, pinpoint popular segments, and gain insights into both positive and negative feedback.

    What’s more, the dashboard is not limited to YouTube. Its design is adaptable for other platforms like **Twitter** and **Instagram**, as well as industries beyond entertainment, including **product reviews**, **news events**, and **consumer feedback**.

    This project highlights my ability to blend **data science**, **NLP**, and **cloud computing** to build a scalable tool that transforms raw comments into meaningful insights. Stay tuned for more updates and screenshots!
    """)



elif selected_page == "Anonymization":
    # Custom CSS for tag-style words
    st.markdown("""
        <style>
        .tag {
            display: inline-block;
            padding: 5px 10px;
            margin: 5px;
            background-color: #f0f0f5;
            border-radius: 6px;
            border: 1px solid #ccc;
            font-size: 14px;
            color: #333;
            font-weight: bold;
        }
        .tag-container {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Project Description
    st.write("""
    # Text Data Anonymization & Analysis for Healthcare Services in Scotland

    This project, conducted in partnership with the **Argyll & Bute Health and Social Care Partnership (NHS)**, focused on developing a highly secure and GDPR-compliant solution to anonymize unstructured Electronic Health Records (EHR) data. By ensuring **100% removal of Personally Identifiable Information (PII)**, the tool enabled safe data sharing for research without compromising the utility of the data.

    ### Tools & Technologies
    """)

    # Tools & Technologies Tags
    st.markdown("""
    <div class="tag-container">
        <div class="tag">Python</div>
        <div class="tag">spaCy</div>
        <div class="tag">Named-Entity Recognition (NER)</div>
        <div class="tag">Natural Language Processing (NLP)</div>
        <div class="tag">Application Development</div>
        <div class="tag">Text Analytics</div>
        <div class="tag">Regex</div>
        <div class="tag">Custom Algorithm</div>
        <div class="tag">GDPR Compliance</div>
        <div class="tag">Data Anonymization</div>
        <div class="tag">Executable Workflow</div>
    </div>
    """, unsafe_allow_html=True)

    # Continue with Project Description
    st.write("""
    ### Project Overview
    In response to the need for secure, anonymized health records that comply with **GDPR regulations**, this project developed a robust tool to anonymize data without compromising its utility for research. The solution anonymized data for over **10,000 individuals**, ensuring secure data sharing within the healthcare sector while providing flexibility for broader applications in other industries.

    ### Key Features

    #### 1. Hybrid Anonymization System
    This project introduced a **two-layer anonymization system** using **spaCy’s Named Entity Recognition (NER)** combined with a **custom dictionary-based filter**. This approach allowed the tool to tag and remove sensitive data like names, addresses, and other PII from unstructured text, while still maintaining context and ensuring the data remained useful for research purposes.

    #### 2. Complete PII Removal with Perfect Recall
    The algorithm achieved a **perfect recall (1.0)**, ensuring no personal data was left exposed. The **transparency** of the tool was a significant factor in its compliance with GDPR standards, making sure every step of the anonymization process was trackable and verifiable.

    #### 3. Secure Workflow for Low-Clearance Users
    A standout feature of the tool was its **secure workflow**. The tool was designed to be used by personnel with **lower security clearance**, such as IT engineers, without exposing them to sensitive information. The anonymization process was fully encapsulated, ensuring that intermediate results and final outputs could **never be traced back to any individual**. This design allowed safe operation and handling of the tool without risking PII exposure, even in environments where users did not have high-level data access.

    #### 4. Flexible, Adaptable Design
    The **layered architecture** of the tool makes it easily adaptable for use across various industries beyond healthcare. The flexibility in its design allows for the anonymization of different types of unstructured data, making it applicable in fields such as finance, legal, and social services.

    ### Impact
    The tool anonymized the records of over **10,000 individuals**, facilitating secure and compliant data sharing for healthcare research. This project not only achieved **distinction** but was also praised for its innovative design and potential applications in other sectors. It demonstrated how cutting-edge data anonymization techniques can be deployed in real-world settings to handle sensitive data responsibly and effectively.
    """)


elif selected_page == "Movie":
    # Custom CSS for tag-style words
    # Custom CSS for tag-style words
    st.markdown("""
        <style>
        .tag {
            display: inline-block;
            padding: 5px 10px;
            margin: 5px;
            background-color: #f0f0f5;
            border-radius: 6px;
            border: 1px solid #ccc;
            font-size: 14px;
            color: #333;
            font-weight: bold;
        }
        .tag-container {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Project Description
    st.write("""
    # Movie Revenue Prediction Web App

    This interactive web app allows users to predict the box office revenue of a movie based on various factors such as the director, cast, genre, and runtime. It also accounts for **inflation adjustments** and **trend analysis** to predict the gross revenue in **2024**, offering a realistic forecast based on historical data and future projections.

    ### Tools & Technologies
    """)

    # Tools & Technologies Tags
    st.markdown("""
    <div class="tag-container">
        <div class="tag">Python</div>
        <div class="tag">Streamlit</div>
        <div class="tag">AWS (EC2)</div>
        <div class="tag">XGBoost</div>
        <div class="tag">LightGBM</div>
        <div class="tag">KNN</div>
        <div class="tag">Cosine Similarity</div>
        <div class="tag">Feature Engineering</div>
        <div class="tag">Data Augmentation</div>
        <div class="tag">Sprse Matrix</div>
        <div class="tag">Trend Analysis</div>
    </div>
    """, unsafe_allow_html=True)

    # Continue with Project Description
    st.write("""
    ### Project Overview
    The web app offers a **user-friendly interface** where users can input various movie-related features (such as **director**, **actors**, **genre**, **certificate**, and **runtime**) and receive a prediction of the movie’s potential revenue. The model adjusts for **inflation** and uses **trend analysis** to project the **gross revenue in 2024**, making the predictions both realistic and forward-looking.

    ### Key Features

    #### 1. Creative Feature Engineering
    Handling **categorical features** such as directors and actors required advanced **feature engineering** and **data augmentation**. The model deals with **sparse matrices**, creating meaningful relationships between features like director-actor pairings and genre combinations, enriching the dataset to provide accurate predictions.

    #### 2. Algorithm Experiments and Custom KNN Approach
    Initially, I experimented with popular algorithms like **XGBoost** and **LightGBM**, but ultimately implemented a **custom KNN-based approach** using **cosine similarity**. This method compares new movies against similar ones, estimating expected revenue by analyzing factors like cast, genre, and runtime. The combination of traditional algorithms and custom modeling allowed for greater flexibility and accuracy in the predictions.

    #### 3. Inflation Adjustment and 2024 Trend Prediction
    The model adjusts the **historical gross revenue** figures to match the expected **2024 value**. By applying **inflation rates** and conducting **trend analysis** based on box office patterns, the predictions account for future changes in movie revenue dynamics. This ensures that users get a **realistic prediction** of how much a movie could gross in 2024, reflecting both past trends and projected future growth.

    #### 4. User-Friendly Deployment on Streamlit
    The entire model is deployed using **Streamlit**, providing a clean, interactive interface for users to input movie features and get real-time predictions. Hosted on **AWS EC2**, the app is scalable, ensuring fast and reliable performance.

    ### Impact
    This web app provides a fun and interactive way to explore the factors that contribute to a movie’s success at the box office. It accounts for both **inflation adjustments** and **2024 trend projections**, offering realistic and forward-looking predictions. The project highlights creative problem-solving through **feature engineering**, **custom algorithms**, and the ability to deploy a user-friendly **machine learning model**.
    """)



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
